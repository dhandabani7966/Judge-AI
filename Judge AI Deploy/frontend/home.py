import streamlit as st

from frontend.components.hero import render_hero
from frontend.components.cards import render_glass_card, render_stat_card
from frontend.components.sections import render_section_header, render_divider
from frontend.components.badges import render_badge


def show_home():

    # ── Hero Section ─────────────────────────────────
    render_hero(
        badge_text="⚖ AI Legal Intelligence Platform",
        title="JudgeAI Pro",
        subtitle="Analyze · Summarize · Predict",
        description=(
            "Upload any court judgment and get an AI-powered breakdown in seconds — "
            "structured legal metadata, a concise summary, and an ML-predicted outcome."
        ),
    )

    # ── Format Badges ──
    st.markdown(
        f"""
        <div class="badge-row" style="margin-top:-16px;margin-bottom:24px;">
            {render_badge("📄 PDF", "gold")}
            {render_badge("📝 DOCX", "gold")}
            {render_badge("📃 TXT", "gold")}
            {render_badge("📊 CSV", "gold")}
            {render_badge("🤖 AI Powered", "blue")}
            {render_badge("⚡ < 3 sec", "blue")}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Platform Highlights ──────────────────────────
    render_section_header("🚀", "Platform Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        render_glass_card(
            icon="📄",
            title="Smart Document Analysis",
            description="Extracts dates, courts, bench details, acts, and sections from any legal document in milliseconds.",
            accent="blue",
        )

    with c2:
        render_glass_card(
            icon="🤖",
            title="AI Summary Engine",
            description="Condenses lengthy court judgments into clear, readable summaries using state-of-the-art NLP.",
            accent="gold",
        )

    with c3:
        render_glass_card(
            icon="⚖",
            title="ML Outcome Prediction",
            description="Random Forest model trained on Jud-IPL dataset predicts case outcomes with 82.47% accuracy.",
            accent="blue",
        )

    # ── Statistics ────────────────────────────────────
    render_divider()

    a, b, c, d = st.columns(4)

    with a:
        render_stat_card("⚖", "Cases Analyzed", "42,342", "+126 Today", "blue")
    with b:
        render_stat_card("🎯", "Accuracy", "82.47%", "+1.3%", "gold")
    with c:
        render_stat_card("⚡", "Avg Speed", "2.8 sec", "", "cyan")
    with d:
        render_stat_card("📄", "Export", "PDF Report", "", "green")

    # ── How It Works ─────────────────────────────────
    render_section_header("⚡", "How It Works")

    steps = [
        ("📂", "Upload", "Drop a PDF, DOCX, TXT or CSV — or paste raw judgment text."),
        ("🧹", "Process", "Text is extracted, cleaned, and prepared for analysis."),
        ("📝", "Summarize", "AI generates a structured summary of the judgment."),
        ("⚖", "Analyze", "Legal metadata — court, bench, acts, sections — is extracted."),
        ("🤖", "Predict", "ML model predicts the case outcome with a confidence score."),
        ("📄", "Export", "Download a professional PDF report with all findings."),
    ]

    cols = st.columns(3)
    for i, (icon, title, desc) in enumerate(steps):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="step-card" style="animation-delay:{i * 0.08}s;">
                    <div class="step-card__num">Step {i + 1}</div>
                    <div class="step-card__icon-wrap">{icon}</div>
                    <h3 class="glass-card__title">{title}</h3>
                    <p class="glass-card__desc">{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── Technology Stack ─────────────────────────────
    render_divider()
    render_section_header("🛠", "Technology Stack")

    techs = [
        ("🐍", "Python", "Core"),
        ("🌊", "Streamlit", "UI"),
        ("🤖", "Scikit-learn", "ML"),
        ("📄", "ReportLab", "PDF"),
        ("🧠", "NLP", "Analysis"),
        ("🌲", "Random Forest", "Model"),
    ]

    tech_cols = st.columns(6)
    for col, (icon, name, role) in zip(tech_cols, techs):
        with col:
            st.markdown(
                f"""
                <div class="tech-card">
                    <div class="tech-card__icon">{icon}</div>
                    <div class="tech-card__name">{name}</div>
                    <div class="tech-card__role">{role}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ── Footer ───────────────────────────────────────
    st.markdown(
        """
        <div class="app-footer">
            <div class="app-footer__text">
                JudgeAI v2.0 Pro &nbsp;·&nbsp; AI Powered Legal Intelligence Platform &nbsp;·&nbsp; © 2026
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )