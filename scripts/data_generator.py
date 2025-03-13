import json
import random
import re
from faker import Faker
import phonenumbers

fake = Faker()
Faker.seed(42)

# Function to find entity spans
def find_entity(text, word):
    word = re.escape(word.strip(",."))
    match = re.search(rf"(?<!\w){word}(?!\w)", text)
    return (match.start(), match.end()) if match else None

# Prevent overlapping entities
def remove_overlapping_entities(entities):
    priority = {
        "JOB_TITLE": 1, "EMAIL": 2, "PHONE": 2, "SKILLS": 3, "COMPANY": 4, "EDUCATION": 5, "CANDIDATE_NAME": 6,
        "DATES": 7, "ADDRESS": 8, "COURSE": 9
    }
    
    sorted_entities = sorted(entities, key=lambda x: (x[0], priority.get(x[2], 99)))
    non_overlapping = []
    last_end = -1

    for start, end, label in sorted_entities:
        if start >= last_end:
            non_overlapping.append((start, end, label))
            last_end = end

    return non_overlapping

# Generate diverse data
skills = ["Python", "AWS", "TensorFlow", "Cybersecurity", "Cloud Computing", "JavaScript", "Kotlin", "Machine Learning", "React", "Agile", "Pen Testing", "SQL", "Databases", "Programming"]
job_titles = ["Software Engineer", "Data Scientist", "DevOps Engineer", "Security Analyst", "Cloud Architect", "Machine Learning Engineer", "Backend Developer", "Senior Software Engineer"]
universities = ["Harvard University", "MIT", "Stanford University", "University of Toronto", "Oxford University", "Carnegie Mellon University", "University of Batangas", "Far Eastern University", "Ateneo de Manila University"]
companies = ["Google", "Microsoft", "Amazon", "Facebook", "Tesla", "OpenAI", "Meta", "BNP Paribas", "IBM", "Netflix"]
locations = ["Blk1 Lot7, Lipa City", "Leviste Hwy, Batangas", "New York, USA", "San Francisco, CA", "Tokyo, Japan", "Paris, France", "Berlin, Germany", "Makati City", "Quezon City"]
courses = ["Harvard’s CS50", "AWS ML Certification", "Google Cloud DevOps", "MIT AI Ethics", "Stanford Data Science", "Database Systems", "Computer Networks"]
date_variations = ["June 30, 2023", "Oct 2023 - May 2024", "2022-2024", "2019", "Spring 2025", "Summer 2018"]
phone_prefixes = ["+63", "+91", "+44", "+1", "+49"]  # Common country codes

train_data = []

for _ in range(5000):  # Increase dataset size for better learning
    name, email = fake.name(), fake.email()
    phone = random.choice(phone_prefixes) + " " + fake.msisdn()[:9]
    job, company, skill = random.choice(job_titles), random.choice(companies), random.choice(skills)
    university, location, course = random.choice(universities), random.choice(locations), random.choice(courses)
    graduation_year, date = str(random.randint(1990, 2025)), random.choice(date_variations)

    text = random.choice([
        f"{name}\n{job} at {company}\nSkills: {skill}\nEmail: {email} | Phone: {phone}",
        f"{name} lives in {location}. Works at {company} as a {job}.", 
        f"{name} completed {course} in {date}.",
        f"{company} is hiring a {job}. Required skills: {skill}.",
        f"Meet {name}, a {job} skilled in {skill}, previously at {company}.",
        f"{name} | {job} | {company} | {skill}",
        f"Contact: {name} | Email: {email} | Phone: {phone}",
        f"Hiring a {job} for our {company} team. Experience in {skill} is preferred.",
        f"Education: {university} | Graduated: {graduation_year}",
        f"Location: {location} | Current Job: {job} at {company}"
    ])

    entities = []
    for word, label in [(name, "CANDIDATE_NAME"), (job, "JOB_TITLE"), (company, "COMPANY"),
                        (skill, "SKILLS"), (university, "EDUCATION"), (graduation_year, "DATES"),
                        (email, "EMAIL"), (phone, "PHONE"), (location, "ADDRESS"), (course, "COURSE"),
                        (date, "DATES")]:
        if word in text:
            span = find_entity(text, word)
            if span:
                entities.append((span[0], span[1], label))

    train_data.append({"text": text, "entities": remove_overlapping_entities(entities)})

# Save the dataset
with open("../data/train_data.json", "w", encoding="utf-8") as f:
    json.dump(train_data, f, indent=4)

print("✅ Data generation complete! 5000 samples generated with improved diversity and formatting.")
