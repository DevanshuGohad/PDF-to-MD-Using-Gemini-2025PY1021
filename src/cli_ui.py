import os
import inquirer

def get_pdf_files():
    """Get all PDF files from current directory and sample pdfs directory."""
    pdf_files = []
    
    # Get PDFs from current directory
    for file in os.listdir('.'):
        if file.lower().endswith('.pdf'):
            pdf_files.append(file)
    
    # Get PDFs from sample pdfs directory
    sample_pdfs_dir = "sample_pdfs"
    if os.path.exists(sample_pdfs_dir):
        for file in os.listdir(sample_pdfs_dir):
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(sample_pdfs_dir, file))
    
    return pdf_files

def select_pdf_files():
    """Create an interactive CLI to select PDF files."""
    pdf_files = get_pdf_files()
    
    if not pdf_files:
        print("No PDF files found in current directory or 'sample pdfs' directory.")
        return []
    
    questions = [
        inquirer.Checkbox(
            'selected_files',
            message="Select PDF files to convert",
            choices=pdf_files,
        ),
    ]
    
    try:
        answers = inquirer.prompt(questions)
        return answers['selected_files'] if answers else []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
