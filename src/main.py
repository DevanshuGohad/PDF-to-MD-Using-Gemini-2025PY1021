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
        markdown = convert_text_to_markdown(pdf_text)
        if not markdown:
            print(f"Skipping {file_name} due to Gemini failure.")
            continue

        # Step 6: Write to .md file
        md_filename = os.path.splitext(os.path.basename(file_name))[0] + ".md"
        md_filepath = os.path.join(output_dir, md_filename)
        with open(md_filepath, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Saved: {md_filepath}")

if __name__ == '__main__':
    main()

        