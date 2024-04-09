# we want to be able to read the video frame by frame and also be able to 
# save it as frames.
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

from utils import (read_video, 
                   save_video)
from trackers import PlayerTracker

def main():
    # read video from input_videos folder   s
    input_video_path = "input_videos\input_video.mp4"
    # read in video frames from utils
    video_frames = read_video(input_video_path)
    
    # detect the players in the video
    # initialize the player tracker with YOLOv8x model
    player_tracker = PlayerTracker(model_path="yolov8x")
    # given the video frames, detect the players in the frames
    player_detections = player_tracker.detect_frames(video_frames,
                                                     read_from_stub=True,
                                                     stub_path="tracker_stubs/player_detections.pkl")
    
    #draw output
    
    ## draw bounding boxes on the frame
    output_video_frames = player_tracker.draw_boxes(video_frames, player_detections)
    
    # save the video and save to output_vidios folder
    save_video(video_frames, "output_videos/output_video.mp4")
    
    
    
if __name__ == "__main__":
    main()  