import pdfplumber
import re

def read_pdf(filename):
    """Extracts text from a PDF file, handling formatting issues."""
    with pdfplumber.open(filename) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    print("PDF has been read")
    
    # Normalize text by removing special characters & extra spaces
    text = re.sub(r"[\s]+", " ", text)  # Replace newlines/tabs with spaces
    return text.lower()  # Convert to lowercase for case-insensitive matching

def find_skills(text, filter_words):
    """Finds keywords in the resume, handling different resume structures."""
    text = text.replace(" ", "")  # Remove spaces to handle cases like "SKILLSANDABILITIES"
    
    found_skills = set()
    
    for word in filter_words:
        word_nospace = word.replace(" ", "").lower()  # Normalize keyword (e.g., "soft skills" -> "softskills")
        if word_nospace in text:
            found_skills.add(word)
    
    for skill in found_skills:
        print(f"{skill} is found")
