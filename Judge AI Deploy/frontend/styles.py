import streamlit as st


def load_css():
    st.markdown(
        """
    <style>

    /* ═══════════════════════════════════════════════════
       JUDGEAI v2.0 — PREMIUM DESIGN SYSTEM
       ═══════════════════════════════════════════════════ */

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&display=swap');

    /* ─── CSS Custom Properties ────────────────────────── */
    :root {
        --bg-primary:    #060B18;
        --bg-surface:    #0C1222;
        --bg-card:       rgba(255,255,255,0.025);
        --bg-card-hover: rgba(255,255,255,0.045);
        --border:        rgba(255,255,255,0.06);
        --border-hover:  rgba(255,255,255,0.12);
        --accent-gold:   #D4AF37;
        --accent-blue:   #3B82F6;
        --accent-electric: #60A5FA;
        --accent-royal:  #1E40AF;
        --text-primary:  #F1F5F9;
        --text-secondary:#94A3B8;
        --text-muted:    #475569;
        --success:       #4ADE80;
        --error:         #F87171;
        --warning:       #FBBF24;
        --info:          #38BDF8;
        --radius-sm:     8px;
        --radius-md:     14px;
        --radius-lg:     20px;
        --radius-xl:     24px;
        --shadow-card:   0 4px 24px rgba(0,0,0,0.4);
        --shadow-elevated: 0 20px 48px rgba(0,0,0,0.5);
        --transition:    all 0.3s cubic-bezier(0.4,0,0.2,1);
        --font-sans:     'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-display:  'Playfair Display', Georgia, serif;
    }

    /* ─── Reset & Base ─────────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header[data-testid="stHeader"] {
        background: rgba(6,11,24,0.8) !important;
        backdrop-filter: blur(12px) !important;
        border-bottom: 1px solid var(--border) !important;
    }

    .stApp {
        background: var(--bg-primary);
        color: var(--text-secondary);
        font-family: var(--font-sans);
    }

    /* Animated mesh background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background:
            radial-gradient(ellipse at 20% 20%, rgba(59,130,246,0.06) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(212,175,55,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 50% 50%, rgba(96,165,250,0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
        animation: meshShift 20s ease-in-out infinite alternate;
    }

    @keyframes meshShift {
        0%   { opacity: 0.6; }
        50%  { opacity: 1; }
        100% { opacity: 0.6; }
    }

    /* ─── Keyframe Animations ──────────────────────────── */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }

    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-16px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(16px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50%      { opacity: 0.5; }
    }

    @keyframes shimmer {
        0%   { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }

    @keyframes glow {
        0%, 100% { box-shadow: 0 0 8px rgba(212,175,55,0.2); }
        50%      { box-shadow: 0 0 20px rgba(212,175,55,0.4); }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50%      { transform: translateY(-8px); }
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }

    @keyframes borderGlow {
        0%, 100% { border-color: rgba(212,175,55,0.15); }
        50%      { border-color: rgba(59,130,246,0.3); }
    }

    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.92); }
        to   { opacity: 1; transform: scale(1); }
    }

    @keyframes dotPulse {
        0%, 80%, 100% { transform: scale(0); opacity: 0.4; }
        40% { transform: scale(1); opacity: 1; }
    }

    /* ─── Sidebar ──────────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0A1128 0%, #0D1525 100%) !important;
        border-right: 1px solid rgba(59,130,246,0.1) !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem !important;
    }

    /* Sidebar Radio Navigation */
    [data-testid="stSidebar"] .stRadio > div {
        gap: 2px !important;
    }

    [data-testid="stSidebar"] .stRadio > label {
        font-size: 10px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px !important;
        color: var(--text-muted) !important;
        margin-bottom: 8px !important;
        padding-left: 4px !important;
    }

    [data-testid="stSidebar"] .stRadio label {
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        color: var(--text-secondary) !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
        padding: 10px 14px !important;
        border-radius: var(--radius-sm) !important;
        border: 1px solid transparent !important;
        transition: var(--transition) !important;
        cursor: pointer !important;
        position: relative !important;
        margin-left: 2px !important;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        color: var(--text-primary) !important;
        background: rgba(59,130,246,0.06) !important;
        border-color: rgba(59,130,246,0.12) !important;
    }

    [data-testid="stSidebar"] .stRadio label[data-checked="true"],
    [data-testid="stSidebar"] .stRadio label:has(input:checked) {
        color: var(--accent-electric) !important;
        background: rgba(59,130,246,0.08) !important;
        border-color: rgba(59,130,246,0.2) !important;
        font-weight: 600 !important;
        border-left: 3px solid var(--accent-blue) !important;
        padding-left: 11px !important;
    }

    [data-testid="stSidebar"] .stRadio input[type="radio"] {
        accent-color: var(--accent-blue) !important;
        width: 14px !important;
        height: 14px !important;
        flex-shrink: 0 !important;
    }

    /* Sidebar Title */
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] .stMarkdown h1 {
        font-size: 20px !important;
        font-weight: 800 !important;
        color: var(--text-primary) !important;
        font-family: var(--font-sans) !important;
        letter-spacing: -0.3px !important;
    }

    [data-testid="stSidebar"] .stCaption {
        color: var(--text-muted) !important;
        font-size: 11px !important;
    }

    /* Sidebar Status Pills */
    [data-testid="stSidebar"] .stSuccess {
        background: rgba(74,222,128,0.06) !important;
        border: 1px solid rgba(74,222,128,0.15) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 12px !important;
    }

    [data-testid="stSidebar"] .stInfo {
        background: rgba(59,130,246,0.06) !important;
        border: 1px solid rgba(59,130,246,0.15) !important;
        border-radius: var(--radius-sm) !important;
        font-size: 12px !important;
        color: var(--accent-blue) !important;
    }

    /* ─── Hero Section ─────────────────────────────────── */
    .hero {
        background: linear-gradient(135deg,
            rgba(59,130,246,0.06) 0%,
            rgba(12,18,34,0.95) 40%,
            rgba(212,175,55,0.04) 100%);
        border: 1px solid rgba(59,130,246,0.12);
        border-radius: var(--radius-xl);
        padding: 52px 48px;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
        animation: fadeIn 0.6s ease;
    }

    .hero-orb {
        position: absolute;
        border-radius: 50%;
        pointer-events: none;
    }

    .hero-orb--1 {
        top: -80px; right: -80px;
        width: 300px; height: 300px;
        background: radial-gradient(circle, rgba(59,130,246,0.1) 0%, transparent 70%);
        animation: float 8s ease-in-out infinite;
    }

    .hero-orb--2 {
        bottom: -60px; left: -60px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, rgba(212,175,55,0.08) 0%, transparent 70%);
        animation: float 10s ease-in-out infinite reverse;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        border-radius: 999px;
        padding: 6px 16px;
        font-size: 11px;
        font-weight: 700;
        color: var(--accent-electric);
        letter-spacing: 1.2px;
        text-transform: uppercase;
        margin-bottom: 20px;
        animation: fadeInUp 0.5s ease 0.1s both;
    }

    .hero-title {
        font-family: var(--font-display) !important;
        font-size: 52px !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #D4AF37 0%, #F5E173 40%, #60A5FA 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        margin-bottom: 8px !important;
        line-height: 1.15 !important;
        animation: fadeInUp 0.5s ease 0.2s both;
    }

    .hero-subtitle {
        font-size: 18px;
        font-weight: 400;
        color: var(--accent-electric);
        letter-spacing: 0.5px;
        margin-bottom: 16px;
        animation: fadeInUp 0.5s ease 0.3s both;
    }

    .hero-description {
        font-size: 15px !important;
        color: var(--text-secondary) !important;
        line-height: 1.8 !important;
        max-width: 620px;
        animation: fadeInUp 0.5s ease 0.4s both;
    }

    /* ─── Glass Cards ──────────────────────────────────── */
    .glass-card {
        background: var(--bg-card);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 28px 24px;
        margin-bottom: 16px;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.5s ease both;
    }

    .glass-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg,
            transparent,
            rgba(59,130,246,0.2),
            rgba(212,175,55,0.2),
            transparent);
        opacity: 0.6;
    }

    .glass-card:hover {
        transform: translateY(-4px);
        border-color: rgba(59,130,246,0.2);
        box-shadow:
            0 16px 40px rgba(0,0,0,0.4),
            0 0 0 1px rgba(59,130,246,0.08);
        background: var(--bg-card-hover);
    }

    .glass-card__icon {
        width: 48px;
        height: 48px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
        border: 1px solid;
        margin-bottom: 16px;
        transition: var(--transition);
    }

    .glass-card:hover .glass-card__icon {
        transform: scale(1.08);
    }

    .glass-card__title {
        font-size: 16px !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
        margin-bottom: 8px !important;
    }

    .glass-card__desc {
        color: var(--text-secondary) !important;
        font-size: 13.5px !important;
        line-height: 1.7 !important;
    }

    /* ─── Info Cards (Result Page) ──────────────────────── */
    .info-card {
        display: flex;
        align-items: stretch;
        background: var(--bg-card);
        backdrop-filter: blur(8px);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        margin-bottom: 12px;
        transition: var(--transition);
        overflow: hidden;
        animation: fadeInUp 0.4s ease both;
    }

    .info-card:hover {
        border-color: var(--border-hover);
        transform: translateX(4px);
        background: var(--bg-card-hover);
    }

    .info-card__accent {
        width: 3px;
        flex-shrink: 0;
    }

    .info-card__content {
        padding: 16px 20px;
    }

    .info-card__label {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 6px;
    }

    .info-card__value {
        font-size: 14.5px;
        color: var(--text-primary);
        font-weight: 500;
        line-height: 1.5;
    }

    /* ─── Stat Cards ───────────────────────────────────── */
    .stat-card {
        background: var(--bg-card);
        backdrop-filter: blur(8px);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 24px 20px;
        text-align: center;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.5s ease both;
    }

    .stat-card:hover {
        transform: translateY(-4px);
        border-color: rgba(59,130,246,0.2);
        box-shadow: var(--shadow-card);
    }

    .stat-card__icon {
        font-size: 28px;
        margin-bottom: 10px;
    }

    .stat-card__label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-muted);
        margin-bottom: 6px;
    }

    .stat-card__value {
        font-size: 26px;
        font-weight: 800;
        color: var(--text-primary);
        letter-spacing: -0.5px;
    }

    .stat-card__delta {
        font-size: 12px;
        font-weight: 600;
        color: var(--success);
        margin-top: 4px;
    }

    .stat-card__glow {
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 120px;
        height: 60px;
        pointer-events: none;
        opacity: 0;
        transition: opacity 0.4s;
    }

    .stat-card:hover .stat-card__glow {
        opacity: 1;
    }

    /* ─── Metric Cards (Streamlit) ─────────────────────── */
    div[data-testid="stMetric"] {
        background: var(--bg-card) !important;
        backdrop-filter: blur(8px) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        padding: 22px 20px !important;
        transition: var(--transition) !important;
        position: relative;
        overflow: hidden;
    }

    div[data-testid="stMetric"]::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 2px;
        background: linear-gradient(90deg, var(--accent-blue), var(--accent-gold));
        opacity: 0;
        transition: opacity 0.3s;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(59,130,246,0.2) !important;
        box-shadow: var(--shadow-card) !important;
    }

    div[data-testid="stMetric"]:hover::after {
        opacity: 1;
    }

    div[data-testid="stMetricLabel"] {
        color: var(--text-muted) !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.8px !important;
    }

    div[data-testid="stMetricValue"] {
        color: var(--text-primary) !important;
        font-size: 26px !important;
        font-weight: 800 !important;
    }

    div[data-testid="stMetricDelta"] {
        color: var(--success) !important;
        font-size: 12px !important;
    }

    /* ─── Section Headers ──────────────────────────────── */
    .section-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin: 36px 0 20px;
        animation: fadeInUp 0.4s ease both;
    }

    .section-header__icon {
        font-size: 20px;
    }

    .section-header__title {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin: 0 !important;
        white-space: nowrap;
    }

    .section-header__line {
        flex: 1;
        height: 1px;
        background: linear-gradient(90deg,
            rgba(59,130,246,0.3),
            rgba(212,175,55,0.15),
            transparent);
    }

    /* ─── Badges ───────────────────────────────────────── */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 0.3px;
        transition: var(--transition);
    }

    .badge:hover {
        transform: translateY(-1px);
    }

    .badge-row {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        margin: 12px 0;
    }

    .badge-gold {
        background: rgba(212,175,55,0.12);
        border: 1px solid rgba(212,175,55,0.25);
        color: var(--accent-gold);
    }

    .badge-blue {
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.2);
        color: var(--accent-blue);
    }

    /* ─── Divider ──────────────────────────────────────── */
    hr,
    .premium-divider {
        border: 0 !important;
        height: 1px !important;
        background: linear-gradient(90deg,
            transparent,
            rgba(59,130,246,0.2),
            rgba(212,175,55,0.15),
            transparent) !important;
        margin: 32px 0 !important;
    }

    /* ─── Upload Zone ──────────────────────────────────── */
    .upload-zone {
        background: linear-gradient(135deg,
            rgba(59,130,246,0.03),
            rgba(212,175,55,0.03));
        border: 2px dashed rgba(59,130,246,0.2);
        border-radius: var(--radius-xl);
        padding: 48px 32px;
        text-align: center;
        margin-bottom: 24px;
        transition: var(--transition);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.5s ease both;
    }

    .upload-zone::before {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: var(--radius-xl);
        padding: 2px;
        background: linear-gradient(135deg,
            rgba(59,130,246,0.15),
            rgba(212,175,55,0.15));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0;
        transition: opacity 0.4s;
        pointer-events: none;
    }

    .upload-zone:hover {
        border-color: rgba(59,130,246,0.4);
        background: rgba(59,130,246,0.04);
    }

    .upload-zone:hover::before {
        opacity: 1;
    }

    .upload-zone__icon {
        font-size: 48px;
        margin-bottom: 16px;
        animation: float 4s ease-in-out infinite;
    }

    .upload-zone h2 {
        font-size: 20px !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        margin-bottom: 8px !important;
    }

    .upload-zone p {
        color: var(--text-muted) !important;
        font-size: 14px !important;
    }

    /* ─── File Uploader (Streamlit) ─────────────────────── */
    [data-testid="stFileUploader"] {
        border: 2px dashed rgba(59,130,246,0.2) !important;
        border-radius: var(--radius-lg) !important;
        background: rgba(59,130,246,0.02) !important;
        padding: 8px !important;
        transition: var(--transition) !important;
    }

    [data-testid="stFileUploader"]:hover {
        border-color: rgba(59,130,246,0.4) !important;
        background: rgba(59,130,246,0.04) !important;
    }

    /* ─── Text Area ────────────────────────────────────── */
    .stTextArea > div > div > textarea {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        font-size: 14px !important;
        font-family: var(--font-sans) !important;
        line-height: 1.7 !important;
        transition: border 0.3s, box-shadow 0.3s !important;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: rgba(59,130,246,0.4) !important;
        box-shadow: 0 0 0 3px rgba(59,130,246,0.08) !important;
    }

    /* ─── Buttons ──────────────────────────────────────── */
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #1E40AF, #3B82F6, #60A5FA) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: var(--radius-md) !important;
        padding: 14px 32px !important;
        font-weight: 700 !important;
        font-size: 14.5px !important;
        letter-spacing: 0.4px !important;
        transition: var(--transition) !important;
        box-shadow: 0 4px 16px rgba(59,130,246,0.3) !important;
        position: relative;
        overflow: hidden;
    }

    .stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(59,130,246,0.45) !important;
    }

    .stButton > button[kind="primary"]:active {
        transform: translateY(0) !important;
    }

    .stButton > button:not([kind="primary"]) {
        background: var(--bg-card) !important;
        color: var(--accent-electric) !important;
        border: 1px solid rgba(59,130,246,0.25) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        transition: var(--transition) !important;
    }

    .stButton > button:not([kind="primary"]):hover {
        background: rgba(59,130,246,0.06) !important;
        border-color: rgba(59,130,246,0.5) !important;
        transform: translateY(-1px) !important;
    }

    /* ─── Download Button ──────────────────────────────── */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #0F4C81, #1E6EB5) !important;
        color: white !important;
        border: 1px solid rgba(59,130,246,0.3) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        transition: var(--transition) !important;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(59,130,246,0.25) !important;
    }

    /* ─── Pipeline Steps ───────────────────────────────── */
    .pipeline-step {
        display: flex;
        align-items: center;
        gap: 14px;
        padding: 12px 16px;
        border-radius: var(--radius-sm);
        margin-bottom: 4px;
        border: 1px solid transparent;
        transition: var(--transition);
        animation: slideInLeft 0.4s ease both;
    }

    .pipeline-step:hover {
        transform: translateX(4px);
    }

    .pipeline-step--done {
        background: rgba(74,222,128,0.04);
        border-color: rgba(74,222,128,0.1);
    }

    .pipeline-step--active {
        background: rgba(59,130,246,0.06);
        border-color: rgba(59,130,246,0.15);
        animation: slideInLeft 0.4s ease both, borderGlow 2s ease infinite;
    }

    .pipeline-step--pending {
        opacity: 0.4;
    }

    .pipeline-step__indicator {
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .pipeline-step__num {
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: rgba(255,255,255,0.05);
        border: 1px solid var(--border);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 11px;
        font-weight: 700;
        color: var(--text-muted);
    }

    .pipeline-step--done .pipeline-step__num {
        background: rgba(74,222,128,0.15);
        border-color: rgba(74,222,128,0.3);
        color: var(--success);
    }

    .pipeline-step--active .pipeline-step__num {
        background: rgba(59,130,246,0.15);
        border-color: rgba(59,130,246,0.3);
        color: var(--accent-blue);
    }

    .pipeline-step__icon {
        font-size: 16px;
    }

    .pipeline-step__label {
        font-size: 13.5px;
        font-weight: 500;
        color: var(--text-secondary);
    }

    .pipeline-step--done .pipeline-step__label {
        color: var(--success);
    }

    .pipeline-step--active .pipeline-step__label {
        color: var(--accent-electric);
        font-weight: 600;
    }

    .pipeline-step__status {
        margin-left: auto;
    }

    .pipeline-step__check {
        color: var(--success);
        font-size: 14px;
        font-weight: 700;
    }

    .pipeline-step__loader {
        display: inline-flex;
        gap: 3px;
    }

    .pipeline-step__loader::before,
    .pipeline-step__loader::after {
        content: '';
        width: 5px;
        height: 5px;
        border-radius: 50%;
        background: var(--accent-blue);
    }

    .pipeline-step__loader::before {
        animation: dotPulse 1.2s infinite ease-in-out;
    }

    .pipeline-step__loader::after {
        animation: dotPulse 1.2s infinite ease-in-out 0.3s;
    }

    /* ─── Confidence Gauge ─────────────────────────────── */
    .confidence-gauge {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
    }

    .confidence-gauge__svg {
        transform: rotate(-90deg);
        width: 100%;
        height: 100%;
    }

    .confidence-gauge__track {
        fill: none;
        stroke: rgba(255,255,255,0.06);
        stroke-width: 8;
    }

    .confidence-gauge__fill {
        fill: none;
        stroke-width: 8;
        stroke-linecap: round;
        transition: stroke-dashoffset 1.5s cubic-bezier(0.4,0,0.2,1);
    }

    .confidence-gauge__text {
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .confidence-gauge__value {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    .confidence-gauge__label {
        font-size: 11px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    /* ─── Progress Ring ────────────────────────────────── */
    .progress-ring {
        position: relative;
        display: inline-flex;
    }

    /* ─── Expander ─────────────────────────────────────── */
    .streamlit-expanderHeader {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-secondary) !important;
        font-weight: 500 !important;
        transition: var(--transition) !important;
    }

    .streamlit-expanderHeader:hover {
        border-color: rgba(59,130,246,0.25) !important;
        color: var(--accent-electric) !important;
    }

    .streamlit-expanderContent {
        background: rgba(255,255,255,0.015) !important;
        border: 1px solid var(--border) !important;
        border-top: none !important;
        border-radius: 0 0 var(--radius-md) var(--radius-md) !important;
    }

    /* ─── Progress Bar ─────────────────────────────────── */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, var(--accent-royal), var(--accent-blue), var(--accent-electric)) !important;
        border-radius: 999px !important;
    }

    .stProgress > div > div {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 999px !important;
    }

    /* ─── Alerts ───────────────────────────────────────── */
    .stSuccess {
        background: rgba(74,222,128,0.06) !important;
        border: 1px solid rgba(74,222,128,0.15) !important;
        border-radius: var(--radius-md) !important;
        color: var(--success) !important;
    }

    .stInfo {
        background: rgba(59,130,246,0.06) !important;
        border: 1px solid rgba(59,130,246,0.15) !important;
        border-radius: var(--radius-md) !important;
        color: var(--accent-blue) !important;
    }

    .stError {
        background: rgba(248,113,113,0.06) !important;
        border: 1px solid rgba(248,113,113,0.15) !important;
        border-radius: var(--radius-md) !important;
    }

    .stWarning {
        background: rgba(251,191,36,0.06) !important;
        border: 1px solid rgba(251,191,36,0.15) !important;
        border-radius: var(--radius-md) !important;
    }

    /* ─── Typography ───────────────────────────────────── */
    h1 {
        color: var(--text-primary) !important;
        font-family: var(--font-display) !important;
        letter-spacing: -0.3px !important;
    }
    h2 {
        color: var(--text-primary) !important;
        font-weight: 700 !important;
    }
    h3 {
        color: var(--text-primary) !important;
        font-weight: 600 !important;
    }
    p {
        color: var(--text-secondary) !important;
    }

    /* ─── Tabs ─────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--bg-card);
        border-radius: var(--radius-md);
        padding: 4px;
        border: 1px solid var(--border);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm);
        color: var(--text-secondary);
        font-weight: 500;
        font-size: 13px;
        padding: 8px 16px;
        transition: var(--transition);
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-primary);
        background: rgba(59,130,246,0.06);
    }

    .stTabs [aria-selected="true"] {
        background: rgba(59,130,246,0.1) !important;
        color: var(--accent-electric) !important;
        font-weight: 600 !important;
    }

    .stTabs [data-baseweb="tab-highlight"] {
        background: var(--accent-blue) !important;
    }

    /* ─── Feature Row ──────────────────────────────────── */
    .feature-row {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px 16px;
        border-radius: var(--radius-sm);
        background: var(--bg-card);
        border: 1px solid var(--border);
        margin-bottom: 6px;
        transition: var(--transition);
        animation: slideInLeft 0.3s ease both;
    }

    .feature-row:hover {
        border-color: rgba(59,130,246,0.2);
        transform: translateX(4px);
        background: var(--bg-card-hover);
    }

    .feature-row__icon {
        font-size: 16px;
        flex-shrink: 0;
    }

    .feature-row__label {
        font-size: 13px;
        font-weight: 500;
        color: var(--text-primary);
        flex: 1;
    }

    /* ─── Step Cards (How it works) ─────────────────────── */
    .step-card {
        text-align: center;
        padding: 32px 20px;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        transition: var(--transition);
        animation: fadeInUp 0.5s ease both;
    }

    .step-card:hover {
        transform: translateY(-4px);
        border-color: rgba(59,130,246,0.2);
        box-shadow: var(--shadow-card);
    }

    .step-card__num {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        color: var(--accent-gold);
        margin-bottom: 6px;
    }

    .step-card__icon-wrap {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: rgba(59,130,246,0.08);
        border: 1px solid rgba(59,130,246,0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        margin: 0 auto 14px;
        transition: var(--transition);
    }

    .step-card:hover .step-card__icon-wrap {
        background: rgba(59,130,246,0.12);
        transform: scale(1.08);
    }

    /* ─── Result Section Cards ─────────────────────────── */
    .result-section {
        background: var(--bg-card);
        backdrop-filter: blur(8px);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 24px;
        margin-bottom: 20px;
        transition: var(--transition);
        animation: fadeInUp 0.5s ease both;
    }

    .result-section:hover {
        border-color: rgba(59,130,246,0.15);
        background: var(--bg-card-hover);
    }

    .result-section__header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
    }

    .result-section__icon {
        font-size: 18px;
    }

    .result-section__title {
        font-size: 15px;
        font-weight: 700;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .result-section__body {
        font-size: 14px;
        color: var(--text-secondary);
        line-height: 1.8;
    }

    /* ─── Prediction Card ──────────────────────────────── */
    .prediction-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        padding: 32px;
        text-align: center;
        transition: var(--transition);
        animation: scaleIn 0.5s ease both;
    }

    .prediction-card:hover {
        border-color: rgba(59,130,246,0.2);
        box-shadow: var(--shadow-card);
    }

    .prediction-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 24px;
        border-radius: 999px;
        font-size: 16px;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 16px;
    }

    .prediction-badge--accepted {
        background: rgba(74,222,128,0.12);
        border: 1px solid rgba(74,222,128,0.3);
        color: var(--success);
    }

    .prediction-badge--rejected {
        background: rgba(248,113,113,0.12);
        border: 1px solid rgba(248,113,113,0.3);
        color: var(--error);
    }

    .prediction-badge--neutral {
        background: rgba(251,191,36,0.12);
        border: 1px solid rgba(251,191,36,0.3);
        color: var(--warning);
    }

    /* ─── Download Section ─────────────────────────────── */
    .download-card {
        background: linear-gradient(135deg,
            rgba(59,130,246,0.06),
            rgba(212,175,55,0.04));
        border: 1px solid rgba(59,130,246,0.15);
        border-radius: var(--radius-xl);
        padding: 28px;
        text-align: center;
        margin-top: 12px;
        animation: fadeInUp 0.5s ease both;
    }

    /* ─── Tech Card ────────────────────────────────────── */
    .tech-card {
        text-align: center;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        padding: 20px 12px;
        transition: var(--transition);
    }

    .tech-card:hover {
        border-color: rgba(59,130,246,0.25);
        transform: translateY(-2px);
    }

    .tech-card__icon {
        font-size: 28px;
        margin-bottom: 8px;
    }

    .tech-card__name {
        font-size: 13px;
        font-weight: 600;
        color: var(--text-primary);
    }

    .tech-card__role {
        font-size: 11px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    /* ─── Developer Card ───────────────────────────────── */
    .dev-card {
        display: flex;
        align-items: center;
        gap: 24px;
        background: linear-gradient(135deg, rgba(59,130,246,0.04), rgba(212,175,55,0.03));
        border: 1px solid rgba(59,130,246,0.15);
        border-radius: var(--radius-xl);
        padding: 28px 32px;
        transition: var(--transition);
    }

    .dev-card:hover {
        border-color: rgba(59,130,246,0.3);
    }

    .dev-card__avatar {
        width: 64px;
        height: 64px;
        min-width: 64px;
        background: linear-gradient(135deg, var(--accent-blue), var(--accent-electric));
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        font-weight: 800;
        color: #fff;
    }

    .dev-card__name {
        font-size: 20px;
        font-weight: 700;
        color: var(--text-primary);
    }

    .dev-card__title {
        font-size: 14px;
        color: var(--text-muted);
        margin-top: 3px;
    }

    /* ─── Empty State ──────────────────────────────────── */
    .empty-state {
        text-align: center;
        padding: 60px 20px;
        animation: fadeIn 0.6s ease;
    }

    .empty-state__icon {
        font-size: 56px;
        margin-bottom: 16px;
        opacity: 0.4;
    }

    .empty-state__title {
        font-size: 20px;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 8px;
    }

    .empty-state__desc {
        font-size: 14px;
        color: var(--text-muted);
        max-width: 400px;
        margin: 0 auto;
    }

    /* ─── History Item ─────────────────────────────────── */
    .history-item {
        display: flex;
        align-items: center;
        gap: 16px;
        padding: 16px 20px;
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        margin-bottom: 8px;
        transition: var(--transition);
        animation: slideInLeft 0.3s ease both;
    }

    .history-item:hover {
        border-color: rgba(59,130,246,0.2);
        background: var(--bg-card-hover);
        transform: translateX(4px);
    }

    .history-item__icon {
        font-size: 20px;
        width: 40px;
        height: 40px;
        border-radius: var(--radius-sm);
        background: rgba(59,130,246,0.08);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .history-item__info {
        flex: 1;
    }

    .history-item__name {
        font-size: 14px;
        font-weight: 600;
        color: var(--text-primary);
    }

    .history-item__meta {
        font-size: 12px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    /* ─── Settings ─────────────────────────────────────── */
    .settings-group {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 24px;
        margin-bottom: 16px;
    }

    .settings-group__title {
        font-size: 14px;
        font-weight: 700;
        color: var(--text-primary);
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 16px;
        padding-bottom: 12px;
        border-bottom: 1px solid var(--border);
    }

    /* ─── Footer ───────────────────────────────────────── */
    .app-footer {
        text-align: center;
        padding: 24px 16px;
        margin-top: 40px;
        border-top: 1px solid var(--border);
    }

    .app-footer__text {
        font-size: 12px;
        color: var(--text-muted);
        letter-spacing: 0.3px;
    }

    /* ─── Scrollbar ────────────────────────────────────── */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: var(--bg-primary); }
    ::-webkit-scrollbar-thumb {
        background: rgba(59,130,246,0.2);
        border-radius: 999px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(59,130,246,0.4);
    }

    /* ─── Responsive ───────────────────────────────────── */
    @media (max-width: 768px) {
        .hero { padding: 32px 24px !important; }
        .hero-title { font-size: 32px !important; }
        .hero-subtitle { font-size: 15px; }
        .dev-card { flex-direction: column; text-align: center; }
        .section-header { margin: 24px 0 14px; }
    }

    /* ─── Selectbox ────────────────────────────────────── */
    .stSelectbox > div > div {
        background: var(--bg-card) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
    }

    /* ─── Toggle ───────────────────────────────────────── */
    .stCheckbox > label > span {
        color: var(--text-secondary) !important;
    }

    /* ─── Analysis Timeline Container ──────────────────── */
    .analysis-timeline {
        padding: 8px 0;
    }

    .analysis-timeline .pipeline-step {
        position: relative;
    }

    .analysis-timeline .pipeline-step:not(:last-child)::after {
        content: '';
        position: absolute;
        left: 27px;
        bottom: -4px;
        width: 1px;
        height: 4px;
        background: var(--border);
    }

    .analysis-timeline .pipeline-step--done:not(:last-child)::after {
        background: rgba(74,222,128,0.2);
    }

    /* ─── Chart/Visualization containers ───────────────── */
    .chart-container {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 20px;
        margin-bottom: 16px;
    }

    /* ─── Activity feed ────────────────────────────────── */
    .activity-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        padding: 12px 0;
        border-bottom: 1px solid var(--border);
    }

    .activity-item:last-child {
        border-bottom: none;
    }

    .activity-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        flex-shrink: 0;
        margin-top: 6px;
    }

    .activity-text {
        font-size: 13px;
        color: var(--text-secondary);
        line-height: 1.5;
    }

    .activity-time {
        font-size: 11px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    /* ─── Roadmap ──────────────────────────────────────── */
    .roadmap-item {
        display: flex;
        gap: 16px;
        padding: 16px 0;
        border-bottom: 1px solid var(--border);
    }

    .roadmap-item:last-child {
        border-bottom: none;
    }

    .roadmap-marker {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        flex-shrink: 0;
        margin-top: 5px;
    }

    .roadmap-content {
        flex: 1;
    }

    .roadmap-title {
        font-size: 14px;
        font-weight: 600;
        color: var(--text-primary);
    }

    .roadmap-desc {
        font-size: 13px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    .roadmap-version {
        font-size: 11px;
        font-weight: 700;
        color: var(--accent-blue);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Dynamic styles based on settings
    theme = st.session_state.get("theme", "Dark")
    accent_color = st.session_state.get("accent_color", "Royal Blue")
    animations_enabled = st.session_state.get("animations_enabled", True)

    dynamic_css = ""

    light_vars = """
        --bg-primary:    #F8FAFC;
        --bg-surface:    #FFFFFF;
        --bg-card:       rgba(0,0,0,0.02);
        --bg-card-hover: rgba(0,0,0,0.04);
        --border:        rgba(0,0,0,0.1);
        --border-hover:  rgba(0,0,0,0.15);
        --text-primary:  #0F172A;
        --text-secondary:#334155;
        --text-muted:    #64748B;
    """

    if theme == "Light":
        dynamic_css += f":root {{ {light_vars} }}\n"
        dynamic_css += """
        [data-testid="stSidebar"] { background: #F8FAFC !important; border-right: 1px solid rgba(0,0,0,0.1) !important; }
        header[data-testid="stHeader"] { background: rgba(248,250,252,0.8) !important; border-bottom: 1px solid rgba(0,0,0,0.1) !important; }
        .hero { background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(255,255,255,0.95) 40%, rgba(212,175,55,0.1) 100%) !important; border: 1px solid rgba(0,0,0,0.1) !important; }
        .hero-title { background: linear-gradient(135deg, #B8860B 0%, #D4AF37 40%, #2563EB 100%) !important; -webkit-background-clip: text !important; -webkit-text-fill-color: transparent !important; }
        .stApp::before { background: radial-gradient(ellipse at 20% 20%, rgba(59,130,246,0.1) 0%, transparent 50%), radial-gradient(ellipse at 80% 80%, rgba(212,175,55,0.1) 0%, transparent 50%), radial-gradient(ellipse at 50% 50%, rgba(96,165,250,0.05) 0%, transparent 50%); }
        .upload-zone { background: #FFFFFF !important; border: 2px dashed rgba(0,0,0,0.1) !important; }
        [data-testid="stSidebar"] .stRadio label:hover { background: rgba(0,0,0,0.04) !important; }
        .glass-card::before { background: linear-gradient(90deg, transparent, rgba(59,130,246,0.2), rgba(212,175,55,0.2), transparent); opacity: 0.3; }
        """
    elif theme == "System":
        dynamic_css += f"@media (prefers-color-scheme: light) {{ :root {{ {light_vars} }} }}\n"

    accent_vars = ""
    if accent_color == "Gold":
        accent_vars = "--accent-blue: #D4AF37; --accent-electric: #F5E173; --accent-royal: #B8860B;"
    elif accent_color == "Purple":
        accent_vars = "--accent-blue: #8B5CF6; --accent-electric: #A78BFA; --accent-royal: #6D28D9;"
    elif accent_color == "Emerald":
        accent_vars = "--accent-blue: #10B981; --accent-electric: #34D399; --accent-royal: #047857;"

    if accent_vars:
        dynamic_css += f":root {{ {accent_vars} }}\n"

    if not animations_enabled:
        dynamic_css += """
        *, *::before, *::after {
            animation: none !important;
            transition: none !important;
        }
        """

    # DEBUG THEME: {theme}

    if dynamic_css:
        st.markdown(f"<style>{dynamic_css}</style>", unsafe_allow_html=True)