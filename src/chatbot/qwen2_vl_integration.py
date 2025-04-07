# from qwen2 import QWEN2  # Assuming QWEN2 is a library for the chatbot

class Dummy:
    def get_response(self, input_text, images, **kwargs):
        # Dummy response for demonstration purposes
        return f"Dummy response to: {input_text} and {type(images)}"

# Initialize the QWEN2-VL chatbot
# chatbot = QWEN2()
chatbot = Dummy()


def handle_chat(input_text, images=None):
    response = chatbot.get_response(input_text, images=images)
    return response