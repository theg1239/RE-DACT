# app/redaction_model.py

import spacy
import random

nlp = spacy.load("en_core_web_sm")

# Predefined lists for synthetic data
SYNTHETIC_NAMES = ["Alice Johnson", "John Doe", "Jane Smith", "Robert Brown", "Emily Davis"]
SYNTHETIC_ORGS = ["Tech Corp", "GlobalTech", "Initech", "Cyberdyne Systems", "Stark Industries"]
SYNTHETIC_LOCATIONS = ["Gotham", "Metropolis", "Smallville", "Springfield", "Shelbyville"]
SYNTHETIC_EMAILS = ["example@example.com", "user@domain.com", "email@service.com"]
SYNTHETIC_PHONE_NUMBERS = ["123-456-7890", "987-654-3210", "555-555-5555"]
SYNTHETIC_DATES = ["January 1, 2000", "December 25, 2019", "July 4, 2021"]

def replace_entity(label):
    if label == "PERSON":
        return random.choice(SYNTHETIC_NAMES)
    elif label == "ORG":
        return random.choice(SYNTHETIC_ORGS)
    elif label == "GPE":
        return random.choice(SYNTHETIC_LOCATIONS)
    elif label == "DATE":
        return random.choice(SYNTHETIC_DATES)
    elif label == "EMAIL":
        return random.choice(SYNTHETIC_EMAILS)
    elif label == "PHONE":
        return random.choice(SYNTHETIC_PHONE_NUMBERS)
    return None

def advanced_redact_text(text):
    doc = nlp(text)
    new_text = text

    entities = sorted(doc.ents, key=lambda ent: ent.start_char, reverse=True)
    
    for ent in entities:
        entity_text = ent.text
        label = ent.label_
        replacement = replace_entity(label)
        
        if replacement:
            new_text = new_text[:ent.start_char] + replacement + new_text[ent.end_char:]
    
    return new_text
