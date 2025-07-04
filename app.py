import streamlit as st
from file_loader import extract_text
from info_extractor import extract_email, extract_phone
from name_extractor import extract_name
from skills_extractor import extract_skills, SKILLS_DB
from job_description_loader import get_text_from_url

st.title("📄 Resume Scanner & Job Matcher")

uploaded_file = st.file_uploader("Upload your resume (.pdf or .docx)", type=['pdf', 'docx'])
job_input_type = st.radio("How do you want to provide the job description?", ["Paste Text", "Provide URL"])

job_text = ""
if job_input_type == "Paste Text":
    job_text = st.text_area("Paste the job description here")
else:
    job_url = st.text_input("Enter the job posting URL")
    if job_url:
        job_text = get_text_from_url(job_url)

if uploaded_file and job_text:
    resume_text = extract_text(uploaded_file)
    
    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    resume_skills = extract_skills(resume_text, SKILLS_DB)
    job_skills = extract_skills(job_text, SKILLS_DB)
    
    matched = set(resume_skills) & set(job_skills)
    missing = set(job_skills) - set(resume_skills)
    total_required = len(set(job_skills))
    total_matched = len(matched)
    score_percentage = round((total_matched / total_required) * 100, 2) if total_required > 0 else 0
    
    st.subheader("📋 Resume Info")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Skills:** {', '.join(resume_skills)}")
    
    st.subheader("📊 Job Match Summary")
    st.write(f"**Score:** {total_matched} / {total_required} → {score_percentage}%")
    st.success(f"Matched Skills: {', '.join(matched) if matched else 'None'}")
    st.warning(f"Missing Skills: {', '.join(missing) if missing else 'None'}")
