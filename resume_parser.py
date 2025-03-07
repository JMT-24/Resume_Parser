import sys
sys.path.append("scripts")

from docx_processor import ReadDocument, ConvertDocument, CreateTextFile ,CreateDocument
from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails
from nlp_processor import GetSents, GetEnts, GetTokenDetails
from pdf_processor import ReadPDF, ConvertPDF


# file = "files/hybrid_setup_letter.docx"
# ReadDocument(file)

filename = "texts/hybrid_setup_letter_pdf.txt"

# DisplayTokenDetails(filename)

txt = GetSents(filename)
CreateTextFile(txt, f"{filename[6:(len(filename)-4)]}_sents.txt")

# filename = "files/hybrid_setup_letter.docx"
# ReadPDF(filename)
# ConvertPDF(filename)
# ConvertDocument(filename)
