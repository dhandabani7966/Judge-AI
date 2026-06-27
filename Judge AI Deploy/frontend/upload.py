import streamlit as st

from frontend.components.hero import render_hero
from frontend.components.sections import render_section_header, render_divider
from frontend.components.badges import render_badge


def show_upload():

    # ── Page Header ──────────────────────────────────
    render_hero(
        badge_text="📂 Document Intake",
        title="Upload Legal Document",
        description=(
            "Upload your legal judgment and JudgeAI will automatically "
            "summarize it, extract key legal information, predict the outcome, "
            "and generate a professional downloadable report."
        ),
        compact=True,
    )

    # ── Upload Zone ──────────────────────────────────
    st.markdown(
        f"""
        <div class="upload-zone">
            <div class="upload-zone__icon">📂</div>
            <h2>Drop your legal document here</h2>
            <p>PDF, DOCX, TXT or CSV &nbsp;·&nbsp; Up to 5 GB per file</p>
            <div class="badge-row" style="justify-content:center;margin-top:16px;">
                {render_badge("📄 PDF", "gold")}
                {render_badge("📝 DOCX", "gold")}
                {render_badge("📃 TXT", "gold")}
                {render_badge("📊 CSV", "gold")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded_file = st.file_uploader(
        "Choose a Legal Document",
        type=["pdf", "docx", "txt", "csv"],
        help="Supported: PDF, DOCX, TXT, CSV — max 5 GB",
        label_visibility="collapsed",
    )

    # ── File Preview ──
    if uploaded_file is not None:
        file_size = uploaded_file.size
        if file_size < 1024:
            size_str = f"{file_size} B"
        elif file_size < 1024 * 1024:
            size_str = f"{file_size / 1024:.1f} KB"
        else:
            size_str = f"{file_size / (1024 * 1024):.1f} MB"

        ext = uploaded_file.name.split(".")[-1].upper()

        st.markdown(
            f"""
            <div class="info-card" style="margin-top:8px;">
                <div class="info-card__accent" style="background:var(--success);"></div>
                <div class="info-card__content" style="display:flex;align-items:center;gap:12px;width:100%;">
                    <span style="font-size:20px;">📄</span>
                    <div style="flex:1;">
                        <div class="info-card__label" style="color:var(--success);">File Uploaded</div>
                        <div class="info-card__value">{uploaded_file.name}</div>
                    </div>
                    <div style="display:flex;gap:6px;">
                        {render_badge(ext, "gold")}
                        {render_badge(size_str, "blue")}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_divider()

    # ── Paste Text ───────────────────────────────────
    st.markdown(
        f"""
        <div style="margin-bottom:14px;">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
                <span style="font-size:17px;font-weight:700;color:var(--text-primary);">
                    📝 Or Paste Judgment Text
                </span>
                {render_badge("Plain text", "blue")}
            </div>
            <p style="font-size:13px;color:var(--text-muted);margin:0;">
                Works with any court judgment copied directly from a browser or document.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    judgment_text = st.text_area(
        "Judgment Text",
        height=220,
        placeholder="Paste the complete legal judgment text here...",
        label_visibility="collapsed",
    )

    # ── Word / Character Counter ──
    if judgment_text.strip():
        word_count = len(judgment_text.split())
        char_count = len(judgment_text)
        st.markdown(
            f"""
            <div style="display:flex;gap:16px;margin-top:4px;">
                <span style="font-size:12px;color:var(--text-muted);">
                    {word_count:,} words
                </span>
                <span style="font-size:12px;color:var(--text-muted);">
                    {char_count:,} characters
                </span>
                <span style="font-size:12px;color:var(--accent-blue);">
                    ~{max(1, word_count // 200)} min read
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Analyze Button ───────────────────────────────
    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:
        analyze = st.button(
            "⚖ Analyze Document",
            type="primary",
            use_container_width=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Tips Expander ────────────────────────────────
    with st.expander("💡 Tips for best results"):
        tips = [
            "Upload clear, text-selectable PDFs for best extraction accuracy.",
            "Scanned image PDFs may have lower accuracy — use DOCX or TXT if available.",
            "Include the complete judgment for accurate legal metadata extraction.",
            "ML prediction confidence improves with full judgment text, not excerpts.",
            "Download the PDF report to share analysis results professionally.",
            "Average processing time is under 3 seconds for standard judgments.",
        ]

        tip_html = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:4px 0;">'
        for tip in tips:
            tip_html += f"""
            <div style="display:flex;gap:10px;align-items:flex-start;">
                <span style="color:var(--accent-blue);font-size:14px;flex-shrink:0;">✦</span>
                <span style="color:var(--text-secondary);font-size:13px;line-height:1.5;">{tip}</span>
            </div>
            """
        tip_html += "</div>"

        st.markdown(tip_html, unsafe_allow_html=True)

    return uploaded_file, judgment_text, analyze