import spacy

print("loading trained model")
nlp = spacy.load("../models/resume_parser_model")

test_texts = [
    "John Smith works as a Machine Learning Engineer at Google.",
    "Alice Johnson is a Senior Software Engineer at Amazon.",
    "Michael Lee recently got hired by OpenAI as a Research Scientist.",
    "Sarah Connor is currently working at Tesla as a Robotics Engineer.",
    "He has expertise in Python, TensorFlow, and NLP.",
    "Her key skills include JavaScript, React, and UI/UX Design.",
    "Expert in Kubernetes, Docker, and Cloud Computing.",
    "Highly skilled in Deep Learning and Neural Networks.",
    "He graduated from Stanford University in 2019.",
    "She earned her Computer Science degree from Harvard in 2021.",
    "Completed an MBA at Wharton School in 2018.",
    "Studied Artificial Intelligence at MIT in 2023.",
    "You can contact me at john.doe@email.com or +1 123 456 7890.",
    "Reach out to Sarah at sarah.connor@example.com or call +44 9876 543210.",
    "Feel free to email me at techguy42@techmail.com.",
    "Phone: +91 99999 88888, Email: research.scientist@aiworld.com.",
    "Microsoft is looking to hire a Data Analyst for their AI team.",
    "Amazon has an open position for a Full Stack Developer.",
    "Apple is recruiting a Security Engineer for its iOS division.",
    "Meta recently posted a job opening for a Cloud Architect.",
    "Name: Robert Downey Jr.\nJob Title: Cybersecurity Engineer\nCompany: Tesla\nSkills: Ethical Hacking, Penetration Testing, Network Security",
    "Contact Info: susan.wilson@workmail.com | +33 765432189\nExperience: Data Engineer at Google (2020 - Present)",
    "Maria Gonzales | Senior Product Manager | Facebook\nEducation: MBA from Stanford, 2016\nSkills: Agile, Scrum, Market Research",
    "Resume: \nName: Daniel Brown\nEmail: daniel.brown@email.com\nPhone: +49 123 456 789\nEducation: MIT, 2022\nExperience: Software Engineer at Apple"
]

for text in test_texts:
    doc = nlp(text)
    print(f"Text: {text}")
    print("Entities: ", [(ent.text, ent.label_) for ent in doc.ents])
    print()
