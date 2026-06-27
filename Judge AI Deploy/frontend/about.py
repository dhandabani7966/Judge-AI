import streamlit as st

from frontend.components.hero import render_hero
from frontend.components.cards import render_glass_card
from frontend.components.sections import render_section_header, render_divider
from frontend.components.badges import render_badge


def show_about():

    # ── Header ───────────────────────────────────────
    render_hero(
        badge_text="ℹ️ About the Platform",
        title="About JudgeAI",
        description=(
            "An AI-powered Legal Intelligence Platform built to analyze court judgments "
            "quickly, accurately, and professionally — designed for students, researchers, "
            "and legal professionals."
        ),
    )

    # ── Mission & Vision ─────────────────────────────
    render_section_header("🎯", "Mission & Vision")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="result-section" style="border-left:3px solid var(--accent-blue);">
                <div class="result-section__header">
                    <span class="result-section__icon">🎯</span>
                    <span class="result-section__title">Mission</span>
                </div>
                <div class="result-section__body">
                    Democratize legal intelligence by making AI-powered judgment analysis
                    accessible to everyone — from law students to seasoned practitioners.
                    We believe technology should simplify legal research, not complicate it.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="result-section" style="border-left:3px solid var(--accent-gold);">
                <div class="result-section__header">
                    <span class="result-section__icon">🔭</span>
                    <span class="result-section__title">Vision</span>
                </div>
                <div class="result-section__body">
                    Build the most comprehensive AI legal assistant that can analyze,
                    summarize, and predict outcomes of any court judgment across jurisdictions
                    with unprecedented accuracy and speed.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_divider()

    # ── Features ─────────────────────────────────────
    render_section_header("🚀", "Features")

    features = [
        ("📂", "Multi-Format Support", "Accepts PDF, DOCX, TXT and CSV — up to 5 GB per file.", "blue"),
        ("⚖", "Legal Metadata Extraction", "Automatically pulls court, bench, acts, sections, and case numbers.", "gold"),
        ("📝", "AI Generated Summary", "NLP-powered summarization of lengthy legal judgments.", "blue"),
        ("🤖", "ML Outcome Prediction", "Random Forest model trained on the Jud-IPL legal dataset.", "gold"),
        ("📊", "Confidence Scoring", "Quantified prediction confidence displayed with a live gauge.", "blue"),
        ("📄", "Professional PDF Report", "One-click export of the full analysis as a formatted PDF.", "gold"),
    ]

    c1, c2 = st.columns(2)
    for i, (icon, title, desc, accent) in enumerate(features):
        col = c1 if i % 2 == 0 else c2
        with col:
            render_glass_card(icon, title, desc, accent)

    render_divider()

    # ── Technology Stack ─────────────────────────────
    render_section_header("🛠", "Technology Stack")

    techs = [
        ("🐍", "Python", "Core Language"),
        ("🌊", "Streamlit", "UI Framework"),
        ("🤖", "Scikit-learn", "ML Model"),
        ("📄", "ReportLab", "PDF Generation"),
        ("🧠", "NLP", "Text Analysis"),
        ("🌲", "Random Forest", "Prediction"),
    ]

    cols = st.columns(6)
    for col, (icon, name, role) in zip(cols, techs):
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

    render_divider()

    # ── Architecture ─────────────────────────────────
    render_section_header("🏗", "Architecture")

    st.markdown(
        """
        <div class="result-section" style="padding:28px;">
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center;">
                <div>
                    <div style="font-size:28px;margin-bottom:8px;">📂</div>
                    <div style="font-size:12px;font-weight:600;color:var(--text-primary);">Document Input</div>
                    <div style="font-size:11px;color:var(--text-muted);">PDF · DOCX · TXT · CSV</div>
                </div>
                <div>
                    <div style="font-size:28px;margin-bottom:8px;">⚙</div>
                    <div style="font-size:12px;font-weight:600;color:var(--text-primary);">Processing</div>
                    <div style="font-size:11px;color:var(--text-muted);">Extract · Clean · Parse</div>
                </div>
                <div>
                    <div style="font-size:28px;margin-bottom:8px;">🧠</div>
                    <div style="font-size:12px;font-weight:600;color:var(--text-primary);">AI Engine</div>
                    <div style="font-size:11px;color:var(--text-muted);">NLP · ML · Prediction</div>
                </div>
                <div>
                    <div style="font-size:28px;margin-bottom:8px;">📄</div>
                    <div style="font-size:12px;font-weight:600;color:var(--text-primary);">Output</div>
                    <div style="font-size:11px;color:var(--text-muted);">Report · Summary · PDF</div>
                </div>
            </div>
            <div style="display:flex;justify-content:center;gap:0;margin-top:12px;">
                <div style="flex:1;height:2px;background:linear-gradient(90deg,transparent,var(--accent-blue),var(--accent-gold),var(--accent-blue),transparent);border-radius:999px;"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_divider()

    # ── Roadmap ──────────────────────────────────────
    render_section_header("🗺", "Roadmap")

    roadmap = [
        ("var(--success)", "v1.0", "Core Platform", "Document analysis, ML prediction, PDF export — Completed"),
        ("var(--accent-blue)", "v2.0", "Premium UI Redesign", "Glassmorphism design, component library, responsive layouts — Current"),
        ("var(--accent-gold)", "v2.5", "Multi-Language Support", "Hindi, Tamil, Bengali, and other Indian language judgments"),
        ("var(--text-muted)", "v3.0", "Advanced Analytics", "Deep learning models, case similarity search, citation graph"),
    ]

    for color, version, title, desc in roadmap:
        st.markdown(
            f"""
            <div class="roadmap-item">
                <div class="roadmap-marker" style="background:{color};"></div>
                <div class="roadmap-content">
                    <div class="roadmap-version">{version}</div>
                    <div class="roadmap-title">{title}</div>
                    <div class="roadmap-desc">{desc}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_divider()

    # ── Developer ────────────────────────────────────
    render_section_header("👨‍💻", "Developer")

    st.markdown(
        f"""
        <div class="dev-card">
            <div class="dev-card__avatar">D</div>
            <div>
                <div class="dev-card__name">Dhandabani M</div>
                <div class="dev-card__title">
                    B.Tech CSE (AI &amp; ML) &nbsp;·&nbsp; Kangeyam Institute of Technology
                </div>
                <div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;">
                    {render_badge("IEEE Educational Society", "gold")}
                    {render_badge("ML Engineer", "blue")}
                    {render_badge("AI Developer", "blue")}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Footer ───────────────────────────────────────
    st.markdown(
        """
        <div class="app-footer">
            <div class="app-footer__text">
                JudgeAI v2.0 Pro &nbsp;·&nbsp; AI Powered Legal Intelligence Platform &nbsp;·&nbsp; MIT License
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )