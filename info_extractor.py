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


def extract_name(text):
    # Look only in the first 10 lines of the resume
    lines = text.strip().split('\n')[:10]
    for line in lines:
        line = line.strip()
        # Skip empty lines or junk
        if not line or any(word.lower() in line.lower() for word in ["contact", "email", "phone", "address"]):
            continue
        # Match two words that look like names (capitalized, no digits)
        name_match = re.match(r'^([A-Z][a-z]+)\s+([A-Z][a-z]+)$', line)
        if name_match:
            return f"{name_match.group(1)} {name_match.group(2)}"
    return None