from file_loader import extract_text
from info_extractor import extract_email, extract_phone
from name_extractor import extract_name
from skills_extractor import extract_skills, SKILLS_DB
from job_description_loader import get_text_from_url, get_text_from_user_input
from gemini_utils import generate_fit_answer

def get_job_description():
    choice = input("\nDo you want to (1) paste the job description or (2) provide a URL? Enter 1 or 2: ")
    if choice == '1':
        return get_text_from_user_input()
    elif choice == '2':
        url = input("Enter the job posting URL: ")
        return get_text_from_url(url)
    else:
        print("Invalid option.")
        return None

def main():
    path = input("Enter resume file path (.pdf or .docx): ")
    text = extract_text(path)

    print("\nExtracted Text (first 300 chars):")
    print(text[:300])

    email = extract_email(text)
    phone = extract_phone(text)
    name = extract_name(text)
    skills = extract_skills(text, SKILLS_DB)

    print("\nExtracted Resume Information:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Skills: {', '.join(skills) if skills else 'None found'}")

    job_text = get_job_description()
    if not job_text:
        print("No job description provided, exiting.")
        return

    job_skills = extract_skills(job_text, SKILLS_DB)

    matched = set(skills) & set(job_skills)
    missing = set(job_skills) - set(skills)
    total_required = len(job_skills)
    total_matched = len(matched)
    score_percentage = round((total_matched / total_required) * 100, 2) if total_required > 0 else 0

    print("\n📋 Job Description Match Summary:")
    print(f"- Total required skills: {total_required}")
    print(f"- Matched skills: {total_matched}")
    print(f"- Score: {total_matched} / {total_required} → {score_percentage}%")

    print("\n✅ Skills You Have:")
    print(", ".join(matched) or "None")

    print("\n⚠️ Skills You’re Missing:")
    print(", ".join(missing) or "None")

    resume_info = {
        "name": name,
        "skills": skills,
        # Add soft skills if you implement extraction
    }

    print("\n🤝 Generating 'Why You're a Good Fit' answer...\n")
    fit_answer = generate_fit_answer(resume_info, job_text)
    print(fit_answer)

if __name__ == '__main__':
    main()
