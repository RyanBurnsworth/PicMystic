import openai
from enum import Enum
from utils.constants import Constants
from utils.logger import Logger

openai.api_key = ""     # place OpenAI API key here

class Image_Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class ImageGenerator:
    _logger: Logger

    def __init__(self):
        self._logger = Logger()

    """
        Create an image from a user inputted prompt

        @param prompt - the prompt from the user
        @image_size - the output size of the image (SMALL, MEDIUM, LARGE)
        @returns - the url to the image generated
    """
    def create_image_from_prompt(self, prompt: str, image_size: Image_Size) -> str:
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size=self._get_image_size(image_size)
            )

            image_url = response[Constants.DATA][0][Constants.URL]
            return image_url
        except Exception as err:
            print("Error creating image from prompt %s with size %s. Error: " + err % (prompt, image_size))
            self._logger.error("Error creating image from prompt %s with size %s. Error: " + err % (prompt, image_size))
            return ""

    """
        Create a variation of an inputted image

        @param image_location - the location of the image to create a variation of
        @param image_size - the output size of the image (SMALL, MEDIUM, LARGE)
        @returns - the url to the generated image variant
    """
    def create_image_variation(self, image_location: str, image_size: Image_Size) -> str:
        try:
            response = openai.Image.create_variation(
                image=open(image_location, "rb"),
                n=1,
                size=self._get_image_size(image_size)
            )

            image_url = response[Constants.DATA][0][Constants.URL]
            return image_url
        except Exception as err:
            print("Error creating image variation from image %s with size %s. Error: " + err % (image_location, image_size))
            self._logger.error("Error creating image variation from image %s with size %s. Error: " + err % (image_location, image_size))
            return ""

    """
        Get the image size by Image_Size enum
        @param image_size - the enum of the size chosen for image output
        @returns - the image size as a string compatiable with the OpenAI api input
    """
    def _get_image_size(self, image_size: Image_Size) -> str:
        if (image_size is Image_Size.SMALL):
            return "256x256"
        elif (image_size is Image_Size.MEDIUM):
            return "512x512"
        elif (image_size is Image_Size.LARGE):
            return "1024x1024"

        return ""
