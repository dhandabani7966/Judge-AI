import streamlit as st


def render_section_header(icon, title):
    """Render a section header with icon, title, and gradient line."""

    st.markdown(
        f"""
        <div class="section-header">
            <span class="section-header__icon">{icon}</span>
            <h2 class="section-header__title">{title}</h2>
            <div class="section-header__line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_divider():
    """Render a premium gradient divider."""

    st.markdown(
        '<div class="premium-divider"></div>',
        unsafe_allow_html=True,
    )
