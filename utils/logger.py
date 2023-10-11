from datetime import datetime
from constants import Constants

class Logger:
    def __init__(self):
        print("Initializing Logger")
    
    def error(self, message: str):
        print("Logging error: " + message)
        current_time = datetime.utcnow()
        f = open(Constants.LOG_FILE_NAME, "a")
        f.write (str(current_time) + " - " + message + "\n")
        f.close()
