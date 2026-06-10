from ultralytics import YOLO

model = YOLO("yolov8m.pt")

important_objects = [
    "person",
    "chair",
    "couch",
    "bench",
    "car",
    "bus",
    "truck",
    "bicycle",
    "motorcycle"
]