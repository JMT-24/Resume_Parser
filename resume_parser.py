import sys
import asyncio
sys.path.append("scripts")

from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails, GetSents, GetEnts, GetTokenDetails
from file_processor import DOCtoText, PDFtoText, CreateTextFile


async def main():
    filename = "files/CV-Juan-Miguel-C.-Torres.docx"
    await DOCtoText(filename)
    docfile = f"texts/{filename[6:(len(filename)-5)]}_docx.txt"
    txt = await GetEnts(docfile)
    await CreateTextFile(txt, f"{docfile[6:(len(docfile)-4)]}_ents.txt")

    print("Main Program Done")



asyncio.run(main())