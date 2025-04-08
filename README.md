# GP8000: Gradio Chatbot Project

This project implements a chatbot interface using Gradio, integrating QWEN2-VL for chatbot functionality and utilizing Tesseract for converting PDF files into text. The application provides a user-friendly interface for interacting with the chatbot and processing PDF documents.

## Project Structure

```
gradio-chatbot-project
├── src
│   ├── demo.py                # Main entry point of the application
│   └── chatbot
│       ├── __init__.py       # Marks the chatbot directory as a package
│       ├── qwen2_vl_integration.py  # Integration logic for the QWEN2-VL chatbot
│       └── tesseract_integration.py  # Logic for converting PDF files into text
├── requirements.txt          # Lists dependencies required for the project
├── README.md                 # Documentation for the project
└── .gitignore                # Specifies files and directories to ignore by Git
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd gradio-chatbot-project
   ```

2. **Install dependencies**:

   Install Tesseract, and configure the executable file path in `src/chatbot/tesseract_integration.py`

3. **Create a virtual environment** (Conda recommended):
   ```bash
   conda env create -f reqrirements.yaml
   conda activate gp8000
   pip install modelscope[multi-modal] transformers_stream_generator
   pip install gradio==5.23.3 pytesseract pdf2image Pillow 
   ```

4. **Run the application**:
   ```bash
   python src/demo.py
   ```

## Usage Guidelines

- Upload PDF, JPEG or PNG files to extract text using Tesseract.
- Enter a prompt in the input box to interact with the QWEN2-VL chatbot.
- (Optional) Diagolue with the chatbot about your preferences and financial knowledge base can help a lot in assisting model decision.

## Dependencies

- Gradio
- Tesseract
- pdf2image
- pytesseract
- Pillow

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
