class Constants: 
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
