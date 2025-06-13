import os
import inquirer
from typing import List

def get_pdf_files() -> List[str]:
    """Get all PDF files from current directory and sample_pdfs directory."""

    sample_pdfs_dir = "sample_pdfs"
    return ([f for f in os.listdir('.') if f.lower().endswith('.pdf')] +
        [os.path.join(sample_pdfs_dir, f) for f in os.listdir(sample_pdfs_dir)
         if f.lower().endswith('.pdf')] if os.path.exists(sample_pdfs_dir) else [])


def select_pdf_files() -> List[str]:
    """Create an interactive CLI to select PDF files."""
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return []
    
    display_to_path = {os.path.basename(f): f for f in pdf_files}
    display_names = list(display_to_path.keys())

    questions = [
        inquirer.Checkbox(
            'selected_files',
            message="Select PDF files to convert",
            choices=display_names,
        ),
    ]

    try:
        answers = inquirer.prompt(questions)
        # Map selected display names back to full paths
        return [display_to_path[name] for name in answers['selected_files']] if answers else []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
