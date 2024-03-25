# YOLO (You Only Look Once) is a popular convolutional neural network (CNN) architecture for object detection.
from ultralytics import YOLO

model = YOLO('yolov8x')  # Initialize model

model.predict('input_videos/image.png', save=True)  # Inference on image