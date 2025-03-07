import pdfplumber

def ReadPDF(filename):
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            print(page.extract_text())

def ConvertPDF(filename):
    with pdfplumber.open(filename) as pdf:
        sentences = [page.extract_text() for page in pdf.pages]
        texts = "\n".join(sentences)

        file = filename[6:(len(filename)-4)]
        with open(f"texts/{file}_pdf.txt", "w", encoding="utf-8") as f:
            f.write(texts)