import google.generativeai as genai

def generate_fit_answer(resume_info: dict, job_description: str) -> str:
    """
    Generate a short and sweet interview answer to
    "Why are you a good fit for this job?" using Gemini chat API.

    Args:
        resume_info: dict with keys like 'name', 'skills', 'soft_skills', etc.
        job_description: full text of the job posting

    Returns:
        Generated answer string.
    """
    prompt = f"""
Given the following resume information and job description, write a short and sweet interview answer to "Why are you a good fit for this job?".

Resume Information:
Name: {resume_info.get('name', 'N/A')}
Skills: {', '.join(resume_info.get('skills', []))}
Soft Skills: {', '.join(resume_info.get('soft_skills', []))}

Job Description:
{job_description}

Answer:
"""
    response = genai.chat.create(
        model="models/chat-bison-001",  # or your Gemini model like "gemini-1.5-flash"
        messages=[{"author": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200,
    )
    return response.last.response.strip()
