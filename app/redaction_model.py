from app.init_presidio import analyzer, anonymizer
from presidio_anonymizer.entities import OperatorConfig


def advanced_redact_text(text):
    # Analyze the text to detect entities
    results = analyzer.analyze(text=text, entities=[], language="en")

    # Anonymize detected entities using replacement or placeholders
    anonymized_text = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
        operators={
            "DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"}),
            # Customize specific entities if needed
        },
    )

    return anonymized_text.text
