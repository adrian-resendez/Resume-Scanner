# 🧠 Resume Scanner & Job Match Scorer

A Python + Streamlit web app that helps job seekers evaluate how well their resume matches a specific job description — using natural language processing, smart keyword matching, and a clean user interface.

🚀 Built by a Computer Science grad actively breaking into tech through hands-on, meaningful projects.

---

## 🌟 Live App

▶️ **Try It Here:** [https://resume-scanner.streamlit.app](https://resume-inspector.streamlit.app)  
(No signup needed — just upload your resume and paste a job description or URL.)

---

## 🎯 Features

✅ **Resume Analysis (PDF/DOCX)**  
- Name detection using spaCy NER  
- Email & phone extraction using regex  
- Skill extraction using a keyword database

✅ **Job Description Input Options**  
- Paste job description text directly  
- Or enter a job posting URL (basic scraping support)

✅ **Matching & Scoring**  
- Calculates match score: `e.g. 14 / 20 → 70%`  
- Shows matched vs. missing skills  
- Visual summary of alignment

✅ **Streamlit-Powered UI**  
- Drag-and-drop resume upload  
- Clean and simple layout  
- Web-deployable via Streamlit Cloud

---

## 🛠️ Tech Stack

| Tool/Library       | Purpose                            |
|--------------------|------------------------------------|
| Python             | Core language                      |
| Streamlit          | Frontend & web hosting             |
| pdfplumber         | PDF parsing                        |
| python-docx        | DOCX parsing                       |
| spaCy              | Name Entity Recognition (NER)      |
| re (regex)         | Email and phone extraction         |
| BeautifulSoup4     | Job posting scraping (HTML)        |
| Requests           | Fetching job posting URLs          |

---

## 📂 Project Structure

resume-scanner/
├── app.py # Streamlit web app interface
├── main.py # CLI version (optional)
├── file_loader.py # Resume file parser
├── info_extractor.py # Email & phone via regex
├── name_extractor.py # spaCy NER name detection
├── skills_extractor.py # Skill matching logic
├── job_description_loader.py # Load job description from URL or text
├── requirements.txt # Python dependencies
└── README.md # This file

---

## 🧑‍💻 Skills Demonstrated

- ✅ End-to-end app: from raw files to insight
- ✅ NLP (name recognition, keyword extraction)
- ✅ Web scraping & URL parsing
- ✅ Regex-based text extraction
- ✅ Modular, clean code organization
- ✅ Frontend + backend integration via Streamlit

---

## 🧪 Try It Locally

### 🔧 1. Clone the repo


git clone https://github.com/adrian-resendez/Resume-Scanner
cd resume-scanner

📦 2. Create virtual environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

📥 3. Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm

▶️ Run Locally (Web App)


streamlit run app.

Visit http://localhost:8501 to try it out in your browser.

📊 Example Output
Resume Extracted:

Name: Fernando Resendez
Email: work.resendez@gmail.com
Phone: (530) 339-0383
Skills: Python, SQL, Power BI, Git, Automation, 

Job Match Summary:

Total Skills Required: 10  
Matched Skills: 6  
Score: 6 / 10 → 60%

✅ Skills You Have:  
Python, Power BI, SQL, Git

⚠️ Skills You’re Missing:  
React, AWS, Docker, Machine Learning

🔮 Future Roadmap
🌐 Better job scraping (Selenium or Playwright)

🧠 Semantic skill matching (embeddings, transformers)

📤 Export results to JSON or CSV

✍️ Resume improvement suggestions

🧪 Upload multiple job descriptions to compare

💼 For Recruiters & Hiring Managers
This project is more than code — it’s a reflection of real-world problem solving.

✅ I built this to automate a process every job seeker faces
✅ I used NLP, regex, and scraping to build something useful from scratch
✅ I deployed it to the web with zero cost using Streamlit
✅ The code is modular and expandable for future integrations

🙋 About Me
👋 I'm a first-gen Mexican-American Computer Science graduate.
💡 I focus on automation, data analysis, and full-stack development.
🚀 I’m actively job hunting and learning nonstop.

Let’s connect:
🔗 LinkedIn – [Adrian Resendez]  https://www.linkedin.com/in/adrian-resendez-08451b265/

