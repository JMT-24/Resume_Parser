import spacy
from spacy.matcher import PhraseMatcher
from rapidfuzz import process

nlp = spacy.load("en_core_web_md")


def fuzzy_match(skill, skill_list, threshold=60):
    """Finds the closest skill match using fuzzy matching"""
    match = process.extractOne(skill, skill_list)
    if match:
        best_match, score = match[0], match[1]
        return best_match if score >= threshold else skill
    return skill

def extract_skills(text, skill_list):
    """Uses spacy NLP and fuzzy matching to detect skills from text"""
    doc = nlp(text.lower())
    matcher = PhraseMatcher(nlp.vocab)

    # Convert skills to spacy patterns
    patterns = [nlp(skill.lower()) for skill in skill_list]
    matcher.add("SKILL", patterns)  
    found_skills = set()
    matches = matcher(doc)

    for match_id, start, end in matches:
        matched_skill = doc[start:end].text # the skill
        normalized_skill = fuzzy_match(matched_skill, skill_list) # apply fuzzy matching
        found_skills.add(normalized_skill)

    return found_skills


