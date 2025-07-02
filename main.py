import os
import json
from PyPDF2 import PdfReader, PdfWriter

def read_config(config_path):
    with open(config_path, 'r') as config_file:
        config = json.load(config_file)
    return config

def split_pdf(input_path, output_path, max_pages_per_file):
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    for i in range(0, total_pages, max_pages_per_file):
        writer = PdfWriter()
        output_filename = f"{os.path.splitext(os.path.basename(input_path))[0]}_part_{i // max_pages_per_file + 1}.pdf"
        
        for page_num in range(i, min(i + max_pages_per_file, total_pages)):
            writer.add_page(reader.pages[page_num])
        
        with open(os.path.join(output_path, output_filename), 'wb') as output_pdf:
            writer.write(output_pdf)
        print(f"Created: {output_filename}")

def main():
    config_path = 'config.json'
    config = read_config(config_path)
    
    input_path = config.get('input_path')
    output_path = config.get('output_path')
    max_pages_per_file = config.get('max_pages_per_file', 10)  # Default to 10 pages if not specified
    
    if not input_path:
        print("Input path is missing in the configuration file.")
        return
    
    if not os.path.exists(input_path):
        print(f"The specified input path does not exist: {input_path}")
        return
    
    split_pdf(input_path, output_path,max_pages_per_file)

if __name__ == "__main__":
    main()



