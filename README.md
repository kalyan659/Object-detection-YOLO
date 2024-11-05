# Object-detection-YOLO
## YOLOv8s Camera Object Detection

This repository provides a Python script for real-time object detection using the YOLOv8s model. The script captures video from your webcam and detects objects within the frames.




https://github.com/user-attachments/assets/31457564-51b0-4dda-ad2a-4de7bedb88aa


## Requirements:

Python 3.x
Ultralytics YOLOv8 package (install using pip install ultralytics)
OpenCV
## Usage:

Clone this repository.
Place your YOLOv8s weights file (e.g., yolov8s.pt) in the same directory.
Run the script: python object_detection.py
## Customization:

Model: Change the model name in the script to use a different YOLOv8 model (e.g., yolov8n, yolov8x).
Confidence: Adjust the confidence threshold to control the sensitivity of object detection.

## Additional Notes:

The script assumes your webcam is connected and accessible.
For better performance, consider using a GPU-enabled environment.
Experiment with different YOLOv8 models and parameters to optimize results for your specific use case.
