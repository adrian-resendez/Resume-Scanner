# name_extractor.py
import re
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    # Step 1: Try spaCy for person entities
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            cleaned = ent.text.strip()
            name_parts = cleaned.split()
            if 2 <= len(name_parts) <= 3:
                return f"{name_parts[0]} {name_parts[-1]}"

    # Step 2: Fallback regex in first 10 lines
    lines = text.strip().split('\n')[:10]
    for line in lines:
        line = line.strip()
        if not line or any(word in line.lower() for word in ["contact", "email", "phone", "address"]):
            continue
        match = re.match(r'^([A-Z][a-z]+)\s+([A-Z][a-z]+)$', line)
        if match:
            return f"{match.group(1)} {match.group(2)}"
    
    return None
