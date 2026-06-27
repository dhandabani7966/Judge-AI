import streamlit as st


def render_badge(text, color="gold"):
    """Render an inline badge/pill."""

    color_map = {
        "gold": ("rgba(212,175,55,0.12)", "rgba(212,175,55,0.3)", "#D4AF37"),
        "blue": ("rgba(59,130,246,0.1)", "rgba(59,130,246,0.25)", "#3B82F6"),
        "green": ("rgba(74,222,128,0.1)", "rgba(74,222,128,0.25)", "#4ADE80"),
        "red": ("rgba(248,113,113,0.1)", "rgba(248,113,113,0.25)", "#F87171"),
        "cyan": ("rgba(34,211,238,0.1)", "rgba(34,211,238,0.25)", "#22D3EE"),
    }
    bg, border, fg = color_map.get(color, color_map["gold"])

    return f'<span class="badge" style="background:{bg};border:1px solid {border};color:{fg};">{text}</span>'


def render_status_badge(status):
    """Render a status badge (Active, Inactive, Pending, etc.)."""

    status_map = {
        "active": ("green", "● Active"),
        "online": ("green", "● Online"),
        "inactive": ("red", "● Inactive"),
        "offline": ("red", "● Offline"),
        "pending": ("gold", "◐ Pending"),
        "processing": ("blue", "◌ Processing"),
    }

    color, label = status_map.get(status.lower(), ("gold", f"● {status}"))
    return render_badge(label, color)


def render_badge_row(badges):
    """Render a row of badges. badges = [(text, color), ...]"""

    html = '<div class="badge-row">'
    for text, color in badges:
        html += render_badge(text, color)
    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)
