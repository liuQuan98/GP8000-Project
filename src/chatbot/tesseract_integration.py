from pdf2image import convert_from_path
from pytesseract import image_to_string
import pytesseract
import os

# Set the path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def convert_pdf_and_img_to_text(pdf_file, images=[]):
    if pdf_file is not None and not os.path.exists(pdf_file):
        return f"File {pdf_file} not found."
    
    if pdf_file is not None:
        images.append(convert_from_path(pdf_file, poppler_path=r"C:\poppler\Library\bin"))
    final_text = ""
    
    for img in images:
        final_text += image_to_string(img)
    
    return final_text

# def handle_pdf_upload(pdf_file):
#     text = convert_pdf_to_text(pdf_file)
#     return text

