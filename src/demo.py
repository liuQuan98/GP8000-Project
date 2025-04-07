import random
import numpy as np
from PIL import Image
import gradio as gr

from chatbot.qwen2_vl_integration import handle_chat
from chatbot.tesseract_integration import convert_pdf_and_img_to_text

def get_response(message, history):
    print("printing history", flush=True)
    for item in history:
        if type(item) == dict:
            print(item, flush=True)
            user_prompt = message.get("text")
            files = message.get("files")


    if type(message) == dict:
        user_prompt = message.get("text")
        files = message.get("files")

        pdf_file_path=None
        images = []
        for item in files:
            path = item.get("path")
            if path.endswith(".pdf"):
                pdf_file_path = path
            elif path.endswith(".png") or path.endswith(".jpg"):
                try:
                    images.append(np.array(Image.open(path)))
                except FileNotFoundError as e:
                    print(f"File {path} not found.", flush=True)
                    user_prompt += f"Notice: File {path} not found."
                    
    recognized_text = convert_pdf_and_img_to_text(pdf_file_path, images)

    # prompt engineering
    system_prompt = f'''
        You are a helpful financial assistant. I am going to show you some documents from scanned files and I
        need you to answer the user's questions based on the documents. First, please notice that the user input is as follows: 
        {user_prompt}
        Do not need to answer the question directly. Instead, by looking at the question, you need to
        judge the user's knowledge background based on the question, but not say it out.
        Then, you need to give a customized answer based on the user's knowledge background.
        E.g., you should avoid providing risky or potentially misleading choices to less knowledgeable users.
        You should also try to provide all the necessary information to help the user make a decision, like the pros and cons of each option.
        You should also provide some basic concepts and definitions of economics to the user if the user lacks economic knowledge.
        The documents are as follows: 
        {recognized_text}
        Please answer my questions based on the documents: 
        {user_prompt}
    '''
    
    return handle_chat(system_prompt, images=images)


demo = gr.ChatInterface(get_response, type="messages", autofocus=False, multimodal=True)

if __name__ == "__main__":
    demo.launch()