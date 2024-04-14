from ultralytics import YOLO

# Load the model
model = YOLO("yolov8n.pt")

# Training
results = model.train(
    data="pothole_v8.yaml",
    imgsz=1280,
    epochs=10,
    batch=8,
    name="yolov8n_v8_50e",
    device="mps",
)

# Export as onnx
model.export(format="onnx")
# Export as torch
model.export(format="torchscript")
# Export as tensor
model.export(format="tensorflow")
