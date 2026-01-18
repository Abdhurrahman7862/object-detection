import cv2
from ultralytics import YOLO
import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty("rate", 140)

def speak(text):
    engine.say(text)
    engine.runAndWait()

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture(0)

last_command = ""
last_spoken_time = 0

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    frame_area = h * w
    center_x = w // 2

    command = "CLEAR PATH"

    results = model(frame, conf=0.5, verbose=False)

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        box_area = (x2 - x1) * (y2 - y1)
        distance_ratio = box_area / frame_area
        box_center = (x1 + x2) // 2

        if distance_ratio < 0.05:
            continue

        if distance_ratio > 0.22:
            command = "STOP"
            break

        if abs(box_center - center_x) < 120:
            command = "STOP"
            break
        elif box_center < center_x:
            command = "MOVE RIGHT"
        else:
            command = "MOVE LEFT"

    now = time.time()
    if command != last_command and now - last_spoken_time > 0.5:
        print(command)
        speak(command.lower())
        last_command = command
        last_spoken_time = now

    display = frame.copy()
    cv2.rectangle(display, (0, 0), (w, 70), (0, 0, 0), -1)
    cv2.putText(
        display,
        f"VOICE CMD: {command}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.4,
        (0, 255, 0) if command != "STOP" else (0, 0, 255),
        3,
    )

    cv2.imshow("Blind Assist Navigation", display)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
