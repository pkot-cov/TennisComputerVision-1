# how we are going to read and write videos
import cv2

def read_video(video_path):
    # read the video from the video path
    cap = cv2.VideoCapture(video_path)
    # empty list to store the frames
    frames = []
    # loop over till the frames are all read
    while True:
        # ret is fales if there are no frames to read.
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return cap

# we want to save the video 
def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()