import spacy
import random
from spacy.training import Example
from spacy.util import minibatch
from sklearn.model_selection import train_test_split

nlp = spacy.blank("en")  # Start with a blank model for better training

# Add NER pipeline if not exists
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner", last=True)
else:
    ner = nlp.get_pipe("ner")

# Define entity labels
LABELS = ["CANDIDATE_NAME", "JOB_TITLE", "ADDRESS", "COURSE", "COMPANY", "SKILLS", "EDUCATION", "DATES", "EMAIL", "PHONE"]
for label in LABELS:
    ner.add_label(label)

print("Loading training data...")
doc_bin = spacy.tokens.DocBin().from_disk("../data/train_data.spacy")
examples = [Example(nlp.make_doc(doc.text), doc) for doc in doc_bin.get_docs(nlp.vocab)]

# Split data (90% training, 10% validation for faster training)
train_data, val_data = train_test_split(examples, test_size=0.1, random_state=42)

print("Training the model...")
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.begin_training()
    optimizer.learn_rate = 0.0002  # Lower learning rate for stability

    epochs = 50
    best_loss = float("inf")
    patience = 10 
    patience_counter = 0

    for epoch in range(epochs):
        print(f"🔄 Epoch {epoch + 1}/{epochs} - Training in progress...")  # Show progress
        random.shuffle(train_data)
        losses = {}
        batches = minibatch(train_data, size=4)  # Reduce batch size for faster training

        for i, batch in enumerate(batches):
            nlp.update(batch, losses=losses, drop=0.4, sgd=optimizer)
            if i % 10 == 0:  # Print progress every 10 batches
                print(f"🟢 Batch {i}/{len(train_data)//4} - Loss: {losses.get('ner', 0):.4f}")

        # Compute validation loss more efficiently
        val_metrics = nlp.evaluate(val_data)
        val_loss = val_metrics["ents_f"]  # Use precomputed metric
        print(f"✅ Epoch {epoch + 1} Completed - Train Loss: {losses.get('ner', 0):.4f} - Val Loss: {val_loss:.4f}")

        # Early stopping
        if val_loss < best_loss:
            best_loss = val_loss
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print("⛔ Early stopping triggered!")
                break

# Save trained model
nlp.to_disk("../models/resume_parser_model")
print("✅ Model training complete")