import streamlit as st


def render_glass_card(icon, title, description, accent="gold"):
    """Render a glass-morphism card with icon, title, description."""

    accent_map = {
        "gold": ("rgba(212,175,55,0.12)", "rgba(212,175,55,0.25)", "#D4AF37"),
        "blue": ("rgba(59,130,246,0.12)", "rgba(59,130,246,0.25)", "#3B82F6"),
        "green": ("rgba(74,222,128,0.12)", "rgba(74,222,128,0.25)", "#4ADE80"),
        "red": ("rgba(248,113,113,0.12)", "rgba(248,113,113,0.25)", "#F87171"),
    }

    bg, border, color = accent_map.get(accent, accent_map["gold"])

    st.markdown(
        f"""
        <div class="glass-card">
            <div class="glass-card__icon" style="background:{bg};border-color:{border};color:{color};">
                {icon}
            </div>
            <h3 class="glass-card__title">{title}</h3>
            <p class="glass-card__desc">{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_info_card(label, value, accent="gold"):
    """Render a labeled info card (used in result page)."""

    accent_colors = {
        "gold": "#D4AF37",
        "blue": "#3B82F6",
        "green": "#4ADE80",
        "red": "#F87171",
    }
    color = accent_colors.get(accent, "#D4AF37")

    st.markdown(
        f"""
        <div class="info-card">
            <div class="info-card__accent" style="background:{color};"></div>
            <div class="info-card__content">
                <div class="info-card__label" style="color:{color};">{label}</div>
                <div class="info-card__value">{value}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_card(icon, label, value, delta="", accent="gold"):
    """Render an animated statistics card."""

    accent_colors = {
        "gold": "#D4AF37",
        "blue": "#3B82F6",
        "green": "#4ADE80",
        "cyan": "#22D3EE",
    }
    color = accent_colors.get(accent, "#D4AF37")

    delta_html = ""
    if delta:
        delta_html = f'<div class="stat-card__delta">{delta}</div>'

    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-card__icon" style="color:{color};">{icon}</div>
            <div class="stat-card__label">{label}</div>
            <div class="stat-card__value">{value}</div>
            {delta_html}
            <div class="stat-card__glow" style="background:radial-gradient(circle,{color}15 0%,transparent 70%);"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
