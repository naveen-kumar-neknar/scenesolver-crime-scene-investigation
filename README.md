# 🧠 SceneSolver – AI-Powered Video Analysis and Scene Summarization

> An intelligent video analysis system designed to detect and summarize suspicious or criminal activities from visual data using **CLIP, YOLOv8, BLIP, and BART** within a full-stack architecture built using **React, Node.js, Express, Flask, and MongoDB**.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![CLIP](https://img.shields.io/badge/AI-CLIP-purple)
![YOLOv8](https://img.shields.io/badge/Object%20Detection-YOLOv8-green)
![BLIP](https://img.shields.io/badge/Scene%20Understanding-BLIP-orange)
![BART](https://img.shields.io/badge/Summarization-BART-blue)
![Flask](https://img.shields.io/badge/AI%20Service-Flask-black?logo=flask)
![Node.js](https://img.shields.io/badge/Backend-Node.js-green?logo=node.js)
![Express](https://img.shields.io/badge/Backend-Express-black?logo=express)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?logo=react)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green?logo=mongodb)

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Key Features](#-key-features)
- [Use Cases](#-use-cases)
- [Technology Stack](#-technology-stack)
- [AI Models](#-ai-models)
- [AI Processing Workflow](#-ai-processing-workflow)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation and Setup](#-installation-and-setup)
- [AI Service Setup](#-ai-service-setup)
- [Backend Setup](#-backend-setup)
- [Frontend Setup](#-frontend-setup)
- [Model Setup](#-model-setup)
- [Model File Location](#-model-file-location)
- [Running the Application](#-running-the-application)
- [Complete End-to-End Setup](#-complete-end-to-end-setup)
- [Deployment Notes](#-deployment-notes)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Future Scope](#-future-scope)
- [Contribution](#-contribution)
- [Author](#-author)
- [License](#-license)

---

# 🚀 Project Overview

SceneSolver is an intelligent video analysis system designed to detect and summarize suspicious or criminal activities from visual data.

The project combines multiple advanced AI models, where each model performs a specific task in the video analysis pipeline.

The system uses:

```text
CLIP
 ↓
Crime Classification

YOLOv8
 ↓
Evidence Detection

BLIP
 ↓
Scene Understanding

BART
 ↓
Scene Summarization
```

These AI capabilities are integrated into a full-stack application consisting of:

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

The application allows users to register, log in, upload media, analyze the content, and view the corresponding results through their personal dashboard.

---

# 🎯 Problem Statement

Analyzing video footage containing suspicious or criminal activities can require identifying multiple types of information from the same visual data.

SceneSolver addresses this by combining multiple AI models into a single analysis system.

The system focuses on:

- Identifying suspicious activities.
- Detecting relevant evidence.
- Understanding visual scenes.
- Generating scene captions.
- Summarizing the analyzed information.
- Maintaining user-specific analysis history.

---

# 🎯 Objectives

The main objectives of SceneSolver are:

1. Detect suspicious or criminal activities from visual data.
2. Classify activities such as robbery, fighting, and shoplifting.
3. Detect relevant evidence such as weapons or violent actions.
4. Generate meaningful captions from visual scenes.
5. Summarize analyzed scene information.
6. Provide user registration and login functionality.
7. Provide a personal user dashboard.
8. Store uploaded media and corresponding results for each user.
9. Integrate multiple AI models into a single full-stack application.

---

# ✨ Key Features

## 🔍 Crime Classification

SceneSolver uses a **fine-tuned CLIP model** to identify activities such as:

- Robbery
- Fighting
- Shoplifting

---

## 🎯 Evidence Detection

The system uses **YOLOv8** to detect relevant objects and activities in video frames.

Examples include:

- Weapons
- Violent actions

---

## 🧠 Scene Understanding

**BLIP** generates meaningful captions from visual content.

This provides textual information describing the analyzed scene.

---

## 📝 Scene Summarization

**BART** produces summaries from the generated scene information.

This converts the analyzed information into a concise representation of the situation.

---

## 👤 User Authentication

The application allows users to:

- Register
- Log in
- Manage their personal dashboard

---

## 📂 History Tracking

The system stores:

- Uploaded media
- Corresponding analysis results

for each user.

Users can access their previous results through their dashboard.

---

## 🌐 Full-Stack System

SceneSolver uses a complete full-stack architecture:

```text
React
  ↓
Node.js + Express
  ↓
Flask
  ↓
AI Models
```

Flask handles AI services, Node.js manages backend APIs, and React powers the frontend UI.

---

# 👨‍💻 Use Cases

## 🚨 Suspicious Activity Analysis

Users can upload video containing suspicious activity and process it through the AI pipeline.

## 🔍 Crime Classification

The system can identify activities such as:

- Robbery
- Fighting
- Shoplifting

## 🎯 Evidence Detection

YOLOv8 can detect relevant objects and activities such as:

- Weapons
- Violent actions

## 🧠 Scene Understanding

BLIP generates meaningful captions from visual content.

## 📝 Scene Summarization

BART summarizes the analyzed scene information.

## 👤 Personal Dashboard

Users can manage their account and access their uploaded media and corresponding results.

---

# 🧰 Technology Stack

| Category | Technology |
|---|---|
| Frontend | React |
| Backend | Node.js + Express |
| AI Service | Flask |
| Database | MongoDB |
| Crime Classification | CLIP |
| Evidence Detection | YOLOv8 |
| Scene Understanding | BLIP |
| Summarization | BART |
| Programming | Python, JavaScript |
| Version Control | Git / GitHub |

---

# 🤖 AI Models

## 🔍 CLIP

A fine-tuned **CLIP model** is used for crime classification.

It identifies activities such as:

```text
Robbery
Fighting
Shoplifting
```

---

## 🎯 YOLOv8

YOLOv8 is used for evidence detection.

It detects objects and activities such as:

```text
Weapons
Violent Actions
```

---

## 🧠 BLIP

BLIP is used for scene understanding and generates meaningful captions from visual content.

---

## 📝 BART

BART is used to generate summaries from the analyzed scene information.

---

# 🔄 AI Processing Workflow

The AI pipeline follows this sequence:

```text
User Uploads Video
        ↓
Visual Data Processing
        ↓
CLIP
        ↓
Crime Classification
        ↓
YOLOv8
        ↓
Evidence Detection
        ↓
BLIP
        ↓
Scene Caption
        ↓
BART
        ↓
Scene Summary
        ↓
Final Results
```

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                 ┌─────────────────┐
                 │ React Frontend  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Node.js +       │
                 │ Express Backend │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Flask AI       │
                 │  Service        │
                 └────────┬────────┘
                          │
            ┌─────────────┼─────────────┐
            │             │             │
            ▼             ▼             ▼
          CLIP          YOLOv8         BLIP
            │             │             │
            ▼             ▼             ▼
      Crime Type       Evidence      Captions
                       Detection
            │             │             │
            └─────────────┼─────────────┘
                          │
                          ▼
                         BART
                          │
                          ▼
                   Scene Summary
                          │
                          ▼
                       MongoDB
                          │
                          ▼
                   User Dashboard
```

---

# 📁 Project Structure

```text
SceneSolver/
│
├── scenesolver-frontend/       # React frontend
│
├── scenesolver-backend/        # Node.js + Express backend
│
├── scenesolver-ai-service/     # Flask AI services
│
├── .gitignore
│
└── README.md
```

The AI service contains:

```text
scenesolver-ai-service/
│
├── CLIP
├── YOLOv8
├── BLIP
└── BART
```

---

# 💻 Requirements

Before running SceneSolver, make sure the following are available:

- Python
- pip
- Node.js
- npm
- MongoDB
- Git

The project also requires the trained model files described in the **Model Setup** section.

---

# ⚙️ Installation and Setup

SceneSolver consists of three main services:

```text
1. Flask AI Service
2. Node.js + Express Backend
3. React Frontend
```

Each service must be configured separately.

---

# 🧠 AI Service Setup

Navigate to:

```bash
cd scenesolver-ai-service
```

Create a Python virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask AI service:

```bash
python ai_service.py
```

---

# ⚙️ Backend Setup

Navigate to:

```bash
cd scenesolver-backend
```

Install dependencies:

```bash
npm install
```

## 🔐 Backend Environment Configuration

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

Start the backend:

```bash
npm start
```

---

# 🌐 Frontend Setup

Navigate to:

```bash
cd scenesolver-frontend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file inside:

```text
scenesolver-frontend/
```

Add:

```env
REACT_APP_API_URL=http://localhost:5000
```

Run the frontend:

```bash
npm start
```

---

# 📦 Model Setup

Due to GitHub file size limitations, trained model files are **not included in the repository**.

The model resources can be obtained from the following notebooks.

### 🔗 CLIP Model Notebook

https://colab.research.google.com/drive/1lILPaN9OPIpBcgEXuFvqAVQ3ZahVIfoE?usp=sharing

### 🔗 YOLO Model Notebook

https://colab.research.google.com/drive/1hMxwK7XjemhPK60jJMHKrw2LfFu4vREd?usp=sharing

---

# 📌 Model File Location

After obtaining the model file, navigate to:

```text
scenesolver-ai-service/
```

If the `models` folder does not exist, create it:

```text
models/
```

Place the model file at:

```text
scenesolver-ai-service/models/visual_clip_classifier.pt
```

The final structure should be:

```text
scenesolver-ai-service/
│
├── models/
│   └── visual_clip_classifier.pt
│
└── ...
```

> ⚠️ **Important:** This step is mandatory. Without the required model file, the Flask AI service will not work.

---

# 🚀 Running the Application

Three services need to run separately.

## Terminal 1 — AI Service

```bash
cd scenesolver-ai-service
venv\Scripts\activate
python ai_service.py
```

## Terminal 2 — Backend

```bash
cd scenesolver-backend
npm install
npm start
```

## Terminal 3 — Frontend

```bash
cd scenesolver-frontend
npm install
npm start
```

---

# 🔄 Complete End-to-End Setup

Once all three services are running:

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
CLIP
  ↓
Crime Classification
  ↓
YOLOv8
  ↓
Evidence Detection
  ↓
BLIP
  ↓
Scene Captions
  ↓
BART
  ↓
Scene Summary
  ↓
Results
  ↓
User Dashboard
  ↓
MongoDB
```

---

# 🌍 Deployment Notes

The AI service can be deployed using platforms such as:

- Render
- Railway
- AWS EC2

The frontend and backend can be hosted separately.

Example:

```text
Frontend → Vercel
Backend  → Render
```

MongoDB Atlas can be used for cloud database storage.

Since trained model files are not included in the repository, they can be hosted externally using:

- Google Drive
- AWS S3

---

# 🔐 Security

Sensitive configuration must not be committed to GitHub.

Never upload:

```text
.env
MongoDB credentials
MongoDB connection strings
JWT secrets
Private credentials
```

Keep backend secrets inside:

```text
scenesolver-backend/.env
```

Keep the frontend API configuration inside:

```text
scenesolver-frontend/.env
```

---

# 🛠️ Troubleshooting

## AI Service Not Working

Verify:

```text
Python is installed
Virtual environment is activated
requirements.txt is installed
Required model file exists
```

Run:

```bash
pip install -r requirements.txt
```

---

## Backend Not Working

Verify:

```text
Node.js is installed
npm install was completed
.env exists
MONGO_URI is configured
JWT_SECRET is configured
```

Then run:

```bash
npm start
```

---

## Frontend Not Working

Verify that dependencies are installed:

```bash
npm install
```

Check:

```env
REACT_APP_API_URL=http://localhost:5000
```

Then run:

```bash
npm start
```

---

## Model Not Found

Verify that the required CLIP model exists at:

```text
scenesolver-ai-service/models/visual_clip_classifier.pt
```

---

# 🚧 Future Scope

Based strictly on the provided project information, no specific future improvements were defined.

Future development can be added to this section as the project evolves.

---

# 🤝 Contribution

Contributions are welcome.

For major changes, please open an issue first to discuss your ideas.

---

# 👨‍💻 Author

## Neknar Naveen Kumar

Developed by **Neknar Naveen Kumar**.

---

# 🔗 Connect

### LinkedIn

https://www.linkedin.com/in/neknar-naveen-kumar-2271a23b5

---

# 📜 License

This project is created for **academic and demonstration purposes**.
