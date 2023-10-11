class Constants: 
    WELCOME_TEXT = "Welcome to PicMystic\n\n"
    CHOOSE_OPTIONS = "Choose one of the following options:\n\n"
    OPTION_ZERO = "    [0] Generate Image Variations Slideshow (uses webcam)\n"
    OPTION_ONE = "    [1] Generate User-Prompt Image Slideshow\n"
    OPTION_TWO = "    [2] Exit\n\n"

    PROMPT_REQUEST = "Enter the prompt: "
    
    MENU_ITEM_ZERO = "0"
    MENU_ITEM_ONE = "1"
    MENU_ITEM_TWO = "2"


    DATA = "data"
    URL = "url"
    
    LOG_FILE_NAME = "./picMysticError.log"

    IMAGE_SIZE_SMALL = "256x256"
    IMAGE_SIZE_MEDIUM = "512x512"
    IMAGE_SIZE_LARGE = "1024x1024"
    
    # for use with MQTT service
    MQTT_TOPIC = "/system/external/monitor"

    DEFAULT_IMAGE_DELAY = 10
    DEFAULT_NUMBER_OF_SLIDES = 5

    # for use in Prompt Generator
    ROLE = "role"
    SYSTEM = "system"
    USER = "user"
    CONTENT = "content"
    MODEL = "gpt-3.5-turbo-0613"
    DEFAULT_MAX_PROMPTS = 5
