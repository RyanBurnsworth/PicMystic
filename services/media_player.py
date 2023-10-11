import vlc
import time
from utils.constants import Constants

class MediaPlayer:
    def __init__(self):
        self
    
    """
        Display an image fullscreen for a period of a given time delay
        
        @param image_location - the location of the image
        @param image_delay - the length to display the image
    """
    def display_image(self, image_location: str, image_delay = Constants.DEFAULT_IMAGE_DELAY):
        print("Displaying image: %s" % image_location)

        media_player = vlc.MediaPlayer()
        media_player.toggle_fullscreen()

        media = vlc.Media(image_location)
        media_player.set_media(media)
        media_player.play()

        time.sleep(image_delay)
