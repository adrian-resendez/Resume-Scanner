import streamlit as st
import google.generativeai as genai

# Prefer secrets if available (Streamlit Cloud), otherwise fall back to .env (local dev)
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in Streamlit secrets or environment variables.")

genai.configure(api_key=api_key)



def generate_fit_answer(resume_info: dict, job_description: str) -> str:
    """
    Uses Gemini to generate a short and sweet "Why I'm a good fit" answer.
    """
    prompt = f"""
Given the following resume and job description, write a short and sweet answer to the interview question:
"Why are you a good fit for this job?"

Resume Info:
Name: {resume_info.get('name', 'N/A')}
Skills: {', '.join(resume_info.get('skills', []))}
Soft Skills: {', '.join(resume_info.get('soft_skills', [])) if resume_info.get('soft_skills') else 'N/A'}

Job Description:
{job_description}

Answer:
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
