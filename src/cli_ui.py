import os
import inquirer
from typing import List

# Get all PDF files from the current directory and the 'sample_pdfs' directory
def get_pdf_files() -> List[str]:
    """
    Get all PDF files from current directory and sample_pdfs directory.
    Returns a list of file paths (relative to the current directory).
    """

    sample_pdfs_dir = "sample_pdfs"
    #List PDFs in current directory and, if it exists, in sample_pdfs directory (with relative path)"""
    return ([f for f in os.listdir('.') if f.lower().endswith('.pdf')] +
        [os.path.join(sample_pdfs_dir, f) for f in os.listdir(sample_pdfs_dir)
         if f.lower().endswith('.pdf')] if os.path.exists(sample_pdfs_dir) else [])


def select_pdf_files() -> List[str]:
    #Create an interactive CLI to select PDF files. Returns a list of selected file paths.

    pdf_files = get_pdf_files()
    
    if not pdf_files:
        #Inform the user if no PDFs are found
        print("No PDF files found in the current directory.")
        return []
    
    # Map display names (just the filename) to their full paths
    display_to_path = {os.path.basename(f): f for f in pdf_files}
    display_names = list(display_to_path.keys()) # List of filenames for display

    # Define the CLI question for selecting files
    questions = [
        inquirer.Checkbox(
            'selected_files',
            message="Select PDF files to convert",
            choices=display_names,
        ),
    ]

    try:
        # Prompt the user to select files
        answers = inquirer.prompt(questions)
        # Map selected display names back to full paths
        return [display_to_path[name] for name in answers['selected_files']] if answers else []
    except Exception as e:
        # Handle any errors that occur during selection
        print(f"An error occurred: {e}")
        return []
