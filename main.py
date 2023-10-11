from services.image_downloader import ImageDownloader
from services.image_generator import ImageGenerator
from services.image_generator import Image_Size
from services.face_detector import FaceDetector
from services.media_player import MediaPlayer
from utils.constants import Constants

image_generator: ImageGenerator
image_downloader: ImageDownloader
face_detector: FaceDetector
media_player: MediaPlayer

"""
    Show a slideshow of AI generated variations of you. Once the face detector detects a face it will generate a variation image, download the image and display it.
    @param number_of_slides - the number of image variations (slides) to show
"""
def show_image_variation_slideshow(number_of_slides = Constants.DEFAULT_NUMBER_OF_SLIDES):    
    slide_counter = 0
    
    while(slide_counter < number_of_slides):
        file_location = face_detector.start_face_detection()
        
        image_url = image_generator.create_image_variation(file_location, Image_Size.LARGE)
        if (image_url != ""):
            slide_counter = slide_counter + 1
            image_location = image_downloader.download_image(image_url)
            media_player.display_image(image_location)

def main():
    global image_downloader, image_generator, face_detector, media_player
    print("Welcome to PicMystic")

    image_generator = ImageGenerator()
    image_downloader = ImageDownloader()
    face_detector = FaceDetector()
    media_player = MediaPlayer()

    show_image_variation_slideshow()

if __name__ == "__main__":
    main()
