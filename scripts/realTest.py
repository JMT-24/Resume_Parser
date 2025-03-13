import spacy

# Load the trained model
print("Loading trained model...")
nlp = spacy.load("../models/resume_parser_model")

# Read the resume file as a whole document
file_path = "../texts/CV_Programmer_docx.txt"
with open(file_path, "r", encoding="utf-8") as file:
    test_text = file.read().strip()  # Read entire content as a single string

# Process the full resume text
doc = nlp(test_text)
print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
