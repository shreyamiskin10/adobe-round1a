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