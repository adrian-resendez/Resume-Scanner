# job_description_loader.py
import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("✅ Fetched URL successfully!")  # ← Add this
        soup = BeautifulSoup(response.text, 'html.parser')

        texts = soup.find_all(text=True)
        visible_texts = filter(tag_visible, texts)
        result = u" ".join(t.strip() for t in visible_texts if t.strip())

        # Print first few lines of result
        print("\n🔍 Extracted text preview:")
        print(result[:1000])  # show first 1000 characters
        return result
    except Exception as e:
        print(f"❌ Error fetching URL: {e}")
        return ""


def tag_visible(element):
    # Skip scripts, styles, etc.
    from bs4.element import Comment
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def get_text_from_user_input():
    print("\nPaste the job description below (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    return "\n".join(lines)
