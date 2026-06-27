import streamlit as st

from frontend.components.hero import render_hero
from frontend.components.cards import render_info_card
from frontend.components.sections import render_section_header, render_divider
from frontend.components.gauges import render_confidence_gauge
from frontend.components.badges import render_badge
from utils.report_generator import generate_pdf_report


def show_result(legal_info, summary, prediction, confidence):

    # ── Hero Header ──────────────────────────────────
    render_hero(
        badge_text="📑 AI Analysis Report",
        title="JudgeAI Analysis Report",
        description=(
            "Complete legal analysis including extracted metadata, "
            "AI-generated summary, case prediction, and downloadable report."
        ),
        compact=True,
    )

    # ── Case Information ─────────────────────────────
    render_section_header("📋", "Case Information")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        render_info_card("📅 Date of Judgment", legal_info["date"], "blue")
        render_info_card("⚖ Court", legal_info["court"], "blue")
        render_info_card("📄 Case Type", legal_info["case_type"], "gold")
        render_info_card("📑 Case Number", legal_info["case_number"], "gold")

    with col2:
        bench = legal_info.get("bench", "Not Found")
        if isinstance(bench, list):
            bench = ", ".join(bench) if bench else "Not Found"

        acts = legal_info.get("acts", "Not Found")
        if isinstance(acts, list):
            acts = ", ".join(acts) if acts else "Not Found"

        sections = legal_info.get("sections", "Not Found")
        if isinstance(sections, list):
            sections = ", ".join(sections) if sections else "Not Found"

        render_info_card("👨‍⚖ Bench", bench, "blue")
        render_info_card("📚 Acts", acts, "gold")
        render_info_card("📌 Sections", sections, "blue")

    render_divider()

    # ── Headnote ─────────────────────────────────────
    render_section_header("📝", "Headnote")

    headnote = legal_info["headnote"]
    if headnote != "Not Found":
        st.markdown(
            f"""
            <div class="result-section">
                <div class="result-section__body">{headnote}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-section" style="text-align:center;">
                <p style="color:var(--text-muted) !important;font-style:italic;">Headnote not available.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Legal Issue ──────────────────────────────────
    render_section_header("⚠️", "Legal Issue")

    legal_issue = legal_info["legal_issue"]
    if legal_issue != "Not Found":
        st.markdown(
            f"""
            <div class="result-section">
                <div class="result-section__body">{legal_issue}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-section" style="text-align:center;">
                <p style="color:var(--text-muted) !important;font-style:italic;">Legal issue not identified.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Final Decision ───────────────────────────────
    render_section_header("⚖", "Final Decision")

    decision = legal_info["final_decision"]

    if "Allowed" in decision:
        decision_color = "green"
        decision_icon = "✓"
    elif "Dismissed" in decision:
        decision_color = "red"
        decision_icon = "✗"
    else:
        decision_color = "gold"
        decision_icon = "◐"

    color_map = {
        "green": ("rgba(74,222,128,0.08)", "rgba(74,222,128,0.2)", "#4ADE80"),
        "red": ("rgba(248,113,113,0.08)", "rgba(248,113,113,0.2)", "#F87171"),
        "gold": ("rgba(251,191,36,0.08)", "rgba(251,191,36,0.2)", "#FBBF24"),
    }
    bg, border, color = color_map[decision_color]

    st.markdown(
        f"""
        <div class="result-section" style="background:{bg};border-color:{border};text-align:center;padding:28px;">
            <div style="font-size:36px;margin-bottom:10px;">{decision_icon}</div>
            <div style="font-size:20px;font-weight:700;color:{color};">{decision}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_divider()

    # ── AI Summary ───────────────────────────────────
    render_section_header("🤖", "AI Generated Summary")

    st.markdown(
        f"""
        <div class="result-section" style="border-left:3px solid var(--accent-blue);">
            <div class="result-section__header">
                <span class="result-section__icon">🤖</span>
                <span class="result-section__title">AI Summary</span>
                {render_badge("NLP Generated", "blue")}
            </div>
            <div class="result-section__body">{summary}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_divider()

    # ── ML Prediction ────────────────────────────────
    render_section_header("🧠", "ML Prediction")

    # Prediction badge
    if prediction == "Accepted":
        pred_class = "prediction-badge--accepted"
        pred_icon = "✓"
    elif prediction == "Rejected":
        pred_class = "prediction-badge--rejected"
        pred_icon = "✗"
    else:
        pred_class = "prediction-badge--neutral"
        pred_icon = "◐"

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown(
            f"""
            <div class="prediction-card">
                <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text-muted);margin-bottom:12px;">
                    Predicted Outcome
                </div>
                <div class="prediction-badge {pred_class}">
                    {pred_icon} {prediction}
                </div>
                <div style="font-size:12px;color:var(--text-muted);margin-top:8px;">
                    Random Forest · Jud-IPL Dataset
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="prediction-card">
                <div style="font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--text-muted);margin-bottom:12px;">
                    Confidence Score
                </div>
            """,
            unsafe_allow_html=True,
        )
        render_confidence_gauge(confidence)
        st.markdown("</div>", unsafe_allow_html=True)

    render_divider()

    # ── Download Report ──────────────────────────────
    render_section_header("📄", "Export Report")

    st.markdown(
        """
        <div class="download-card">
            <div style="font-size:32px;margin-bottom:12px;">📄</div>
            <div style="font-size:16px;font-weight:600;color:var(--text-primary);margin-bottom:4px;">
                Download Analysis Report
            </div>
            <p style="font-size:13px;color:var(--text-muted) !important;margin-bottom:16px;">
                Professional PDF report with all findings, metadata, and predictions.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    pdf = generate_pdf_report(
        legal_info=legal_info,
        summary=summary,
        prediction=prediction,
        confidence=confidence,
    )

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name="JudgeAI_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )