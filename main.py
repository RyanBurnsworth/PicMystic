from services.image_downloader import ImageDownloader
from services.image_generator import ImageGenerator
from services.image_generator import Image_Size

def main():
    print("Welcome to PicMystic")
    image_generator = ImageGenerator()
    image_downloader = ImageDownloader()

    image_url = image_generator.create_image_from_prompt("A fat yellow cat smoking a cigar on the porch in the country", Image_Size.MEDIUM)

    if (image_url != ""):
        image_location = image_downloader.download_image(image_url)
        print(image_location)

if __name__ == "__main__":
    main()
