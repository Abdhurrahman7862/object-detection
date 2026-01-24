# 🦯 Blind Assist Navigation (Object Detection)

This repository implements a **real-time navigation assistant** for visually impaired users using a webcam and object detection.

It detects obstacles and gives **spoken navigation commands** (e.g., clear path, stop, move left, move right).

---

## 🧠 Features

- ✔️ Real-time object detection using **YOLOv8**
- ✔️ Voice feedback using **pyttsx3**
- ✔️ On-screen status display
- ✔️ Simple directional guidance logic

---

## 📦 Requirements

This project uses **Python 3.8+** and the following packages:

- `ultralytics` – YOLOv8 object detection  
- `opencv-python` – video capture & display  
- `pyttsx3` – offline text-to-speech  
- `numpy`

---

## 🛠️ Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Abdhurrahman7862/object-detection.git
    cd object-detection
    ```

2. Create and activate a virtual environment (**recommended**):
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux / macOS
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies:
   
---

## 📄 requirements.txt

    ```txt
    ultralytics
    opencv-python
    pyttsx3
    numpy
    ```

    ```bash
    pip install -r requirements.txt
    ```
    download --> https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt

---

## ▶️ Running the App

Make sure your webcam is connected, then run:

```bash
python try.py





