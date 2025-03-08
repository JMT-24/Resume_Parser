import sys
sys.path.append("scripts")

from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails, GetSents, GetEnts, GetTokenDetails
from file_processor import DOCtoText, PDFtoText, CreateTextFile


filename = "files/CV-Juan-Miguel-C.-Torres.docx"

# DOCtoText(filename)

docfile = f"texts/{filename[6:(len(filename)-5)]}_docx.txt"

txt = GetEnts(docfile)
CreateTextFile(txt, f"{docfile[6:(len(docfile)-4)]}_ents.txt")
