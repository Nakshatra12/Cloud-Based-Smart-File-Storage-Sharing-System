# Cloud-Based-Smart-File-Storage-Sharing-System
To design and deploy a secure, scalable, and efficient cloud-based file storage system where users can upload, access, and share files through a web interface using cloud services.
#### This project allows users to:

✔ Sign up & log in
✔ Upload files
✔ Download files
✔ Store documents securely in Cloud Storage
✔ Save file metadata in Firestore
✔ Access the backend via Cloud Run
✔ Enjoy a clean, simple UI

### 👤 Author

S Nakshatra

## 📌 Table of Contents

Project Overview

Features

Technology Stack

Architecture

Project Structure

Backend API Endpoints

How to Run Locally

Deployment on Google Cloud

Screenshots / Demo

Future Enhancements

License

## 📖 Project Overview

This system is a Mini Google Drive-like cloud storage app, where users can:

Upload files into Google Cloud Storage

Authenticate using JWT

Fetch their personal files

Download files securely

View uploaded files on a dashboard

The backend runs on Google Cloud Run, making it fully serverless and scalable.

## ⭐ Features
### 🔐 User Management

Signup

Login

JWT authentication

### 📤 File Handling

Upload files

Auto-generate unique names

Store metadata in Firestore

Store files in Cloud Storage

### 📥 File Access

Download files

View file list

Open files in the browser

### ☁ Cloud Deployment

Backend deployed on Cloud Run

Files stored in GCP Storage Bucket

Metadata stored in Firestore

## 🛠 Technology Stack
### Frontend

HTML

CSS

JavaScript

### Backend

Python Flask

JWT Authentication

Gunicorn (for Cloud Run)

### Google Cloud Platform

Cloud Run

Cloud Storage

Firestore (NoSQL)

Artifact Registry

Cloud Build

## 🏛 Architecture
Frontend (HTML/JS)
        ↓
Cloud Run (Flask API)
        ↓
Cloud Storage  ← Stores files securely
        ↓
Firestore DB  ← Stores file metadata

## 📁 Project Structure
smart-drive-backend/
│── app.py
│── config.py
│── requirements.txt
│── Dockerfile
│── runtime.txt
│── .env
│
├── controllers/
│   ├── user_controller.py
│   └── file_controller.py
│
├── utils/
│   ├── jwt_token.py
│   └── auth.py
│
frontend/
│── index.html
│── signup.html
│── dashboard.html
│── script.js
│── style.css

## 🔌 Backend API Endpoints
### 🔹 Auth APIs
Method	Endpoint	Description
POST	/signup	Create user
POST	/login	Login & get JWT token
### 🔹 File APIs
Method	Endpoint	Description
POST	/upload	Upload file
GET	/files	List user files
DELETE	/delete/<filename>	Delete file
GET	/share/<filename>	Generate share link
### 💻 How to Run Locally
#### 1️⃣ Install dependencies
pip install -r requirements.txt

#### 2️⃣ Set environment variables

Create .env:

SECRET_KEY=your-secret-key
GCP_BUCKET_NAME=your-bucket-name
FIRESTORE_PROJECT_ID=your-project-id

#### 3️⃣ Run server
python app.py


Backend runs on:

http://127.0.0.1:5000

## ☁ Deployment (Google Cloud Run)
#### Build container:
gcloud builds submit --tag asia-south1-docker.pkg.dev/PROJECT_ID/smartdrive-repo/smartdrive .

#### Deploy:
gcloud run deploy smart-drive \
  --image asia-south1-docker.pkg.dev/PROJECT_ID/smartdrive-repo/smartdrive \
  --region asia-south1 \
  --allow-unauthenticated

## 🎥 Screenshots / Demo

demo video.

## 🚀 Future Enhancements

Folder support

Delete confirmation modal

Drag & Drop file upload

Shareable public links

File preview (PDF/Image)

User profile

📄 License

This project is for educational purposes.
