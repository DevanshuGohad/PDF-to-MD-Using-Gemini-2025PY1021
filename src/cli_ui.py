import os
import inquirer
from typing import List, Dict

def get_pdf_files() -> Dict[str, List[str]]:
    """Get all PDF files from current directory and sample pdfs directory."""
    pdf_files = {
        "Current Directory": [],
        "Sample PDFs": []
    }
    
    current_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]
    pdf_files["Current Directory"] = current_files
    
    # Get PDFs from sample pdfs directory
    sample_pdfs_dir = "sample_pdfs"
    if os.path.exists(sample_pdfs_dir):
        sample_files = [f for f in os.listdir(sample_pdfs_dir) if f.lower().endswith('.pdf')]
        pdf_files["Sample PDFs"] = sample_files
    
    return pdf_files

def select_pdf_files() -> List[str]:
    """Create an interactive CLI to select PDF files."""
    pdf_files = get_pdf_files()
    if not any(pdf_files.values()):
        print("No PDF files found in current directory or 'sample pdfs' directory.")
        return []
    
    choices = []
    for directory, files in pdf_files.items():
        if files:
            choices.append(f"--- {directory} ---")
            if directory == "Current Directory":
                choices.extend([f for f in files])
            else:
                choices.extend([os.path.join(directory, f) for f in files])
    
    questions = [
        inquirer.Checkbox(
            'selected_files',
            message="Select PDF files to convert",
            choices=choices,
        ),
    ]
    
    try:
        answers = inquirer.prompt(questions)
        selected = answers['selected_files'] if answers else []
        return [f for f in selected if not f.startswith('---')]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
