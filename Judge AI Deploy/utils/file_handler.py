from utils.pdf_extractor import extract_text_from_pdf
from utils.docx_extractor import extract_text_from_docx
from utils.txt_extractor import extract_text_from_txt
from utils.csv_extractor import extract_text_from_csv

def extract_text(uploaded_file):
    ext=uploaded_file.name.split(".")[-1].lower()
    if ext=="pdf":
        return extract_text_from_pdf(uploaded_file)
    elif ext=="docx":
        return extract_text_from_docx(uploaded_file)
    elif ext=="txt":
        return extract_text_from_txt(uploaded_file)
    elif ext=="csv":
        return extract_text_from_csv(uploaded_file)
    return ""
