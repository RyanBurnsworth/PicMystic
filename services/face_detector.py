import os
import cv2
from utils.utils import Utils

class FaceDetector:
    _capturing_face = True
    _utils: Utils

    def __init__(self):
        self._utils = Utils()
    
    def start_face_detection(self) -> str:
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
                saved_image = current_directory + self._utils.getDateTimeAsString() + ".png"
                cv2.imwrite(saved_image, frame)
                self._capturing_face = False
            
            cv2.imshow('Video', frame)

        video_capture.release()
        cv2.destroyAllWindows()
        return saved_image

    def stop_face_detection(self):
        self._capturing_face = False
    