# Tennis Match Analysis Project

## Overview

This project aims to bring computer vision technologies into the realm of tennis sports analytics. By utilizing advanced machine learning models, the system is designed to detect and track players and tennis balls throughout video footage of matches. This projects solution extends beyond simple tracking; it comprehensively understands the spatial dynamics of the game by detecting key points of the tennis court. This allows for an in-depth analysis of player positioning, ball trajectories, distances covered, and the precision of shots. 

## Features

- **Player and Ball Detection**: Utilizes YOLO, an object detection model, to accurately detect and track fast-moving tennis balls and players in real-time.
- **Court Key Points Detection**: Employs a Convolutional Neural Network (CNN) trained to identify the court's key points, assisting in strategic analysis.
- **Gameplay Analysis**:
  - Determines whether shots are in or out.
  - Counts the number of shots hit by each player.
  - Measures the velocity of each shot.
- **Player Movement Analysis**:
  - Calculates the speed of the players.
  - Evaluates the total distance covered by each player during a match.

## Technology Stack

- **PyTorch**: The project uses PyTorch to train both the YOLO and CNN models, leveraging its dynamic computational graph and efficient memory usage for high-speed analysis.
- **Object Detection Model (YOLO)**: Fine-tuned to enhance the detection accuracy of the default out-of-the-box models for the high-speed context of tennis.
- **Convolutional Neural Network**: Custom-built and trained to estimate the tennis court's key points, enabling a nuanced understanding of player positions and game dynamics.

## Getting Started

### Analyzing a Single Frame

To begin our analysis, we start with a static image of a tennis match. This initial step helps us understand the basics of image detection using the YOLO model.

Original Image:
![Original Tennis Match Image](input_videos/image.png)

After running this image through the YOLO model, we observe the following results:

Predicted Image:
![YOLO Predicted Image](runs/detect/predict/image.png)

In the predicted image, we can see that YOLO successfully detects various objects, including people, tennis rackets, and a clock. Each detected object is surrounded by a bounding box, accompanied by a class name and a confidence score, indicating the model's certainty about the object's identity.

### Analyzing a Video Sequence

Next, we apply YOLO to a video of a tennis match. In this scenario, YOLO analyzes each frame of the video and assigns bounding boxes, class names, and confidence scores to all detected objects.

Video Analysis:
![YOLO Video Analysis](runs/detect/predict3/input_video.gif)

However, we notice that the detection of the tennis ball (classified as "sports ball") is inconsistent across frames. To improve our analysis and gather more detailed information, we will need to fine-tune a detector model specifically for the tennis ball.

## Refining the YOLO Model for Tennis Ball Detection

To enhance the accuracy of our YOLO model in detecting tennis balls, we will utilize a specialized training dataset tailored for this purpose. This dataset is available on Roboflow and can be accessed via the following link:

[Tennis Ball Detection Dataset on Roboflow](https://universe.roboflow.com/viren-dhanwani/tennis-ball-detection)
![Sample Image from Dataset](readme_folder/fed3_jpg.rf.09d2a51b2725b6734cf7c512f9eab272.jpg)


The dataset utilized for refining the YOLO model is a collection of images capturing tennis court scenes, closely resembling the initial image used in our analysis. It includes aerial photographs of tennis courts with the tennis ball in motion, often appearing blurry due to its high speed. Each image in the dataset is annotated with bounding boxes that precisely outline the tennis ball, providing essential training data for improving the model's detection accuracy (Bounding Box [0 0.58359375 0.4861111111111111 0.0125 0.025] the first number is the class the last for are the bounding box).

### Dataset Composition:

- **Total Images**: 578
- **Training Set**: 428 images
- **Validation Set**: 100 images
- **Test Set**: 50 images

This dataset is instrumental in training our YOLO model to better detect and track tennis balls, particularly in challenging conditions where the ball is moving rapidly. By fine-tuning our model with this dataset, we aim to enhance its performance in real-time tennis match analysis.

### Improving Object Detection with the Refined YOLOv5 Model

After training the YOLOv5 model to enhance the detection of tennis balls, we observed a significant improvement in the model's ability to track the ball. However, this specialization led to a trade-off where the model's capability to detect other objects like players, chairs, and clocks diminished. To address this issue and achieve a more balanced object detection performance, we plan to implement the following steps:

![Improved Ball Detection](runs/detect/predict4/input_video.gif)

1. **Multi-Task Learning**: Integrate a multi-task learning approach where the model is trained to perform both tasks - detecting the tennis ball and other relevant objects simultaneously. This can be achieved by using a shared backbone network with separate branches for different tasks.

2. **Data Augmentation**: Enhance the training dataset with more diverse images that include various objects present in a tennis match. This will help the model learn to recognize a wider range of objects along with the tennis ball.

3. **Fine-Tuning with Balanced Dataset**: Re-train the model with a balanced dataset that includes an equal proportion of images with tennis balls and other objects. This will prevent the model from being overly biased towards detecting only the tennis ball.

4. **Ensemble Models**: Consider using an ensemble of models where one model is specialized in detecting the tennis ball, and another model is trained to detect other objects. The final detections can be combined to achieve comprehensive object detection in the scene.

By implementing these steps, we aim to refine the YOLOv5 model further to not only excel in tennis ball detection but also maintain its ability to detect other important objects in the tennis match, providing a holistic analysis of the game.






## Contributing

(Include guidelines on how others can contribute to the project.)

## License

(Include information about the project's license here, if applicable.)

## Contact

(Your contact information or that of the project maintainer.)


# Tennis Match Analyzer with YOLOv8x

This project utilizes the YOLOv8x (You Only Look Once, version 8x) object detection model to analyze and identify various elements in a live tennis match. The image demonstrates the model's ability to detect and classify objects with bounding boxes and confidence scores in real-time.
![Initial Image of tennis match](/input_videos/image.png)


## Features

- **Real-Time Object Detection**: Using the YOLOv8x model, the application identifies and labels different objects in a tennis match scene.
- **Confidence Scoring**: Each object is recognized with a confidence score, reflecting the model's certainty about the object's identification.
- **Multi-Object Classification**: The model simultaneously classifies multiple objects, including tennis players, audience members, chairs, and sports equipment.
- **Sports Analytics**: This application can be utilized for sports analytics, providing insights into player positions, game statistics, and audience engagement.

## Application in Action

The provided image from a tennis match shows the YOLOv8x model's output. The model highlights:

- Bounding box.
- class name.
- Confidence score.
- Players on the court.
- Spectators around the court.
- The chair umpire.
- Tennis equipment, including the ball and racket.
![inital prediction](/runs/detect/predict/image.png)
Each object is enclosed in a bounding box with a label and a confidence score (e.g., 'person 0.83', 'clock 0.36', 'sports ball 0.50').

## Potential Use Cases

- **Player Performance Tracking**: Analyzing player movements and positions to aid in performance improvement strategies.
- **Audience Analysis**: Monitoring audience size and engagement levels.
- **Equipment Detection**: Keeping track of the ball and equipment for automated scoring systems.

## Future Enhancements

- Enhancing the model for even higher accuracy and speed.
- Expanding the number of recognizable objects specific to various sports.
- Integrating with video feeds for live match analysis.
