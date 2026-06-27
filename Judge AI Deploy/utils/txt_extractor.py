def extract_text_from_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8",errors="ignore")
