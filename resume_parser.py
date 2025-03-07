import sys
sys.path.append("scripts")

from docx_processor import ReadDocument, ConvertDocument, CreateTextFile ,CreateDocument
from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails
from nlp_processor import GetSents, GetEnts, GetTokenDetails



#ReadDocument("files/hybrid_setup_letter.docx")

with open ("texts/hybrid_setup_letter.txt", "r") as f:
    text = f.read()

# DisplayTokenDetails(text)

# txt = GetTokenDetails(text)

# txt = GetEnts(text)

txt = GetSents(text)
CreateTextFile(txt, "Ents.txt")
