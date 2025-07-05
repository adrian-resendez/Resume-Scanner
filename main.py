import os
import streamlit as st
from dotenv import load_dotenv

from gemini_utils import generate_fit_answer
from file_loader import extract_text
from info_extractor import extract_email, extract_phone
from name_extractor import extract_name
from skills_extractor import extract_skills, SKILLS_DB
from job_description_loader import get_text_from_url

# Load environment variables
load_dotenv()

def display_resume_info(text):
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text, SKILLS_DB)

    st.header("👤 Resume Info")
    st.write(f"**Name:** {name or 'Not found'}")
    st.write(f"**Email:** {email or 'Not found'}")
    st.write(f"**Phone:** {phone or 'Not found'}")
    st.write(f"**Skills ({len(skills)}):** {', '.join(skills) if skills else 'None'}")

    return name, email, phone, skills

def process_job_description_input():
    method = st.radio("🔹 Step 2: Provide Job Description", ["Paste Text", "Provide URL"])

    if method == "Paste Text":
        return st.text_area("Paste the job description here")
    else:
        url = st.text_input("Enter the job posting URL")
        if url:
            with st.spinner("Fetching job description from URL..."):
                return get_text_from_url(url)
        return ""

def display_match_summary(resume_skills, job_description):
    job_skills = extract_skills(job_description, SKILLS_DB)
    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)

    score = round((len(matched) / len(job_skills)) * 100, 2) if job_skills else 0

    st.header("📊 Match Summary")
    st.metric("Matching Score", f"{len(matched)} / {len(job_skills)} ({score}%)")
    st.success(f"✅ Matched Skills: {', '.join(matched) or 'None'}")
    st.error(f"🛑 Missing Skills: {', '.join(missing) or 'None'}")

    return job_skills

def main():
    st.set_page_config(page_title="Resume Scanner & Job Matcher", layout="centered")
    st.title("📄 Resume Scanner & Job Matcher")
    st.caption("Upload your resume and compare it with a job description to see how well you match!")

    uploaded_file = st.file_uploader("🔹 Step 1: Upload Resume", type=["pdf", "docx"])
    if not uploaded_file:
        st.info("Please upload a .pdf or .docx resume to begin.")
        return

    with st.spinner("Processing your resume..."):
        resume_text = extract_text(uploaded_file)
        name, email, phone, skills = display_resume_info(resume_text)

    job_description = process_job_description_input()
    if job_description:
        display_match_summary(skills, job_description)

        resume_info = {
            "name": name,
            "skills": skills,
            "soft_skills": ["communication", "teamwork", "adaptability"]  # add auto-extraction later if needed
        }

        with st.spinner("Generating a tailored response..."):
            fit_answer = generate_fit_answer(resume_info, job_description)

        st.header("🤝 Why You're a Good Fit")
        st.write(fit_answer)

if __name__ == "__main__":
    main()
