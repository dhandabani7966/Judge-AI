from docx import Document
import tempfile

def extract_text_from_docx(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".docx") as f:
        f.write(uploaded_file.read())
        path=f.name
    doc=Document(path)
    return "\n".join(p.text for p in doc.paragraphs)
