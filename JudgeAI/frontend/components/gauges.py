import streamlit as st


def render_confidence_gauge(confidence, size=160):
    """Render a circular confidence gauge with animated fill."""

    # Calculate stroke-dashoffset for the circle
    radius = (size - 16) / 2
    circumference = 2 * 3.14159 * radius
    offset = circumference - (confidence / 100) * circumference

    # Color based on confidence level
    if confidence >= 75:
        color = "#4ADE80"
        label = "High"
    elif confidence >= 50:
        color = "#FBBF24"
        label = "Medium"
    else:
        color = "#F87171"
        label = "Low"

    st.markdown(
        f"""
        <div class="confidence-gauge" style="width:{size}px;height:{size}px;">
            <svg viewBox="0 0 {size} {size}" class="confidence-gauge__svg">
                <circle
                    cx="{size/2}" cy="{size/2}" r="{radius}"
                    class="confidence-gauge__track"
                />
                <circle
                    cx="{size/2}" cy="{size/2}" r="{radius}"
                    class="confidence-gauge__fill"
                    style="
                        stroke:{color};
                        stroke-dasharray:{circumference};
                        stroke-dashoffset:{offset};
                    "
                />
            </svg>
            <div class="confidence-gauge__text">
                <div class="confidence-gauge__value" style="color:{color};">{confidence:.1f}%</div>
                <div class="confidence-gauge__label">{label}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_progress_ring(value, max_val=100, label="", size=80, color="#3B82F6"):
    """Render a small progress ring."""

    pct = (value / max_val) * 100 if max_val > 0 else 0
    radius = (size - 10) / 2
    circumference = 2 * 3.14159 * radius
    offset = circumference - (pct / 100) * circumference

    st.markdown(
        f"""
        <div class="progress-ring" style="width:{size}px;height:{size}px;">
            <svg viewBox="0 0 {size} {size}">
                <circle cx="{size/2}" cy="{size/2}" r="{radius}"
                    fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="4"/>
                <circle cx="{size/2}" cy="{size/2}" r="{radius}"
                    fill="none" stroke="{color}" stroke-width="4"
                    stroke-linecap="round"
                    stroke-dasharray="{circumference}"
                    stroke-dashoffset="{offset}"
                    transform="rotate(-90 {size/2} {size/2})"
                    style="transition: stroke-dashoffset 1.5s ease;"/>
            </svg>
            <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;">
                <span style="font-size:{size//5}px;font-weight:700;color:#F1F5F9;">{value}</span>
                <span style="font-size:{size//8}px;color:#64748B;">{label}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
