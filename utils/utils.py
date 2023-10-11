from datetime import datetime

class Utils:
    def __init__(self):
        self
    
    def getDateTimeAsString(self) -> str:
        now = datetime.now()
        return now.strftime("%m-%d-%Y-%H-%M-%S")