import sys
import asyncio
sys.path.append("scripts")

from nlp_processor import DisplaySents, DisplayEnts, DisplayTokenDetails, GetSents, GetEnts, GetTokenDetails
from file_processor import DOCtoText, PDFtoText, CreateTextFile


async def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    filename = sys.argv[1] 
    print(f"Processing file: {filename}")

    if (filename.endswith(".docx")):
        await DOCtoText(filename)
        docfile = f"texts/{filename[6:(len(filename)-5)]}_docx.txt"
        txt = await GetEnts(docfile)
        await CreateTextFile(txt, f"{docfile[6:(len(docfile)-4)]}_ents.txt")
    elif (filename.endswith(".pdf")):
        await PDFtoText(filename)
        docfile = f"texts/{filename[6:(len(filename)-4)]}_pdf.txt"
        txt = await GetEnts(docfile)
        await CreateTextFile(txt, f"{docfile[6:(len(docfile)-4)]}_ents.txt")

    print("Main Program Done")



asyncio.run(main())