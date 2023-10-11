from datetime import datetime

class Utils:
    def __init__(self):
        self
    
    def get_date_time_as_string(self) -> str:
        now = datetime.now()
        return now.strftime("%m-%d-%Y-%H-%M-%S")

    def convert_dict_to_list(self, input: dict) -> list:
        output = []

        for value in input.values():
            output.append(value)

        return output