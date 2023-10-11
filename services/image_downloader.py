import os
import wget
from utils.logger import Logger

class ImageDownloader:
    _logger: Logger

    def __init__(self):
        self._logger = Logger()

    """
        Download an image from a url provided

        @param image_url - the url of the image's location
        @returns the file location of the downloaded image
    """
    def download_image(self, image_url: str) -> str:
        current_directory = os.getcwd() + "\\images\\"
        
        try:
            filename =  wget.download(image_url)
        except Exception as err:
            print("Error downloading image: %s" % image_url)
            self._logger.error("Error download image: %s" % image_url)
            self._logger.error(str(err))
            return ""

        return current_directory + filename
