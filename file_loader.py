import pdfplumber
import docx

def extract_text(uploaded_file):
    file_name = uploaded_file.name

    if file_name.endswith('.pdf'):
        with pdfplumber.open(uploaded_file) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text

    elif file_name.endswith('.docx'):
        doc = docx.Document(uploaded_file)
        return '\n'.join([p.text for p in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format. Only PDF and DOCX are supported.")
