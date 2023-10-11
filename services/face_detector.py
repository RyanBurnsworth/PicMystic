import os
import cv2
from utils.utils import Utils

class FaceDetector:
    _capturing_face = True
    _utils: Utils

    def __init__(self):
        self._utils = Utils()
    
    """
        Keep the webcam on until a face is detected. Once a face is detected save the image.
        @returns the location of the image taken
    """
    def get_facial_image(self) -> str:
        saved_image = ""
        casc_path = os.getcwd() + "\\resources\\haarcascade_frontalface_default.xml"
        face_cascade = cv2.CascadeClassifier(casc_path)

        video_capture = cv2.VideoCapture(0)

        self._capturing_face = True

        while self._capturing_face:
            _, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

            faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
        
            if len(faces) > 0:
                current_directory = os.getcwd() + "\\images\\"
                saved_image = current_directory + self._utils.get_date_time_as_string() + ".png"
                cv2.imwrite(saved_image, frame)
                self._capturing_face = False
            
        video_capture.release()
        return saved_image

    def stop_face_detection(self):
        self._capturing_face = False
    