from cli_ui import select_pdf_files

def main():
    selected_files = select_pdf_files()
    if selected_files:
        print(f"Selected files: {selected_files}")
    else:
        print("No files were selected.")

if __name__ == '__main__':
    main()

