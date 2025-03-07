import pdfplumber

def ReadPDF(filename):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            print(page.extract_text())

ReadPDF("../files/hybrid_setup_letter.pdf")