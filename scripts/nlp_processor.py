import asyncio
import spacy
# python -m spacy download en_core_web_md
nlp = spacy.load("en_core_web_md")

def DisplaySents(filename):
    with open (filename, "r") as f:
        text = f.read()
    doc = nlp(text)
    for sent in doc.sents:
        print(sent)

def DisplayEnts(filename):
    with open(filename, "r") as f:
        text = f.read()
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    
def DisplayTokenDetails(filename):
    with open(filename, "r") as f:
        text = f.read()
    doc = nlp(text)
    for sent in doc.sents:
        print("\n🔹 Sentence:", sent.text)
        print(f"{'Token':<15}{'POS':<10}{'Dependency':<15}{'Head'}") 
        print("=" * 50)  

        for token in sent:  
            print(f"{token.text:<15}{token.pos_:<10}{token.dep_:<15}{token.head}")

async def GetSents(filename):
    with open(filename, "r") as f:
        text = f.read()
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    txt = "\n".join(sentences)
    print("Sents generated")
    return txt

async def GetEnts(filename):
    with open(filename, "r") as f:
        text = f.read()
    doc = nlp(text)
    entities = [f"{ent.text} ({ent.label_})" for ent in doc.ents]
    txt = "\n".join(entities)
    print("Entity labeling are generated")
    return txt

async def GetTokenDetails(filename):
    with open(filename, "r") as f:
        text = f.read()
    doc = nlp(text)

    details = [] 

    for sent in doc.sents:
        details.append(f"\n🔹 Sentence: {sent.text}")
        details.append(f"{'Token':<15}{'POS':<10}{'Dependency':<15}{'Head'}")
        details.append("=" * 50)

        for token in sent:
            details.append(f"{token.text:<15}{token.pos_:<10}{token.dep_:<15}{token.head}")

    txt = "\n".join(details)
    print("Token Details generated")
    return txt
