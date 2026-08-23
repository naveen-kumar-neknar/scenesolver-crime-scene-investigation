# 🧠 SceneSolver

> **SceneSolver** is an intelligent video analysis system designed to detect and summarize suspicious or criminal activities from visual data. It combines **CLIP, YOLOv8, BLIP, and BART** within a full-stack architecture built using **React, Node.js, Express, Flask, and MongoDB**.

---

## ✨ Overview

SceneSolver analyzes uploaded video content using multiple AI models, where each model performs a specific task in the analysis pipeline.

The system combines:

- 🔍 **CLIP** for crime classification
- 🎯 **YOLOv8** for evidence detection
- 🧠 **BLIP** for scene understanding and caption generation
- 📝 **BART** for scene summarization
- 👤 **User authentication** for account management
- 📂 **History tracking** for storing uploaded media and results
- 🌐 **React** for the frontend
- ⚙️ **Node.js + Express** for backend APIs
- 🤖 **Flask** for AI services
- 🗄️ **MongoDB** for application data

---

## 🚀 Key Features

### 🔍 Crime Classification

SceneSolver uses a fine-tuned **CLIP model** to identify activities such as:

- Robbery
- Fighting
- Shoplifting

### 🎯 Evidence Detection

**YOLOv8** is used to detect relevant objects and activities in video frames, such as:

- Weapons
- Violent actions

### 🧠 Scene Understanding

**BLIP** generates meaningful captions from visual content to provide a better understanding of the analyzed scene.

### 📝 Scene Summarization

**BART** summarizes the generated scene information into a concise representation of the analyzed situation.

### 👤 User Authentication

Users can:

- Register
- Log in
- Manage their personal dashboard

### 📂 History Tracking

The system stores uploaded media and corresponding analysis results for each user.

### 🌐 Full-Stack Architecture

The application is divided into three major services:

```text
React Frontend
      ↓
Node.js + Express Backend
      ↓
Flask AI Service
      ↓
CLIP + YOLOv8 + BLIP + BART
      ↓
MongoDB
```

---

## 🧠 AI Model Pipeline

Each AI model is responsible for a specific stage of the analysis.

### 🔍 CLIP — Crime Classification

The fine-tuned CLIP model identifies the type of suspicious activity.

```text
Visual Content
      ↓
     CLIP
      ↓
Crime Classification
```

---

### 🎯 YOLOv8 — Evidence Detection

YOLOv8 analyzes video frames and detects relevant evidence such as weapons or violent actions.

```text
Video Frame
      ↓
    YOLOv8
      ↓
Evidence Detection
```

---

### 🧠 BLIP — Scene Understanding

BLIP generates meaningful captions from the visual content.

```text
Visual Scene
      ↓
     BLIP
      ↓
Scene Caption
```

---

### 📝 BART — Scene Summarization

BART summarizes the generated scene information.

```text
Scene Information
      ↓
     BART
      ↓
Scene Summary
```

---

## 🔄 Complete Workflow

```text
User
  ↓
Uploads Video
  ↓
React Frontend
  ↓
Node.js + Express Backend
  ↓
Flask AI Service
  ↓
┌──────────────┬──────────────┬──────────────┐
│              │              │              │
▼              ▼              ▼              ▼
CLIP         YOLOv8          BLIP           BART
│              │              │              │
▼              ▼              ▼              ▼
Crime        Evidence       Scene          Scene
Class.       Detection      Caption        Summary
│              │              │              │
└──────────────┴──────────────┴──────────────┘
                       ↓
                    Results
                       ↓
                    MongoDB
                       ↓
                User Dashboard
```

---

## 📁 Project Structure

```text
SceneSolver/
│
├── scenesolver-frontend/       # React frontend
│
├── scenesolver-backend/        # Node.js + Express backend
│
├── scenesolver-ai-service/     # Flask AI services
│   ├── CLIP
│   ├── YOLOv8
│   ├── BLIP
│   └── BART
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Local Setup

SceneSolver consists of three services that need to be configured separately:

```text
1. Flask AI Service
2. Node.js + Express Backend
3. React Frontend
```

---

# 1️⃣ AI Service — Flask

Navigate to the AI service directory:

```bash
cd scenesolver-ai-service
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start the AI Service

```bash
python ai_service.py
```

The Flask service handles the AI functionality involving:

- CLIP
- YOLOv8
- BLIP
- BART

---

# 2️⃣ Backend — Node.js + Express + MongoDB

Open another terminal and navigate to:

```bash
cd scenesolver-backend
```

## Install Dependencies

```bash
npm install
```

## Configure Environment Variables

Create a `.env` file inside:

```text
scenesolver-backend/
```

Add:

```env
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
PORT=5000
```

### Environment Variables

| Variable | Description |
|---|---|
| `MONGO_URI` | MongoDB connection string |
| `JWT_SECRET` | Secret key used for authentication |
| `PORT` | Backend server port |

## Start the Backend

```bash
npm start
```

---

# 3️⃣ Frontend — React

Open another terminal and navigate to:

```bash
cd scenesolver-frontend
```

## Install Dependencies

```bash
npm install
```

## Configure Frontend Environment

Create a `.env` file inside:

```text
scenesolver-frontend/
```

Add:

```env
REACT_APP_API_URL=http://localhost:5000
```

## Start the Frontend

```bash
npm start
```

---

# 📦 Model Setup

Due to GitHub file size limitations, the trained model files are **not included in the repository**.

The required model resources can be prepared using the following notebooks.

## 🔗 CLIP Model Notebook

https://colab.research.google.com/drive/1lILPaN9OPIpBcgEXuFvqAVQ3ZahVIfoE?usp=sharing

## 🔗 YOLO Model Notebook

https://colab.research.google.com/drive/1hMxwK7XjemhPK60jJMHKrw2LfFu4vREd?usp=sharing

---

# 📌 Model Placement

After obtaining the required model file, place it inside:

```text
scenesolver-ai-service/models/
```

If the `models` directory does not already exist, create it:

```text
scenesolver-ai-service/
└── models/
```

The CLIP model should be placed at:

```text
scenesolver-ai-service/models/visual_clip_classifier.pt
```

### Expected Model Path

```text
SceneSolver/
│
└── scenesolver-ai-service/
    │
    └── models/
        └── visual_clip_classifier.pt
```

> ⚠️ **Important:** This step is mandatory. Without the required model file, the Flask AI service will not work correctly.

---

# 🗄️ MongoDB Configuration

SceneSolver uses MongoDB for application data.

Create the backend `.env` file:

```text
scenesolver-backend/.env
```

Configure:

```env
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
PORT=5000
```

### 🔐 Security

Never commit the `.env` file to GitHub.

Do not expose:

```text
MongoDB credentials
MongoDB connection strings
JWT secrets
Private keys
Other sensitive configuration
```

Use the `.gitignore` file to prevent sensitive files from being committed.

---

# 🌍 Deployment Notes

The project can be deployed as separate services.

### AI Service

The Flask AI service can be deployed using platforms such as:

- Render
- Railway
- AWS EC2

### Frontend and Backend

The frontend and backend can be hosted separately.

Example:

```text
React Frontend
      ↓
    Vercel

Node.js Backend
      ↓
    Render
```

### Database

**MongoDB Atlas** can be used for cloud database storage.

### Model Storage

Because trained model files are not included in the GitHub repository, model files can be hosted externally using services such as:

- Google Drive
- AWS S3

---

# 🔄 Example End-to-End Workflow

```text
1. User uploads a video containing suspicious activity
                         ↓
2. CLIP predicts the type of crime
                         ↓
3. YOLOv8 detects objects such as weapons or violent actions
                         ↓
4. BLIP generates scene captions
                         ↓
5. BART summarizes the situation
                         ↓
6. Analysis results are generated
                         ↓
7. Results are saved to the user's dashboard
```

---

# 🛠️ Service Communication

```text
                    React Frontend
                          │
                          ▼
                Node.js + Express
                     Backend
                          │
                          ▼
                   Flask AI Service
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
        CLIP            YOLOv8           BLIP
          │               │               │
          ▼               ▼               ▼
      Crime Type       Evidence         Caption
                                     
                          │
                          ▼
                         BART
                          │
                          ▼
                     Summary
                          │
                          ▼
                       MongoDB
```

---

# 📋 Quick Start

If the project has already been configured, the basic startup sequence is:

### Terminal 1 — AI Service

```bash
cd scenesolver-ai-service
venv\Scripts\activate
python ai_service.py
```

### Terminal 2 — Backend

```bash
cd scenesolver-backend
npm install
npm start
```

### Terminal 3 — Frontend

```bash
cd scenesolver-frontend
npm install
npm start
```

Then open the frontend application in the browser.

---

# 🚨 Important Setup Checklist

Before running the complete application, verify:

- [ ] Python is installed
- [ ] Node.js and npm are installed
- [ ] MongoDB connection is configured
- [ ] Backend `.env` file is created
- [ ] Frontend `.env` file is created
- [ ] Python dependencies are installed
- [ ] Node.js dependencies are installed
- [ ] Required model files are downloaded
- [ ] `visual_clip_classifier.pt` is placed inside the `models` directory
- [ ] Flask AI service is running
- [ ] Node.js backend is running
- [ ] React frontend is running

---

# 🤝 Contribution

Contributions are welcome.

For major changes, please open an issue first to discuss the proposed changes before making significant modifications.

---

# 👨‍💻 Author

**Neknar Naveen Kumar**

---

# 🔗 Connect With Me

**LinkedIn:**  
https://www.linkedin.com/in/neknar-naveen-kumar-2271a23b5

---

# 📜 License

This project is created for **academic and demonstration purposes**.
