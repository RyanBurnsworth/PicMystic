from services.image_downloader import ImageDownloader
from services.image_generator import ImageGenerator
from services.image_generator import Image_Size
from services.face_detector import FaceDetector

def main():
    print("Welcome to PicMystic")
    image_generator = ImageGenerator()
    image_downloader = ImageDownloader()
    
    face_detector = FaceDetector()
    file_location = face_detector.start_face_detection()
    
    image_url = image_generator.create_image_variation(file_location, Image_Size.LARGE)
    if (image_url != ""):
        image_location = image_downloader.download_image(image_url)
        print(image_location)

if __name__ == "__main__":
    main()
