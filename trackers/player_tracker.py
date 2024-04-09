# we are going to create the tracking for the playes in the video
from ultralytics import YOLO
import cv2
import pickle

class PlayerTracker:
    # we can change the model we want to use for tracking
    def __init__(self,model_path):
        self.model = YOLO(model_path)
     
     
    # this function will be able to detect muiltiple frames
    def detect_frames(self,frames, read_from_stub=False, stub_path=None):
        # output a list to store the players in the frame
        players_detections= []
        
        if read_from_stub and stub_path is not None:
            with open(stub_path, "rb") as f:
                players_detections = pickle.load(f)
            return players_detections
        
        # loop over the frames
        for frame in frames:
            # detect the players in the frame
            player_dict = self.detect_frame(frame)
            players_detections.append(player_dict)
            
        if stub_path is not None:
            with open(stub_path, "wb") as f:
                pickle.dump(players_detections, f)
            
        return players_detections
       
    # we are going to detect the players in the frame
    def detect_frame(self,frame):
        # persist=True means that the tracker will remember the object from the previous frame
        results = self.model.track(frame, persist=True)[0] 
        # map id's to names
        id_name_dict = results.names
        
        # output a dictionary to store the players id as key and the bounding box as value
        player_dict = {}
        # only choose bounding boxes that are people
        for box in results.boxes:
            # get the track id (number above the player)
            track_id = int(box.id.tolist()[0])
            # get the bounding box coordinates keep in the xyxy format
            result = box.xyxy.tolist()[0]
            # get the class id of the object
            object_cls_id = box.cls.tolist()[0]
            # map the id to the name of the object
            object_cls_name = id_name_dict[object_cls_id]
            # only choose the bounding boxes that are people
            if object_cls_name == "person":
                player_dict[track_id] = result
                
        return player_dict
    
    
    # draw bounding boxes on the frame
    def draw_boxes(self,video_frames,player_detection):
        output_video_frames = []
        # loop over the players in the frame
        for frame, player_dict in zip(video_frames, player_detection):
            # draw the bounding box on the frame
            for track_id, bbox in player_dict.items():
                x1, y1, x2, y2 = bbox
                cv2.putText(frame, f"Player ID: {track_id}", (int(bbox[0]), int(bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)
            output_video_frames.append(frame)
        return output_video_frames