from langchain_community.document_loaders import PyPDFLoader

from pypdf import PdfReader

def extract_text_from_cv(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    return text