import json
import random
import re
from faker import Faker
import phonenumbers

fake = Faker()

def find_entity(text, word):
    """Finds the start and end position of an entity in text, ensuring accurate spans."""
    match = re.search(rf"\b{re.escape(word)}\b", text)
    return (match.start(), match.end()) if match else None

def remove_overlapping_entities(entities):
    """Removes overlapping entities based on character spans."""
    sorted_entities = sorted(entities, key=lambda x: x[0])  # Sort by start index
    non_overlapping = []

    last_end = -1
    for start, end, label in sorted_entities:
        if start >= last_end:  # Ensure no overlap
            non_overlapping.append((start, end, label))
            last_end = end

    return non_overlapping

train_data = []

for _ in range(500):
    name = fake.name()
    email = fake.email()

    # Generate a valid phone number
    phone_raw = fake.phone_number()
    try:
        parsed_phone = phonenumbers.parse(phone_raw, "US")
        phone = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except phonenumbers.NumberParseException:
        phone = "+1 123-456-7890"  # Fallback phone number in case of parsing error

    job = fake.job()
    company = fake.company()
    skill = random.choice(["Python", "Django", "React", "Machine Learning", "AWS", "Kubernetes", "SQL"])
    university = fake.company()  # Using company names as universities for realistic results
    graduation_year = str(random.randint(1990, 2025))

    experience = f"{random.randint(1, 15)} years of experience in {skill}"
    certification = f"Certified in {fake.catch_phrase()}"

    text_templates = [
        f"{name} is a {job} at {company}. Skilled in {skill}. {experience}. {certification}. Graduated from {university} in {graduation_year}. Contact: {email}, {phone}.",
        f"{name}, a {job} at {company}, specializes in {skill}. With {experience}, they hold {certification}. They studied at {university}, graduating in {graduation_year}. Reach out via {email} or {phone}.",
        f"Meet {name}, currently working as a {job} at {company}. Expertise: {skill}. {experience}. {certification}. Alumni of {university}, Class of {graduation_year}. Contact Info: {email}, {phone}."
    ]

    text = random.choice(text_templates)

    entities = []
    for word, label in [(name, "CANDIDATE_NAME"), (job, "JOB_TITLE"), (company, "COMPANY"),
                        (skill, "SKILLS"), (university, "EDUCATION"), (graduation_year, "DATES"),
                        (email, "EMAIL"), (phone, "PHONE")]:
        span = find_entity(text, word)
        if span:
            entities.append((span[0], span[1], label))

    # 🔥 **Remove overlapping entities BEFORE saving to train_data**
    non_overlapping_entities = remove_overlapping_entities(entities)

    train_data.append({"text": text, "entities": non_overlapping_entities})

with open("../data/train_data.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, indent=4)

print("✅ Artificial data created successfully (without overlapping entities)!")
