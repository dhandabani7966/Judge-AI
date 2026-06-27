import streamlit as st

from frontend.components.hero import render_hero
from frontend.components.cards import render_stat_card
from frontend.components.sections import render_section_header, render_divider
from frontend.components.badges import render_badge
from frontend.components.timeline import render_pipeline_step


def show_dashboard():

    # ── Header ───────────────────────────────────────
    render_hero(
        badge_text="📊 Platform Overview",
        title="JudgeAI Dashboard",
        description="Real-time platform statistics and AI processing pipeline overview.",
        compact=True,
    )

    # ── Top Metrics ──────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_stat_card("⚖", "Cases Analyzed", "42,342", "+126 Today", "blue")
    with c2:
        render_stat_card("🎯", "Accuracy", "82.47%", "+1.3%", "gold")
    with c3:
        render_stat_card("🤖", "ML Model", "Random Forest", "", "cyan")
    with c4:
        render_stat_card("⚡", "Avg Processing", "2.8 sec", "-0.2 sec", "green")

    render_divider()

    # ── Pipeline + Features ──────────────────────────
    left, right = st.columns([3, 2], gap="large")

    with left:
        render_section_header("⚡", "AI Processing Pipeline")

        pipeline_steps = [
            ("📂", "Upload Legal Document"),
            ("📖", "Extract Text from File"),
            ("🧹", "Clean & Preprocess"),
            ("📝", "Generate AI Summary"),
            ("⚖", "Extract Legal Information"),
            ("🤖", "Predict Case Outcome"),
            ("📄", "Generate Professional Report"),
        ]

        for i, (icon, label) in enumerate(pipeline_steps):
            render_pipeline_step(icon, label, "done", step_num=i + 1)

    with right:
        render_section_header("🚀", "Platform Features")

        features = [
            ("📄", "PDF Support", "gold"),
            ("📝", "DOCX Support", "gold"),
            ("📃", "TXT Support", "gold"),
            ("📊", "CSV Support", "gold"),
            ("🤖", "AI Summary", "blue"),
            ("⚖", "ML Prediction", "blue"),
            ("📈", "Confidence Score", "blue"),
            ("📄", "PDF Report Export", "blue"),
        ]

        for icon, label, color in features:
            badge_html = render_badge("Active", color)
            st.markdown(
                f"""
                <div class="feature-row">
                    <span class="feature-row__icon">{icon}</span>
                    <span class="feature-row__label">{label}</span>
                    <span style="margin-left:auto;">{badge_html}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_divider()

    # ── Prediction Distribution ──────────────────────
    render_section_header("📈", "Analytics")

    chart_left, chart_right = st.columns(2, gap="large")

    with chart_left:
        st.markdown(
            """
            <div class="chart-container">
                <div style="font-size:13px;font-weight:700;color:var(--text-primary);margin-bottom:16px;text-transform:uppercase;letter-spacing:0.5px;">
                    Prediction Distribution
                </div>
            """,
            unsafe_allow_html=True,
        )

        # CSS-only horizontal bar chart
        st.markdown(
            """
                <div style="margin-bottom:12px;">
                    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                        <span style="font-size:12px;color:var(--text-secondary);">Accepted</span>
                        <span style="font-size:12px;font-weight:600;color:var(--success);">58%</span>
                    </div>
                    <div style="height:8px;background:rgba(255,255,255,0.05);border-radius:999px;overflow:hidden;">
                        <div style="height:100%;width:58%;background:linear-gradient(90deg,#1E40AF,#4ADE80);border-radius:999px;transition:width 1s ease;"></div>
                    </div>
                </div>
                <div style="margin-bottom:12px;">
                    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                        <span style="font-size:12px;color:var(--text-secondary);">Rejected</span>
                        <span style="font-size:12px;font-weight:600;color:var(--error);">32%</span>
                    </div>
                    <div style="height:8px;background:rgba(255,255,255,0.05);border-radius:999px;overflow:hidden;">
                        <div style="height:100%;width:32%;background:linear-gradient(90deg,#1E40AF,#F87171);border-radius:999px;transition:width 1s ease;"></div>
                    </div>
                </div>
                <div>
                    <div style="display:flex;justify-content:space-between;margin-bottom:4px;">
                        <span style="font-size:12px;color:var(--text-secondary);">Other</span>
                        <span style="font-size:12px;font-weight:600;color:var(--warning);">10%</span>
                    </div>
                    <div style="height:8px;background:rgba(255,255,255,0.05);border-radius:999px;overflow:hidden;">
                        <div style="height:100%;width:10%;background:linear-gradient(90deg,#1E40AF,#FBBF24);border-radius:999px;transition:width 1s ease;"></div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with chart_right:
        st.markdown(
            """
            <div class="chart-container">
                <div style="font-size:13px;font-weight:700;color:var(--text-primary);margin-bottom:16px;text-transform:uppercase;letter-spacing:0.5px;">
                    Recent Activity
                </div>
            """,
            unsafe_allow_html=True,
        )

        activities = [
            ("#4ADE80", "Document analyzed — Civil Appeal", "2 min ago"),
            ("#3B82F6", "PDF report generated", "5 min ago"),
            ("#D4AF37", "ML prediction: Accepted (87.3%)", "12 min ago"),
            ("#60A5FA", "New document uploaded", "18 min ago"),
            ("#4ADE80", "Analysis completed successfully", "25 min ago"),
        ]

        for color, text, time in activities:
            st.markdown(
                f"""
                <div class="activity-item">
                    <div class="activity-dot" style="background:{color};"></div>
                    <div>
                        <div class="activity-text">{text}</div>
                        <div class="activity-time">{time}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    render_divider()

    # ── Bottom Stats ─────────────────────────────────
    render_section_header("📊", "Platform Statistics")

    a, b, c = st.columns(3)
    with a:
        render_stat_card("📄", "Reports Generated", "1,254", "+18 Today", "blue")
    with b:
        render_stat_card("🧠", "Predictions Made", "18,946", "+94 Today", "gold")
    with c:
        render_stat_card("📂", "Documents Processed", "42,342", "+126 Today", "green")