import spacy

print("loading trained model")
nlp = spacy.load("../models/resume_parser_model")

print("Pipeline Components:", nlp.pipe_names)
print("Entity Labels:", nlp.get_pipe("ner").labels)  # Check entity labels

text = "Jane Doe is a Data Scientist at Microsoft."
doc = nlp(text)
print("Detected Entities:", [(ent.text, ent.label_) for ent in doc.ents])  # Check output

# test_texts = [
#     "Jane Doe is a Data Scientist at Microsoft.",
#     "She is skilled in Java and React.",
#     "Graduated from Harvard in 2020.",
#     "Contact: janedoe@email.com, +1 987 654 3210."
# ]

# for text in test_texts:
#     doc = nlp(text)
#     print(f"Text: {text}")
#     print("Entities: ", [(ent.text, ent.label_) for ent in doc.ents])
#     print()
