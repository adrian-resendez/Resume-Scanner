import streamlit as st
from gemini_utils import generate_fit_answer
from file_loader import extract_text
from info_extractor import extract_email, extract_phone
from name_extractor import extract_name
from skills_extractor import extract_skills, SKILLS_DB
from job_description_loader import get_text_from_url, get_text_from_user_input

def main():
    st.title("📄 Resume Scanner & Job Matcher")

    uploaded_file = st.file_uploader("Upload Resume (.pdf or .docx)", type=["pdf", "docx"])
    if not uploaded_file:
        st.info("Please upload your resume to get started.")
        return

    # Extract resume text
    resume_text = extract_text(uploaded_file)

    # Extract info
    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    skills = extract_skills(resume_text, SKILLS_DB)

    st.header("👤 Resume Info")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Skills ({len(skills)}):** {', '.join(skills)}")

    # Job description input
    option = st.radio("Choose input method:", ("Paste Text", "Provide URL"))

    if option == "Paste Text":
        job_description = st.text_area("Paste the job description here")
    else:
        url = st.text_input("Enter the job posting URL")
        if url:
            job_description = get_text_from_url(url)
        else:
            job_description = ""

    if job_description:
        job_skills = extract_skills(job_description, SKILLS_DB)

        matched = set(skills) & set(job_skills)
        missing = set(job_skills) - set(skills)
        total_required = len(job_skills)
        total_matched = len(matched)
        score = round((total_matched / total_required) * 100, 2) if total_required > 0 else 0

        st.header("📊 Match Summary")
        st.write(f"Matching Score: {total_matched} / {total_required} ({score}%)")
        st.success(f"✅ Matched Skills: {', '.join(matched) or 'None'}")
        st.error(f"🛑 Missing Skills: {', '.join(missing) or 'None'}")

        # Generate and show the "Why you're a good fit" answer using Gemini
        resume_info = {
            "name": name,
            "skills": skills,
            # add soft skills if you have them
        }
        with st.spinner("Generating 'Why you’re a good fit' answer..."):
            fit_answer = generate_fit_answer(resume_info, job_description)

        st.header("🤝 Why You're a Good Fit")
        st.write(fit_answer)

if __name__ == "__main__":
    main()
