from datetime import datetime
from utils.constants import Constants

class Logger:
    def __init__(self):
        self

    def error(self, message: str):
        print("Logging error: " + message)
        current_time = datetime.utcnow()
        f = open(Constants.LOG_FILE_NAME, "a")
        f.write (str(current_time) + " - " + message + "\n")
        f.close()
