import streamlit as st
from file_loader import extract_text
from info_extractor import extract_email, extract_phone
from name_extractor import extract_name
from skills_extractor import extract_skills, SKILLS_DB
from job_description_loader import get_text_from_url

st.set_page_config(page_title="Resume Scanner & Job Matcher", page_icon="📄", layout="centered")

# ------------------------
# Header
# ------------------------
st.markdown("<h1 style='text-align: center;'>📄 Resume Scanner & Job Matcher</h1>", unsafe_allow_html=True)
st.markdown("Upload your resume and compare it with a job description to see how well you match!")

# ------------------------
# Upload & Input
# ------------------------
st.markdown("### 🔹 Step 1: Upload Resume")
uploaded_file = st.file_uploader("Choose a .pdf or .docx file", type=['pdf', 'docx'])

st.markdown("### 🔹 Step 2: Provide Job Description")
job_input_type = st.radio("Choose input method:", ["Paste Text", "Provide URL"], horizontal=True)

job_text = ""
if job_input_type == "Paste Text":
    job_text = st.text_area("Paste the job description below", height=200)
else:
    job_url = st.text_input("Enter the job posting URL")
    if job_url:
        job_text = get_text_from_url(job_url)

# ------------------------
# Processing
# ------------------------
if uploaded_file and job_text:
    st.markdown("### ✅ Processing your resume...")
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

    # ------------------------
    # Resume Info
    # ------------------------
    st.markdown("### 👤 Resume Info")
    col1, col2 = st.columns(2)
    col1.markdown(f"**Name:** `{name}`")
    col1.markdown(f"**Email:** `{email}`")
    col1.markdown(f"**Phone:** `{phone}`")
    col2.markdown(f"**Skills ({len(resume_skills)}):**")
    col2.markdown(f"`{', '.join(resume_skills)}`")

    # ------------------------
    # Job Match Summary
    # ------------------------
    st.markdown("---")
    st.markdown("### 📊 Match Summary")
    st.metric(label="Matching Score", value=f"{total_matched} / {total_required}", delta=f"{score_percentage}%")

    if matched:
        st.success(f"✅ **Matched Skills:** {', '.join(matched)}")
    else:
        st.warning("⚠️ No matched skills found.")

    if missing:
        st.error(f"🛑 **Missing Skills:** {', '.join(missing)}")
    else:
        st.info("🎉 All required skills are present!")

else:
    st.info("⬆️ Upload your resume and enter a job description to begin.")

