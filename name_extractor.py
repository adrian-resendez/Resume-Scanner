import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    # Check only top 10 lines
    lines = text.strip().split("\n")[:10]

    # Pre-clean the lines
    cleaned_lines = [
        line.strip()
        for line in lines
        if line.strip() and not any(kw in line.lower() for kw in ["email", "phone", "linkedin", "contact", "resume", "address"])
    ]

    # Use spaCy on top lines only
    for line in cleaned_lines:
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                name_parts = ent.text.strip().split()
                if 2 <= len(name_parts) <= 3 and all(word.istitle() for word in name_parts):
                    return f"{name_parts[0]} {name_parts[-1]}"

    # Fallback: Regex on top lines (e.g. "John Smith")
    for line in cleaned_lines:
        match = re.match(r'^([A-Z][a-z]{1,})\s+([A-Z][a-z]{1,})$', line)
        if match:
            return f"{match.group(1)} {match.group(2)}"

    return None
