from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    legal_info,
    summary,
    prediction,
    confidence,
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>JudgeAI Analysis Report</b>", styles["Title"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    fields = [
        ("Date", legal_info["date"]),
        ("Court", legal_info["court"]),
        ("Case Type", legal_info["case_type"]),
        ("Case Number", legal_info["case_number"]),
        ("Bench", str(legal_info["bench"])),
        ("Acts", str(legal_info["acts"])),
        ("Sections", str(legal_info["sections"])),
        ("Final Decision", legal_info["final_decision"]),
        ("Prediction", prediction),
        ("Confidence", f"{confidence:.2f}%"),
    ]

    for title, value in fields:
        story.append(
            Paragraph(
                f"<b>{title}</b>: {value}",
                styles["BodyText"],
            )
        )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>Headnote</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            legal_info["headnote"],
            styles["BodyText"],
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>Legal Issue</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            legal_info["legal_issue"],
            styles["BodyText"],
        )
    )

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(
        Paragraph(
            "<b>AI Summary</b>",
            styles["Heading2"],
        )
    )

    story.append(
        Paragraph(
            summary,
            styles["BodyText"],
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf