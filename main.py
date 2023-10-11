from services.image_downloader import ImageDownloader
from services.prompt_generator import PromptGenerator
from services.image_generator import ImageGenerator
from services.image_generator import Image_Size
from services.face_detector import FaceDetector
from services.media_player import MediaPlayer
from utils.constants import Constants

prompt_generator: PromptGenerator
image_downloader: ImageDownloader
image_generator: ImageGenerator
face_detector: FaceDetector
media_player: MediaPlayer

"""
    Using the webcam, show a slideshow of AI generated variations of you. 
    Once the face detector detects a face it will generate a variation image, download the image and display it.

    @param number_of_slides - the number of image variations (slides) to show
"""
def show_image_variation_slideshow(number_of_slides = Constants.DEFAULT_NUMBER_OF_SLIDES):    
    slide_counter = 0

    while(slide_counter < number_of_slides):
        file_location = face_detector.get_facial_image()
        
        image_url = image_generator.create_image_variation(file_location, Image_Size.LARGE)
        if (image_url != ""):
            slide_counter = slide_counter + 1
            image_location = image_downloader.download_image(image_url)
            media_player.display_image(image_location)

"""
    Show a slideshow of AI generated images based on a user prompt. 
    The user prompt is fed in to ChatGPT to generate a number of variations of the prompt which are used for the slideshow
    
    @param input_prompt - the seed prompt
"""
def show_image_generation_slideshow(input_prompt: str):
    global prompt_generator

    slide_counter = 0
    variation_prompt_list = prompt_generator.generate_prompt_list_from_input(input_prompt)

    while(slide_counter < len(variation_prompt_list)):
        image_url = image_generator.create_image_from_prompt(variation_prompt_list[slide_counter], Image_Size.LARGE)
        if (image_url != ""):
            slide_counter = slide_counter + 1
            image_location = image_downloader.download_image(image_url)
            media_player.display_image(image_location)

def main():
    global prompt_generator, image_downloader, image_generator, face_detector, media_player
    print("Welcome to PicMystic")

    prompt_generator = PromptGenerator()
    image_downloader = ImageDownloader()
    image_generator = ImageGenerator()
    face_detector = FaceDetector()
    media_player = MediaPlayer()

    # show_image_variation_slideshow()

    show_image_generation_slideshow("A warm Autumn afternoon in Indiana")

if __name__ == "__main__":
    main()
