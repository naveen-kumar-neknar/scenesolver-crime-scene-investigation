import os
import cv2
import json
import glob
import torch
import tempfile
from PIL import Image
from collections import Counter
from transformers import CLIPModel, CLIPProcessor, pipeline
from transformers import BlipProcessor, BlipForConditionalGeneration
from ultralytics import YOLO
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# --- Flask App Initialization ---
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# === Load Models (Done once on startup for performance) ===
print("🔌 Loading AI models, please wait...")

# Helper class for the classifier
class VisualCLIPClassifier(torch.nn.Module):
    def __init__(self, base_model, num_classes=5):
        super().__init__()
        self.clip = base_model
        self.classifier = torch.nn.Linear(self.clip.config.projection_dim, num_classes)

    def forward(self, pixel_values):
        with torch.no_grad():
            features = self.clip.get_image_features(pixel_values=pixel_values)
        return self.classifier(features)

# Define labels
label2id = {"fighting": 0, "robbery": 1, "shoplifting": 2, "explosion": 3, "normal": 4}
id2label = {v: k for k, v in label2id.items()}
evidence_labels = {0: "fire", 1: "smoke", 2: "fighting", 3: "gun", 4: "knife", 5: "shoplifting"}

# --- Model Loading ---
# Ensure you have your model files in a 'models' subfolder
CLIP_MODEL_PATH = os.path.join('models', 'visual_clip_classifier.pt')
YOLO_MODEL_PATH = os.path.join('models', 'evidence_best_epoch50.pt')

if not os.path.exists(CLIP_MODEL_PATH) or not os.path.exists(YOLO_MODEL_PATH):
    print(f"🚨 CRITICAL ERROR: Make sure '{CLIP_MODEL_PATH}' and '{YOLO_MODEL_PATH}' exist.")
    # Exit or handle as needed
    exit()

# Load CLIP
clip_base = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
visual_clip_model = VisualCLIPClassifier(clip_base, num_classes=5)
visual_clip_model.load_state_dict(torch.load(CLIP_MODEL_PATH, map_location="cpu"))
visual_clip_model.eval()
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load YOLO
yolo_model = YOLO(YOLO_MODEL_PATH)

# Load BLIP and BART
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").eval()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


print("✅ AI models loaded successfully.")

# === AI Processing Functions ===
def classify_with_yolo_override(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = clip_processor(images=image, return_tensors="pt")
    with torch.no_grad():
        logits = visual_clip_model(inputs["pixel_values"])
    clip_pred = id2label[logits.argmax().item()]

    yolo_results = yolo_model(image_path, verbose=False)[0]
    
    yolo_preds = [evidence_labels[int(cls)] for cls in yolo_results.boxes.cls.tolist()] if yolo_results.boxes else []
    
    # Extract bounding boxes and confidences for the 'foundObjects' field
    found_objects_details = []
    if yolo_results.boxes:
        for box in yolo_results.boxes:
            class_id = int(box.cls[0])
            found_objects_details.append({
                "object": evidence_labels.get(class_id, "unknown"),
                "match": round(float(box.conf[0]) * 100), # Convert confidence to percentage
                "box": [int(coord) for coord in box.xyxy[0].tolist()] # [x1, y1, x2, y2]
            })

    final_label = clip_pred
    if "gun" in yolo_preds or "knife" in yolo_preds:
        final_label = "robbery"
    elif "fighting" in yolo_preds:
        final_label = "fighting"
    elif "fire" in yolo_preds or "smoke" in yolo_preds:
        final_label = "explosion"
        
    return {
        "final_label": final_label,
        "clip_pred": clip_pred,
        "yolo_labels": yolo_preds,
        "found_objects_details": found_objects_details
    }

def generate_summary(captions):
    # This function remains the same as in your original code
    if not captions:
        return "No meaningful activity was detected in the video frames to generate a story."
    # ... (the rest of your generate_summary function)
    filtered = [c for c in set(captions) if not any(g in c.lower() for g in ["video game", "cover", "dark skies", "book"])]
    if not filtered:
        return "No meaningful activity was detected to generate a story."

    combined = " ".join(filtered)
    if len(combined) < 60: # If text is too short, summarizer might fail
        return combined

    try:
        # Limit the input to the summarizer model's max length
        max_input_length = summarizer.model.config.max_position_embeddings - 5
        summary = summarizer(combined[:max_input_length], max_length=150, min_length=40, do_sample=False)[0]["summary_text"]
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "A detailed narrative could not be generated from the scene's content."

def run_video_analysis(video_path, frame_skip=15):
    print(f"\n🎞 Processing Video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    try: 
        results, captions, all_yolo_objects = [], [], []
        frame_idx = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if frame_idx % frame_skip != 0:
                frame_idx += 1
                continue
            temp_path = os.path.join(tempfile.gettempdir(), f"frame_{frame_idx}.jpg")
            
            cv2.imwrite(temp_path, frame)
            try:
                yolo_result = classify_with_yolo_override(temp_path)
                results.append(yolo_result["final_label"])
                all_yolo_objects.extend(yolo_result['found_objects_details'])

                img = Image.open(temp_path).convert("RGB")
                blip_inputs = blip_processor(images=img, return_tensors="pt")
                blip_out = blip_model.generate(**blip_inputs, max_new_tokens=40)
                caption = blip_processor.decode(blip_out[0], skip_special_tokens=True)
                captions.append(caption)
            except Exception as frame_error:
                print(f"Warning: Could not process frame {frame_idx}. Error: {frame_error}")
            finally:
                 if os.path.exists(temp_path):
                    os.remove(temp_path) # Clean up the frame immediately

            frame_idx += 1
    finally:
        # --- THIS IS A CRITICAL FIX (FIXES PermissionError) ---
        # This ensures the video file handle is released before the script tries to delete it.
        print("Releasing video capture...")
        cap.release()

    if not results:
        return {"error": "Could not process any frames from the video."}
    
    # Determine final classification and evidence
    crime_counts = Counter(cat for cat in results if cat != 'normal')
    final_class = max(crime_counts, key=crime_counts.get) if crime_counts else 'normal'

    # Consolidate found objects
    unique_objects = {obj['object']: obj for obj in all_yolo_objects}
    found_objects = list(unique_objects.values())
    
    # Create final output matching the frontend schema
    full_story = generate_summary(captions)
    quick_caption = f"This video has been classified as '{final_class.capitalize()}'."

    # Generate keywords
    scene_keywords = [{"keyword": final_class.capitalize(), "match": 95}]
    yolo_labels = set(obj['object'] for obj in found_objects)
    for label in yolo_labels:
        scene_keywords.append({"keyword": label.capitalize(), "match": 88})

    return {
        "quickCaption": quick_caption,
        "fullStory": full_story,
        "sceneKeywords": scene_keywords,
        "foundObjects": found_objects
    }


# --- Flask API Endpoint ---
@app.route('/analyze', methods=['POST'])
def analyze_media():
    if 'media' not in request.files:
        return jsonify({"error": "No media file provided"}), 400
    
    file = request.files['media']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Use a try...finally block to ensure file cleanup happens no matter what
    try:
        file.save(filepath)
        print(f"Starting analysis for '{filename}' ({file.mimetype})...")
        results = {}

        if file.mimetype.startswith('video'):
            results = run_video_analysis(filepath)

        elif file.mimetype.startswith('image'):
            # --- THIS LOGIC IS NOW FIXED AND EXPANDED ---
            classification_results = classify_with_yolo_override(filepath)
            
            # Also generate a caption for the image
            img = Image.open(filepath).convert("RGB")
            blip_inputs = blip_processor(images=img, return_tensors="pt")
            blip_out = blip_model.generate(**blip_inputs, max_new_tokens=75)
            caption = blip_processor.decode(blip_out[0], skip_special_tokens=True)
            
            # Now, we manually build the same structure as the video analysis
            final_label = classification_results.get('final_label', 'unknown')
            yolo_labels = classification_results.get('yolo_labels', [])
            
            results = {
                "quickCaption": caption,
                "fullStory": f"The image has been classified as '{final_label}'. Key objects detected include: {', '.join(yolo_labels) if yolo_labels else 'none'}.",
                "sceneKeywords": [{"keyword": kw, "match": 90} for kw in set([final_label] + yolo_labels)],
                "foundObjects": classification_results.get('found_objects_details', [])
            }
        else:
            return jsonify({"error": "Unsupported file type"}), 400
            
        print("Analysis successful.")
        return jsonify(results)
            
    except Exception as e:
        print(f"🚨 An exception occurred during AI processing: {e}") 
        import traceback
        traceback.print_exc()
        return jsonify({"error": "An internal error occurred during AI model processing."}), 500
        
    finally:
        # This block will always run, ensuring the uploaded file is deleted
        if os.path.exists(filepath):
            print(f"Cleaning up file: {filepath}")
            # The 'cap.release()' in run_video_analysis should prevent PermissionErrors
            os.remove(filepath)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)