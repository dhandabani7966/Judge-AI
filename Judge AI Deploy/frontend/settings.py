import streamlit as st


def show_settings():
    """Display application settings."""

    from frontend.components.hero import render_hero
    from frontend.components.sections import render_section_header, render_divider

    # ── Initialize settings in session state ──
    defaults = {
        "theme": "Dark",
        "accent_color": "Royal Blue",
        "animations_enabled": True,
        "notifications_enabled": True,
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

    # ── Hero ──
    render_hero(
        badge_text="⚙ Preferences",
        title="Settings",
        description="Customize your JudgeAI experience. All preferences are stored in your current session.",
        compact=True,
    )

    # ── Appearance ──
    render_section_header("🎨", "Appearance")

    st.markdown(
        """
        <div class="settings-group">
            <div class="settings-group__title">Theme</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    theme_opts = ["Dark", "Light", "System"]
    theme = st.selectbox(
        "Theme",
        theme_opts,
        index=theme_opts.index(st.session_state.theme) if st.session_state.theme in theme_opts else 0,
        label_visibility="collapsed",
    )
    if theme != st.session_state.theme:
        st.session_state.theme = theme
        if st.session_state.notifications_enabled:
            st.toast(f"Theme updated to {theme}", icon="🎨")
        st.rerun()

    st.markdown(
        """
        <div class="settings-group">
            <div class="settings-group__title">Accent Color</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    accent_opts = ["Royal Blue", "Gold", "Purple", "Emerald"]
    accent = st.selectbox(
        "Accent Color",
        accent_opts,
        index=accent_opts.index(st.session_state.accent_color) if st.session_state.accent_color in accent_opts else 0,
        label_visibility="collapsed",
    )
    if accent != st.session_state.accent_color:
        st.session_state.accent_color = accent
        if st.session_state.notifications_enabled:
            st.toast(f"Accent color updated to {accent}", icon="✨")
        st.rerun()

    # Color preview
    color_map = {
        "Royal Blue": "#3B82F6",
        "Gold": "#D4AF37",
        "Purple": "#8B5CF6",
        "Emerald": "#10B981",
    }
    preview_color = color_map.get(accent, "#3B82F6")
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:10px;margin:8px 0 20px;">
            <div style="width:24px;height:24px;border-radius:6px;background:{preview_color};"></div>
            <span style="font-size:13px;color:var(--text-secondary);">Active: {accent}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_divider()

    # ── Behavior ──
    render_section_header("⚡", "Behavior")

    st.markdown(
        """
        <div class="settings-group">
            <div class="settings-group__title">Animations & Notifications</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    animations = st.toggle(
        "Enable Animations",
        value=st.session_state.animations_enabled,
    )
    if animations != st.session_state.animations_enabled:
        st.session_state.animations_enabled = animations
        if st.session_state.notifications_enabled:
            st.toast(f"Animations {'enabled' if animations else 'disabled'}", icon="⚡")
        st.rerun()

    notifications = st.toggle(
        "Enable Notifications",
        value=st.session_state.notifications_enabled,
    )
    if notifications != st.session_state.notifications_enabled:
        st.session_state.notifications_enabled = notifications
        if notifications:
            st.toast("Notifications enabled", icon="🔔")
        st.rerun()

    render_divider()

    # ── About ──
    render_section_header("ℹ️", "Application Info")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Version", "2.0 Pro")
    with c2:
        st.metric("ML Model", "Random Forest")
    with c3:
        st.metric("Accuracy", "82.47%")

    render_divider()

    # ── Reset ──
    col1, col2, col3 = st.columns([2, 1.5, 2])
    with col2:
        if st.button("🔄 Reset All Preferences", use_container_width=True):
            for key, val in defaults.items():
                st.session_state[key] = val
            st.success("✅ Preferences reset to defaults.")
            st.rerun()
