# app/init_presidio.py

from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from faker import Faker
import random

# Initialize Presidio Analyzer and Anonymizer
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Initialize Faker
fake = Faker()

def generate_fake_entity(entity_type):
    """
    Generate a fake value based on the entity type.

    Args:
        entity_type (str): The type of the entity.

    Returns:
        str: A fake value corresponding to the entity type.
    """
    if entity_type == "PERSON":
        return fake.name()
    elif entity_type == "LOCATION":
        return fake.city()
    elif entity_type == "EMAIL_ADDRESS":
        return fake.email()
    elif entity_type == "PHONE_NUMBER":
        return fake.phone_number()
    elif entity_type == "CREDIT_CARD":
        return fake.credit_card_number()
    elif entity_type == "IP_ADDRESS":
        return fake.ipv4()
    elif entity_type == "DATE_TIME":
        return fake.date_time().strftime('%Y-%m-%d %H:%M:%S')
    elif entity_type == "URL":
        return fake.url()
    elif entity_type == "NRP":
        return f"{fake.country()} {fake.word()}"
    elif entity_type == "IBAN_CODE":
        return fake.iban()
    elif entity_type == "CRYPTO":
        return "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    elif entity_type == "IN_PAN":
        return fake.bothify(text="?????#####?")
    elif entity_type == "IN_AADHAAR":
        return fake.bothify(text="####-####-####")
    elif entity_type == "US_PASSPORT":
        return fake.bothify(text="#########")
    elif entity_type == "US_DRIVER_LICENSE":
        return fake.bothify(text="D########")
    # Add more mappings as necessary for other entity types
    return "<REDACTED>"

def recognize_and_anonymize_entities(text, redaction_level):
    """
    Recognize and anonymize sensitive entities in the input text based on redaction level.

    Args:
        text (str): The input text to process.
        redaction_level (int): The level of redaction (0-100).

    Returns:
        str: The text with sensitive entities anonymized and replaced with fake data.
    """
    # Analyze the text to find sensitive entities
    analysis_results = analyzer.analyze(text=text, entities=[], language='en')

    # Determine redaction threshold
    threshold = redaction_level / 100.0

    # Anonymize each entity with a fake value
    anonymized_result = text
    for result in analysis_results:
        # Use redaction level to determine if the entity should be redacted
        if result.score >= threshold:
            entity_text = text[result.start:result.end]
            fake_value = generate_fake_entity(result.entity_type)
            anonymized_result = anonymized_result.replace(entity_text, fake_value)

    return anonymized_result