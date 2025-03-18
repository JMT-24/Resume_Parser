import sys
sys.path.append("scripts")
import shutil

from file_processor import read_docs, read_pdf
from fileCrawler import crawl_folder
from spacyFilter import extract_skills


folder = "files/Resumes"
files = crawl_folder(folder)
skills = {"python", "sql", "figma", "mysql", "php"}
desitintaionFolder = "files/Filtered"

for file in files:
    text = read_pdf(file)
    found_skills = extract_skills(text, skills)
    if found_skills:
        # print(f"{file} has the skills: {found_skills}")
        shutil.copy(file, desitintaionFolder)

