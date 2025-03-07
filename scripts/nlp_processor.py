import spacy

nlp = spacy.load("en_core_web_md")

def DisplaySents(text):
    doc = nlp(text)
    for sent in doc.sents:
        print(sent)

def DisplayEnts(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
def DisplayTokenDetails(text):
    doc = nlp(text)
    for sent in doc.sents:
        print("\n🔹 Sentence:", sent.text)
        print(f"{'Token':<15}{'POS':<10}{'Dependency':<15}{'Head'}") 
        print("=" * 50)  

        for token in sent:  
            print(f"{token.text:<15}{token.pos_:<10}{token.dep_:<15}{token.head}")

def GetSents(text):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    txt = "\n".join(sentences)
    return txt

def GetEnts(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    txt = "\n".join(entities)
    return txt

def GetTokenDetails(text):
    doc = nlp(text)

    details = [] 

    for sent in doc.sents:
        details.append(f"\n🔹 Sentence: {sent.text}")
        details.append(f"{'Token':<15}{'POS':<10}{'Dependency':<15}{'Head'}")
        details.append("=" * 50)

        for token in sent:
            details.append(f"{token.text:<15}{token.pos_:<10}{token.dep_:<15}{token.head}")

    txt = "\n".join(details)
    return txt
