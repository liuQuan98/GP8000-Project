from modelscope import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch
import os


class Dummy:
    # for debugging only
    def get_response(self, input_text, images, **kwargs):
        # Dummy response for demonstration purposes
        return f"Dummy response to: {input_text} and {type(images)}"
    

class ChatBot_Qwen:
    def __init__(self, model_name='qwen/Qwen-VL-Chat'):
        print("Loading model and tokenizer...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).eval()
        self.chat_history = []

    def _prepare_images(self, image_paths):
        images = []
        for path in image_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Image path not found: {path}")
            img = Image.open(path).convert('RGB')
            images.append(img)
        return images

    def get_response(self, text, images=None):
        """
        Parameters:
            text (str): The user's input query.
            images (list): List of image paths (str) or PIL Images.
        Returns:
            str: Response from Qwen-VL
        """
        # if images is not None and isinstance(images[0], str):
        #     images = self._prepare_images(images)

        messages = []
        if text:
            messages.append({"text": text})
        if images:
            for img in images:
                messages.append({"image": img})

        input = self.tokenizer.from_list_format(messages)

        response, _ = self.model.chat(self.tokenizer, input, history=None)
        return response

# Initialize the chatbot
chatbot = ChatBot_Qwen()

# # Initialize the dummy chatbot for debugging
# chatbot = Dummy()

def handle_chat(input_text, images=None):
    response = chatbot.get_response(input_text, images=images)
    return response

