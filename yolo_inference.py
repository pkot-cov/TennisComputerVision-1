# YOLO (You Only Look Once) is a popular convolutional neural network (CNN) architecture for object detection.
from ultralytics import YOLO

model = YOLO('yolov8x')  # Initialize model

# this is used to create the bounding box around, class label and confidence score.
# model.predict('input_videos/image.png', save=True)  # Inference on image

# we can create an LIST of numbrs by setting this to a variable.
# result = model.predict('input_videos/image.png', save=True)  # Inference on image

# repeat this for the video
# this process takes a while because it is processing the video frame by frame.
result = model.predict('input_videos/input_video.mp4', save=True)
print(result)
print("boxes:")
for box in result[0].boxes:
    print(box)