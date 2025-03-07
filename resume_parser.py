import sys
sys.path.append("scripts")

from docx_processor import ReadDocument, ConvertDocument, CreateDocument
from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails
from nlp_processor import GetSents, GetEnts, GetTokenDetails



#ReadDocument("files/hybrid_setup_letter.docx")

with open ("texts/hybrid_setup_letter.txt", "r") as f:
    text = f.read()

# DisplayTokenDetails(text)

txt = GetTokenDetails(text)
CreateDocument(txt, "text.txt")
