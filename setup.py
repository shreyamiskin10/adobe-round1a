import os

base_dir = r"D:\Documents\adobe_hackathon_pdf_ai"

folders = [
    "app",
    "input",
    "output"
]

files_content = {
    "app/extractor.py": '''
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
''',

    "app/main.py": '''
import os
from extractor import extract_text_from_pdf, write_json_output

input_dir = "../input"
output_dir = "../output"

for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(input_dir, filename)
        text = extract_text_from_pdf(pdf_path)
        write_json_output(text, filename.replace('.pdf', ''), output_dir)

print("✅ All PDFs processed and JSON saved.")
''',

    "requirements.txt": "PyMuPDF==1.23.9",

    "README.md": '''
# Adobe Hackathon 2025 - PDF AI App (Round 1A)

## Objective
Extract text from multiple PDFs and convert them to structured JSON.

## Setup
- Place your PDFs in `input/`
- Run `main.py` to get output JSONs in `output/`
'''
}

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

# Create files with content
for rel_path, content in files_content.items():
    full_path = os.path.join(base_dir, rel_path)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip())

print("✅ Project structure and files created successfully!")
