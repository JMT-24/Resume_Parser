import json
import spacy
from spacy.tokens import DocBin

nlp = spacy.blank("en")

# Load training data
with open("../data/train_data.json", "r", encoding="utf-8") as f:
    TRAIN_DATA = json.load(f)

doc_bin = DocBin()
missing_entity_count = 0  # Track failed entity matches
overlap_count = 0  # Track overlaps removed

# Define common resume section headers to ignore
HEADERS = {"EDUCATIONAL BACKGROUND", "TRAININGS AND SEMINARS ATTENDED", "WORK EXPERIENCE", "PERSONAL INFORMATION"}

# Define keywords that should always be classified under specific labels
FORCE_EDUCATION = {"University", "College", "Elementary School", "High School"}
FORCE_ADDRESS = {"Street", "Avenue", "Highway", "Subdivision", "Village", "City"}
FORCE_PHONE_PREFIXES = {"+63", "+91", "+44", "+1", "+49"}  # Common country codes

def remove_overlaps(entities):
    """Removes overlapping entities by prioritizing JOB_TITLE > EMAIL/PHONE > SKILLS > COMPANY > EDUCATION > CANDIDATE_NAME."""
    global overlap_count
    priority = {
        "JOB_TITLE": 1, "EMAIL": 2, "PHONE": 2, "SKILLS": 3, "COMPANY": 4, "EDUCATION": 5, "CANDIDATE_NAME": 6,
        "DATES": 7, "ADDRESS": 8, "COURSE": 9
    }
    
    entities = sorted(entities, key=lambda x: (x[0], priority.get(x[2], 99)))  # Sort by priority
    cleaned = []
    last_end = -1

    for start, end, label in entities:
        if start >= last_end:  # No overlap
            cleaned.append([start, end, label])
            last_end = end  # Update last end position
        else:
            overlap_count += 1
            print(f"⚠️ Removing overlapping entity: '{start}-{end}' ({label})")
    
    return cleaned

def snap_to_tokens(text, entities, nlp):
    """Adjusts entity spans to match token boundaries more effectively."""
    doc = nlp.make_doc(text)
    snapped_entities = []
    
    for start, end, label in entities:
        entity_text = text[start:end].strip()
        
        # Ignore headers (all caps section titles)
        if entity_text in HEADERS:
            print(f"⚠️ Ignoring section header: '{entity_text}'")
            continue

        # Force universities, colleges, and schools to be EDUCATION
        if entity_text in FORCE_EDUCATION:
            label = "EDUCATION"
        
        # Force locations like streets, highways, etc., to be ADDRESS
        if any(keyword in entity_text for keyword in FORCE_ADDRESS):
            label = "ADDRESS"

        # Ensure phone numbers with country codes are correctly labeled
        if any(entity_text.startswith(prefix) for prefix in FORCE_PHONE_PREFIXES):
            label = "PHONE"

        span = doc.char_span(start, end, label=label, alignment_mode="expand")  # Use "expand" mode
        if span:
            snapped_entities.append([span.start_char, span.end_char, label])
        else:
            print(f"⚠️ Invalid entity span: '{entity_text}' ({label}) in: {text} (Adjusting manually)")
            
            # Try a fallback method (use nearest token)
            closest_token_start, closest_token_end = None, None
            for token in doc:
                if start >= token.idx and end <= token.idx + len(token.text):
                    closest_token_start, closest_token_end = token.idx, token.idx + len(token.text)
                    break
            if closest_token_start is not None:
                snapped_entities.append([closest_token_start, closest_token_end, label])
            else:
                print(f"❌ Could not align entity '{entity_text}' ({label})")
    
    return snapped_entities

for item in TRAIN_DATA:
    text = item["text"]
    entities = item["entities"]

    # Step 1: Remove overlapping spans with improved priority logic
    entities = remove_overlaps(entities)

    # Step 2: Snap to valid token boundaries & force correct labels
    entities = snap_to_tokens(text, entities, nlp)

    doc = nlp.make_doc(text)
    ents = []

    for start, end, label in entities:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span:
            ents.append(span)
        else:
            missing_entity_count += 1
            print(f"⚠️ Warning: Entity '{text[start:end]}' ({label}) could not be created in: {text}")

    # Assign entities to doc and add to DocBin
    doc.ents = ents
    doc_bin.add(doc)

# Save to disk
doc_bin.to_disk("../data/train_data.spacy")

print(f"✅ Training data saved in spaCy format ({len(TRAIN_DATA)} documents).")
if missing_entity_count > 0:
    print(f"⚠️ {missing_entity_count} entity spans failed due to tokenization issues.")
if overlap_count > 0:
    print(f"⚠️ {overlap_count} overlapping entities were removed.")