# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 08:46:28 2024

@author: kalya
"""

import cv2
import supervision as sv
from ultralytics import YOLO

#read the video
#video = cv2.VideoCapture('car2.mp4')
video = cv2.VideoCapture(0)
model = YOLO('yolov8s.pt')
bbox_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()


while video.isOpened():
    rect, frame = video.read()
    #reduce the frame size
    frame = cv2.resize(frame, (700,500))
    if rect == True:
        result = model(frame)[0]
        detections = sv.Detections.from_ultralytics(result)
        detections = detections[detections.confidence > .5]
        labels =[
            result.names[class_id]
            for class_id 
            in detections.class_id
        ]
        frame = bbox_annotator.annotate( scene = frame , detections = detections)
        frame = label_annotator.annotate(scene = frame , detections = detections, 
                                        labels =labels)
        #fps = video.get(cv2.cv.CV_CAP_PROP_FPS )
        #print('vediorate',fps)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()