import streamlit as st
from datetime import datetime
import textwrap

from frontend.styles import load_css
from frontend.home import show_home
from frontend.dashboard import show_dashboard
from frontend.upload import show_upload
from frontend.result import show_result
from frontend.about import show_about
from frontend.history import show_history
from frontend.settings import show_settings

from utils.file_handler import extract_text
from utils.summary import generate_summary
from utils.legal_analyzer import analyze_judgment
from utils.predictor import predict_case


# ─────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────

st.set_page_config(
    page_title="JudgeAI — AI Legal Intelligence",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────
# LOAD CSS
# ─────────────────────────────────────────────────────────

load_css()

# ─────────────────────────────────────────────────────────
# SESSION STATE DEFAULTS
# ─────────────────────────────────────────────────────────

if "analysis_history" not in st.session_state:
    st.session_state.analysis_history = []

if "selected_history_item" not in st.session_state:
    st.session_state.selected_history_item = None

if "total_analyses" not in st.session_state:
    st.session_state.total_analyses = 0


# ─────────────────────────────────────────────────────────
# PREMIUM SIDEBAR
# ─────────────────────────────────────────────────────────

st.sidebar.markdown(
    textwrap.dedent("""
    <div style="padding:4px 12px 20px;">
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;">
    <div style="width:40px;height:40px;background:linear-gradient(135deg,#1E40AF 0%,#3B82F6 100%);border-radius:10px;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 16px rgba(59,130,246,0.3);font-size:20px;flex-shrink:0;">⚖️</div>
    <div>
    <div style="font-size:18px;font-weight:800;color:var(--text-primary);letter-spacing:-0.3px;line-height:1.1;">JudgeAI</div>
    <div style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent-gold);">v2.0 Pro · AI Legal</div>
    </div>
    </div>
    </div>
    <div style="height:1px;background:linear-gradient(90deg,var(--accent-blue),transparent);opacity:0.3;margin:10px 0 16px;"></div>
    <div style="font-size:9px;font-weight:700;text-transform:uppercase;letter-spacing:1.8px;color:var(--text-muted);margin-bottom:8px;padding-left:2px;">Navigation</div>
    </div>
    """)
    , unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📂 Analyze",
        "📊 Dashboard",
        "📋 History",
        "⚙️ Settings",
        "ℹ️ About",
    ],
    label_visibility="collapsed",
)

# ── Sidebar Footer ──
history_count = len(st.session_state.analysis_history)

st.sidebar.markdown(
f"""<div style="padding:0 12px;">
<div style="height:1px;background:linear-gradient(90deg,var(--accent-blue),transparent);opacity:0.15;margin:16px 0;"></div>
<!-- AI Status -->
<div style="display:flex;align-items:center;gap:8px;background:rgba(74,222,128,0.06);border:1px solid rgba(74,222,128,0.15);border-radius:8px;padding:8px 12px;margin-bottom:10px;">
<div style="width:7px;height:7px;border-radius:50%;background:var(--success);box-shadow:0 0 8px rgba(74,222,128,0.6);animation:pulse 2s infinite;flex-shrink:0;"></div>
<span style="font-size:12px;font-weight:600;color:var(--success);">AI System Online</span>
</div>
<!-- Session Info -->
<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:10px 12px;margin-bottom:10px;">
<div style="font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:1px;color:var(--text-muted);margin-bottom:6px;">Session</div>
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
<span style="font-size:12px;color:var(--text-secondary);">Analyses Run</span>
<span style="font-size:12px;font-weight:700;color:var(--text-primary);">{history_count}</span>
</div>
<div style="display:flex;justify-content:space-between;align-items:center;">
<span style="font-size:12px;color:var(--text-secondary);">Model</span>
<span style="font-size:12px;font-weight:700;color:var(--accent-electric);">Random Forest</span>
</div>
</div>
<!-- System Health Bar -->
<div style="margin-bottom:6px;">
<div style="display:flex;justify-content:space-between;margin-bottom:4px;">
<span style="font-size:10px;color:var(--text-muted);">System Health</span>
<span style="font-size:10px;color:var(--success);">Optimal</span>
</div>
<div style="height:3px;background:var(--border);border-radius:2px;overflow:hidden;">
<div style="height:100%;width:94%;background:linear-gradient(90deg,var(--accent-blue),var(--success));border-radius:2px;"></div>
</div>
</div>
<div style="font-size:10px;color:var(--text-muted);text-align:center;margin-top:12px;">
JudgeAI v2.0 · Jud-IPL Dataset · 82.47% Accuracy
</div>
</div>""",
    unsafe_allow_html=True,
)


# ─────────────────────────────────────────────────────────
# ANALYSIS PIPELINE HELPER
# ─────────────────────────────────────────────────────────

PIPELINE_STEPS = [
    ("📄", "Reading Document"),
    ("📖", "Extracting Text"),
    ("🧹", "Cleaning Data"),
    ("📝", "Generating AI Summary"),
    ("⚖️", "Extracting Legal Information"),
    ("🤖", "Running ML Prediction"),
    ("📊", "Preparing Report"),
    ("✅", "Analysis Complete"),
]


def _render_pipeline_html(current_step):
    """Render a vertical analysis timeline as pure HTML (no Streamlit per-step)."""
    items_html = ""
    for i, (icon, label) in enumerate(PIPELINE_STEPS):
        if i < current_step:
            state_color = "#4ADE80"
            status_icon = "✓"
            label_color = "#94A3B8"
            connector_color = "rgba(74,222,128,0.3)"
        elif i == current_step:
            state_color = "#3B82F6"
            status_icon = "●"
            label_color = "#F1F5F9"
            connector_color = "rgba(255,255,255,0.06)"
        else:
            state_color = "#334155"
            status_icon = ""
            label_color = "#475569"
            connector_color = "rgba(255,255,255,0.04)"

        connector_html = ""
        if i < len(PIPELINE_STEPS) - 1:
            connector_html = f"""
            <div style="
                width:2px;height:24px;
                background:{connector_color};
                margin:0 auto;margin-left:17px;
            "></div>"""

        dot_inner = f'<span style="font-size:11px;color:{state_color};">{status_icon}</span>' if status_icon else ""

        items_html += f"""
        <div style="display:flex;align-items:center;gap:12px;">
            <div style="
                width:36px;height:36px;border-radius:50%;flex-shrink:0;
                background:{"rgba(59,130,246,0.12)" if i == current_step else ("rgba(74,222,128,0.08)" if i < current_step else "rgba(255,255,255,0.03)")};
                border:1.5px solid {state_color};
                display:flex;align-items:center;justify-content:center;
                font-size:16px;
            ">{icon if i >= current_step else dot_inner}</div>
            <div style="flex:1;">
                <div style="font-size:13px;font-weight:{"600" if i == current_step else "500"};color:{label_color};">{label}</div>
            </div>
            <div style="font-size:11px;color:{state_color};font-weight:700;">
                {"Done" if i < current_step else ("Running..." if i == current_step else "")}
            </div>
        </div>
        {connector_html}
        """

    return f"""
    <div style="
        background:rgba(255,255,255,0.025);
        border:1px solid rgba(255,255,255,0.06);
        border-radius:16px;
        padding:24px 28px;
        margin:16px 0;
    ">
        <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1.5px;color:#475569;margin-bottom:20px;">
            🔄 Analysis Pipeline
        </div>
        {items_html}
    </div>
    """


# ─────────────────────────────────────────────────────────
# PAGE ROUTING
# ─────────────────────────────────────────────────────────

# ── Home ──
if page == "🏠 Home":
    show_home()

# ── Dashboard ──
elif page == "📊 Dashboard":
    show_dashboard()

# ── About ──
elif page == "ℹ️ About":
    show_about()

# ── History ──
elif page == "📋 History":
    show_history()

# ── Settings ──
elif page == "⚙️ Settings":
    show_settings()

# ── Analyze ──
elif page == "📂 Analyze":

    uploaded_pdf, judgment_text, analyze = show_upload()

    if analyze:

        if uploaded_pdf is None and (not judgment_text or judgment_text.strip() == ""):
            st.error("Please upload a legal document or paste judgment text to analyze.")

        else:

            # ── Animated Pipeline Timeline ──
            pipeline_placeholder = st.empty()

            def update_pipeline(step):
                pipeline_placeholder.markdown(
                    _render_pipeline_html(step),
                    unsafe_allow_html=True,
                )

            # Step 0 — Reading Document
            update_pipeline(0)
            input_text = (
                extract_text(uploaded_pdf)
                if uploaded_pdf is not None
                else judgment_text
            )

            # Step 1 — Extracting Text
            update_pipeline(1)

            # Step 2 — Cleaning Data
            update_pipeline(2)

            # Step 3 — Generating AI Summary
            update_pipeline(3)
            summary = generate_summary(input_text)

            # Step 4 — Extracting Legal Information
            update_pipeline(4)
            legal_info = analyze_judgment(input_text)

            # Step 5 — Running ML Prediction
            update_pipeline(5)
            prediction, confidence = predict_case(input_text)

            # Step 6 — Preparing Report
            update_pipeline(6)

            # Step 7 — Complete (show full done state)
            update_pipeline(7)

            # ── Save to History ──
            doc_name = (
                uploaded_pdf.name
                if uploaded_pdf is not None
                else "Pasted Text"
            )
            st.session_state.analysis_history.append({
                "name": doc_name,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "prediction": prediction,
                "confidence": confidence,
                "court": legal_info.get("court", "Unknown Court"),
                "legal_info": legal_info,
                "summary": summary,
            })
            st.session_state.total_analyses += 1

            # ── Clear pipeline after a moment & show results ──
            pipeline_placeholder.empty()

            # ── Show Result ──
            show_result(
                legal_info,
                summary,
                prediction,
                confidence,
            )