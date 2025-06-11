from cli_ui import select_pdf_files

def main():
    # Get selected PDF files from user
    selected_files = select_pdf_files()
    
    # Show results
    if selected_files:
        print("Selected files:")
        for file in selected_files:
            print(f"- {file}")
    else:
        print("No files were selected.")

if __name__ == '__main__':
    main()

    