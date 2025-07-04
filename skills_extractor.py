def extract_skills(text, skills_list):
    text_lower = text.lower()
    found_skills = set()
    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.add(skill)
    return list(found_skills)

# Example skill list (you can expand this!)
SKILLS_DB = [
    "Python", "JavaScript", "SQL", "Power BI", "C++", "Java",
    "React", "Node.js", "HTML", "CSS", "Git", "Docker", "AWS",
    "Machine Learning", "Data Analysis", "Automation", "Linux"
]
