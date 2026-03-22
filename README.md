# 🧠 SceneSolver

SceneSolver is an intelligent video analysis system designed to detect and summarize suspicious or criminal activities from visual data. It combines multiple advanced AI models such as CLIP, YOLOv8, BLIP, and BART within a full-stack architecture built using React, Node.js, and Flask.

---

## 🚀 Key Features

* 🔍 **Crime Classification**
  Identifies activities like robbery, fighting, or shoplifting using a fine-tuned CLIP model.

* 🎯 **Evidence Detection**
  Utilizes YOLOv8 to detect objects such as weapons or violent actions in frames.

* 🧠 **Scene Understanding**
  Generates meaningful captions with BLIP and produces summaries using BART.

* 👤 **User Authentication**
  Allows users to register, log in, and manage their personal dashboard.

* 📂 **History Tracking**
  Stores uploaded media and corresponding results for each user.

* 🌐 **Full-Stack System**
  Flask handles AI services, Node.js manages backend APIs, and React powers the frontend UI.

---

## 📁 Project Structure

```
SceneSolver/
│
├── scenesolver-frontend/       # React frontend
├── scenesolver-backend/        # Node.js + Express backend
├── scenesolver-ai-service/     # Flask AI services (CLIP, YOLO, BLIP, BART)
├── .gitignore
└── README.md
```

---

## ⚙️ Local Setup Guide

### 1️⃣ AI Service (Flask)

```bash
cd scenesolver-ai-service

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run service
python ai_service.py
```

---

### 2️⃣ Backend (Node.js + MongoDB)

```bash
cd scenesolver-backend

# Install dependencies
npm install
```

Create a `.env` file inside `scenesolver-backend/`:

```
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
PORT=5000
```

Start backend:

```bash
npm start
```

---

### 3️⃣ Frontend (React)

```bash
cd scenesolver-frontend

npm install
```

Create `.env` inside frontend:

```
REACT_APP_API_URL=http://localhost:5000
```

Run frontend:

```bash
npm start
```

---

## 📦 Model Setup

Due to GitHub file size limitations, trained model files are not included in the repository.

You can download and use them from the following resources:

* 🔗 CLIP Model Notebook:
  https://colab.research.google.com/drive/1lILPaN9OPIpBcgEXuFvqAVQ3ZahVIfoE?usp=sharing

* 🔗 YOLO Model Notebook:
  https://colab.research.google.com/drive/1hMxwK7XjemhPK60jJMHKrw2LfFu4vREd?usp=sharing

Place the downloaded model file inside:

```
scenesolver-ai-service/models/
```

---

## 🌍 Deployment Notes

* AI service can be deployed using platforms like Render, Railway, or AWS EC2.
* Frontend and backend can be hosted separately (e.g., Vercel + Render).
* MongoDB Atlas can be used for cloud database storage.
* Model files should be hosted externally (Google Drive, AWS S3, etc.).

---

## 🔄 Example Workflow

1. User uploads a video containing suspicious activity
2. CLIP predicts the type of crime
3. YOLO detects objects like weapons or fights
4. BLIP generates scene captions
5. BART summarizes the situation
6. Results are saved to the user's dashboard

---

## 🤝 Contribution

Contributions are welcome. For major changes, please open an issue first to discuss your ideas.

---

## 👨‍💻 Author

Developed by **Neknar Naveen Kumar**

---
