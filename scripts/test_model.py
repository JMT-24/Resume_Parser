import spacy

print("loading trained model")
nlp = spacy.load("../models/resume_parser_model")

test_texts = [
    # Standard resume-like sentences
    "John Smith is a Machine Learning Engineer at Google.",
    "Alice Johnson, Senior Software Engineer @ Amazon.",
    "Michael Lee recently got hired by OpenAI as a Research Scientist.",
    "Sarah Connor - Robotics Engineer, currently working at Tesla.",
    
    # Unstructured & informal resume data
    "Python expert | Google | 5 years experience.",
    "AI specialist. Previously: Microsoft, OpenAI.",
    "Skills: JavaScript, React, UI/UX. Contact: techguy42@techmail.com.",
    "Graduated Stanford University, 2019. Ex-Facebook.",
    
    # Contact information in different formats
    "You can reach me at john.doe@email.com | +1 123 456 7890.",
    "Sarah's contact: sarah.connor@example.com | Ph: +44 9876 543210.",
    "Email: research.scientist@aiworld.com | Phone: +91 99999 88888.",
    
    # International names & companies
    "René Dupont is a Data Scientist at BNP Paribas in France.",
    "Carlos Martínez | Backend Developer | Mercado Libre.",
    "Akira Takahashi works at Sony as a Robotics Engineer.",
    
    # Job postings
    "Microsoft is hiring a Data Analyst for its AI team.",
    "Amazon seeks a Full Stack Developer.",
    "Apple is looking for a Security Engineer in its iOS division.",
    "Meta recently announced a Cloud Architect opening.",
    
    # Messy, informal, and typo cases
    "Johhn Smitth is a ML Eng. @ Gogle",
    "Michael, Lee got hired - OpenAI (Research Scientist).",
    "Sr. Software Eng. at MSFT.",
    
    # Resume-style structured entries
    "Name: Robert Downey Jr.\nJob: Cybersecurity Engineer\nCompany: Tesla\nSkills: Ethical Hacking, Pen Testing",
    "Contact Info: susan.wilson@workmail.com | +33 765432189\nExperience: Data Engineer @ Google (2020 - Present)",
    "Maria Gonzales | Senior Product Manager | Facebook\nEducation: MBA - Stanford, 2016\nSkills: Agile, Scrum, Market Research",
    "Resume:\nName: Daniel Brown\nEmail: daniel.brown@email.com\nPhone: +49 123 456 789\nEducation: MIT, 2022\nExperience: Software Engineer - Apple"
]


for text in test_texts:
    doc = nlp(text)
    print(f"Text: {text}")
    print("Entities: ", [(ent.text, ent.label_) for ent in doc.ents])
    print()
