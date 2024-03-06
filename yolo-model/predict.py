from ultralytics import YOLO

model = YOLO('runs/detect/yolo8n_v8_50e2/weights/best.pt')
model.predict('pothole1.png')
