import os
import openai
import json
from utils.logger import Logger
from utils.constants import Constants
from utils.utils import Utils

openai.api_key = os.environ['OPEN_AI_KEY']

class PromptGenerator:
    _logger: Logger
    _utils: Utils

    def __init__(self):
        self._logger = Logger()
        self._utils = Utils()

    """
        Generate a list of prompts from an input prompt. 

        @param input_prompt - the prompt to generate variations of
        @param max_prompts - the maximum number of prompts to return
        @returns a list of prompt variations
    """
    def generate_prompt_list_from_input(self, input_prompt: str, max_prompts = Constants.DEFAULT_MAX_PROMPTS) -> list:
        output_prompts = ""

        system_message = "For every user input give back " + str(max_prompts) + " variations of that prompt which can be used for generating images with DALL-E. Do not provide an explanation and only provide the list in a JSON format. For example, { \"variation_1\": \"This is variation one\", \"variation_2\", \"This is variation 2\", ... }"
        try :
            print("Generating %d prompt variations from input: %s " % (max_prompts, input_prompt))

            chat_completion = openai.ChatCompletion.create(
                temperature = 0.6,
                model = Constants.MODEL, 
                messages = [{Constants.ROLE: Constants.SYSTEM, Constants.CONTENT: system_message}, { Constants.ROLE: Constants.USER, Constants.CONTENT: input_prompt }])
            output_prompts = chat_completion.choices[0].message.content
        except Exception as err:
            self._logger("Error retrieving chat completion from OpenAI for input prompt %s: " % input_prompt)
            self._logger.error(str(err))

            print("PromptGenerator Error: Failed to retrieve chat completion: " + err)
        
        variations_json = json.loads(output_prompts)
        variations_list = self._utils.convert_dict_to_list(variations_json)
        
        return variations_list
