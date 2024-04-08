# we want to be able to read the video frame by frame and also be able to 
# save it as frames.
from utils import (read_video, 
                   save_video)

def main():
    # path to the video
    input_video_path = "input_videos/input_video.mp4"
    # read in video frames from utils
    video_frames = read_video(input_video_path)
    
    # save the video and save to output_vidios folder
    save_video(video_frames, "output_videos/output_video.mp4")
    
    
    
if __name__ == "__main__":
    main()