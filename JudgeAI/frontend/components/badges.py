import streamlit as st

def render_badge(text, accent="gold"):
    """Return badge HTML string (do NOT call st.markdown inside)."""
    accent_colors = {
        "gold":  ("rgba(212,175,55,0.15)",  "#D4AF37"),
        "blue":  ("rgba(59,130,246,0.15)",  "#3B82F6"),
        "green": ("rgba(74,222,128,0.15)",  "#4ADE80"),
        "cyan":  ("rgba(34,211,238,0.15)",  "#22D3EE"),
        "red":   ("rgba(248,113,113,0.15)", "#F87171"),
    }
    bg, color = accent_colors.get(accent, accent_colors["gold"])
    
    # ✅ Return string — st.markdown() call வேண்டாம்!
    return f"""
        <span style="
            background:{bg};
            color:{color};
            border:1px solid {color}40;
            padding:2px 10px;
            border-radius:999px;
            font-size:11px;
            font-weight:700;
            letter-spacing:0.5px;
        ">{text}</span>
    """
