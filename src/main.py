import os
from cli_ui import select_pdf_files
from utils import extract_text_images_tables
from gemini import convert_text_to_markdown

def main():
    output_dir = "converted-md"

    # Step 1: Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Step 2: Let user select PDFs  
    selected_files = select_pdf_files()
    if not selected_files:
        print("No files were selected.")
        return

    # Step 3: Process each file
    for file_name in selected_files:
        print(f"Processing: {file_name, output_dir}")
        
        # Step 4: Extract text
        pdf_text = extract_text_images_tables(file_name, output_dir)
        if not pdf_text:
            print(f"Skipping {file_name} due to empty or unreadable content.")
            continue

        # Step 5: Convert to markdown

        # Step 6: Write to .md file

if __name__ == '__main__':
    main()

        