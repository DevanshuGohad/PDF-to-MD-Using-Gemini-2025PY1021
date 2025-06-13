import fitz  # PyMuPDF
import os
from PIL import Image

def extract_text_images_tables(pdf_path: str, output_image_dir: str) -> str:
    """Extracts text, images, and attempts to preserve tables from a PDF."""
    
    # Open the PDF file
    doc = fitz.open(pdf_path)
    full_text = ""

    # Ensure output directory exists
    os.makedirs(output_image_dir, exist_ok=True)
    # Create a subdirectory for images
    images_dir = os.path.join(output_image_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # Iterate through each page in the PDF
    for i, page in enumerate(doc):
        # Extract text from the page
        text = page.get_text()
        # Add page heading and text to the Markdown content
        full_text += f"\n\n## Page {i + 1}\n\n{text.strip()}\n"

        # Extract all images from the page
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0] # Reference to the image in the PDF
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"] # Image data in bytes
            image_ext = base_image["ext"]# Image file extension (e.g., 'png', 'jpeg')
            # Create a unique filename for each image
            image_filename = f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page{i + 1}_img{img_index + 1}.{image_ext}"
            image_filepath = os.path.join(images_dir, image_filename)

            # Save the image file to the images directory
            with open(image_filepath, "wb") as img_file:
                img_file.write(image_bytes)

            # Add a Markdown image reference (relative path) to the content
            full_text += f"\n![Image](images/{image_filename})\n"

    # Close the PDF file
    doc.close()
    # Return the complete Markdown content
    return full_text.strip()
