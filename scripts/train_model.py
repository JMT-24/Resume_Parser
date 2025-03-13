import spacy
import random
from spacy.training import Example
from spacy.util import minibatch

nlp = spacy.load("en_core_web_md")

if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

LABELS = ["CANDIDATE_NAME", "JOB_TITLE", 
          "COMPANY", "SKILLS", "EDUCATION", "DATES", "EMAIL", "PHONE"]

for label in LABELS:
    ner.add_label(label)

print("Loading trainig data")
doc_bin = spacy.tokens.DocBin().from_disk("../data/train_data.spacy")
examples = []
for doc in doc_bin.get_docs(nlp.vocab):
    example = Example(doc, doc)  # Corrected entity annotation
    examples.append(example)



print(" train the model")
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.resume_training()

    epochs = 100

    for epoch in range(epochs):
        random.shuffle(examples)
        losses = {}

        # use minibatch to break data into smaller sets
        batches = minibatch(examples, size=8)
        for batch in batches:
            nlp.update(batch, losses=losses, drop=0.4) # drop means dropout that prevents overfitting

        print(f"Epoch: {epoch + 1} / {epochs} - Loss: {losses}")


nlp.to_disk("../models/resume_parser_model")
print("Model training complete")