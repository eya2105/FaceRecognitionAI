# FaceRecognitionAI
## Face Recognition Login System (Django + AI)

This project is a facial recognition login system built with **Django** and powered by **AI-based face recognition** using the `face_recognition` Python library. Users can authenticate themselves by capturing a photo using their webcam or by entering their username and password.

---

## Features

- Login via facial recognition (webcam capture)
- Traditional username/password login
- Real-time webcam capture in the browser
- AI-powered face encoding and comparison
- Reload/reset webcam interface with one click
- Preview of captured photo before submission
- Smooth integration with Django backend

---

## How AI is Used

The system uses the [`face_recognition`](https://github.com/ageitgey/face_recognition) library, which is built on **deep learning models** (ResNet CNNs) trained to:
- Detect faces in images
- Encode faces into 128-dimensional embeddings
- Compare unknown faces to a database of known encodings
- Identify and classify users based on face similarity


---
