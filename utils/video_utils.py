import cv2 # how we are going to read and write videos

def read_video(video_path):
    # read the video from the video path
    cap = cv2.VideoCapture(video_path)
    # empty list to store the frames
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return video