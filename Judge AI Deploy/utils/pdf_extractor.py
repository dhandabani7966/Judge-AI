import fitz

def extract_text_from_pdf(pdf_file):
    """
    Extract text from uploaded PDF.
    """

    document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    extracted_text = ""

    for page in document:
        extracted_text += page.get_text()

    return extracted_text

