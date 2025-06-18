from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Initialize the Gemini model
# Using 'gemini-2.5-flash-preview-05-20' model here
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')

def convert_text_to_markdown(text: str) -> str:
    """Convert content to markdown using Gemini."""
    prompt = (
        "Convert the following content from a PDF to clean, readable Markdown. "
        "Preserve headings, paragraphs, and convert tables if any. "
        "Where you see ![Image](path), include the image using Markdown syntax like "
        "![description](path). Use appropriate headers and lists.\n\n"
        f"{text}"
    )
    try:
        # Generate content using the Gemini model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Handle any errors that occur during the conversion
        print(f"Gemini conversion failed: {e}")
        return ""