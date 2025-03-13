import json
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")

with open ("../data/train_data.json", "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

# convert data into spacy format
doc_bin = DocBin()
for item in TRAIN_DATA:
    text = item["text"]
    entities = item["entities"]

    doc = nlp.make_doc(text)
    ents =[]
    for start, end, label in entities:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span:
            ents.append(span)
    
    doc.ents = ents
    doc_bin.add(doc)

doc_bin.to_disk("../data/train_data.spacy")
print("Training data is saved as spacy format")