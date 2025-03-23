import pdfplumber
from docx import Document

def read_docs(filename):
    doc = Document(filename)
    paragraphs = [paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()]
    text = "\n".join(paragraphs)
    return text

def read_pdf(filename):
    """Extracts text from a PDF file."""
    with pdfplumber.open(filename) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text