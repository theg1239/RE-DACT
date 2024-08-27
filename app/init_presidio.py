import random
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from faker import Faker

# Initialize the engines
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
        return fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
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
    Recognize and anonymize sensitive entities in the input text.

    Args:
        text (str): The input text to process.
        redaction_level (int): The level of redaction (0 to 100).

    Returns:
        str: The text with sensitive entities anonymized and replaced with fake data.
    """
    # Ensure redaction_level is numeric
    try:
        redaction_level = (
            float(redaction_level) / 100.0
        )  # Convert to a fraction if necessary
    except ValueError:
        raise ValueError("Redaction level must be a number.")

    # Analyze the text to find sensitive entities
    analysis_results = analyzer.analyze(text=text, entities=[], language="en")

    # Anonymize each entity with a fake value depending on the redaction level
    anonymized_result = text
    for result in analysis_results:
        entity_text = text[result.start : result.end]

        # Redact based on redaction level
        if redaction_level >= 0.5:  # Example condition for redaction
            fake_value = generate_fake_entity(result.entity_type)
            anonymized_result = anonymized_result.replace(entity_text, fake_value)

    return anonymized_result
