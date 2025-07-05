# info_extractor.py
import re

def extract_email(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    matches = re.findall(email_regex, text)
    return matches[0] if matches else None

def extract_phone(text):
    phone_regex = r'(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?[\s-]?)?\d{3}[\s-]?\d{4}'
    matches = re.findall(phone_regex, text)
    if matches:
        # re.findall with groups returns list of tuples, but we want full match
        # Let's use re.search instead
        match = re.search(phone_regex, text)
        return match.group(0) if match else None
    return None


import re
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")