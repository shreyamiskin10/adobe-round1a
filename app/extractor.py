import fitz  # PyMuPDF
import json
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def write_json_output(text, filename, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{filename}.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({"filename": filename, "text": text}, f, indent=4)