import streamlit as st


def render_hero(badge_text, title, subtitle="", description="", compact=False):
    """Render a premium hero section with animated background orbs."""

    padding = "32px 40px" if compact else "52px 48px"
    title_size = "36px" if compact else "52px"

    subtitle_html = ""
    if subtitle:
        subtitle_html = f"""
        <div class="hero-subtitle">{subtitle}</div>
        """

    desc_html = ""
    if description:
        desc_html = f"""
        <p class="hero-description">{description}</p>
        """

    st.markdown(
        f"""
        <div class="hero" style="padding:{padding};">
            <div class="hero-orb hero-orb--1"></div>
            <div class="hero-orb hero-orb--2"></div>
            <div class="hero-badge">{badge_text}</div>
            <h1 class="hero-title" style="font-size:{title_size};">{title}</h1>
            {subtitle_html}
            {desc_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
