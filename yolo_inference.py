# YOLO (You Only Look Once) is a popular convolutional neural network (CNN) architecture for object detection.
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from ultralytics import YOLO


# 1111111111111 First we want to predict with just the yolov8 model first 

# inital prediction using yolov8 did well at seeing all objects in video and images
# model = YOLO('yolov8x')  # Initialize model

# this is used to create the bounding box around, class label and confidence score.
# model.predict('input_videos/image.png', save=True)  # Inference on image

# 2222222222222 Now we want to predict with the yolov8 but just on the video and get the results and predeted video out
# model = YOLO('yolov8x')  # Initialize model

# we can create an LIST of numbrs by setting this to a variable.
# this process takes a while because it is processing the video frame by frame.
# result = model.predict('input_videos/input_video.mp4', save=True)

# 33333333 we now want to use the trained model yolo5_last.pt to see the tennis ball in the video.
# model = YOLO('models/yolo5_last.pt')  # Initialize model

# Predict tennis ball better with new model v5
#result = model.predict('input_videos/input_video.mp4', conf = 0.2, save=True)  # Inference on image

# 4444444444 we now want to revert buck to yolov8 and we want to track the players in the vedio
model = YOLO('yolov8x')  # Initialize model

result = model.track('input_videos/input_video.mp4', conf=0.2, save=True)  # Inference on video

print(result)
print("boxes:")
for box in result[0].boxes:
    print(box)