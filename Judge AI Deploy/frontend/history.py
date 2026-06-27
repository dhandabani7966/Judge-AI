import streamlit as st
from datetime import datetime


def show_history():
    """Display analysis history from session state."""

    from frontend.components.hero import render_hero
    from frontend.components.sections import render_section_header, render_divider
    from frontend.components.badges import render_badge

    # ── Initialize history in session state ──
    if "analysis_history" not in st.session_state:
        st.session_state.analysis_history = []

    # ── Hero ──
    render_hero(
        badge_text="📋 Analysis History",
        title="History",
        description="View and manage your past legal document analyses. All data is stored in your current session.",
        compact=True,
    )

    # ── View Selected Item Detail ──
    if "selected_history_item" in st.session_state and st.session_state.selected_history_item is not None:
        item = st.session_state.selected_history_item
        col_back, _ = st.columns([1, 4])
        with col_back:
            if st.button("← Back to History", use_container_width=True):
                st.session_state.selected_history_item = None
                st.rerun()
        
        from frontend.result import show_result
        show_result(
            legal_info=item["legal_info"],
            summary=item["summary"],
            prediction=item["prediction"],
            confidence=item["confidence"]
        )
        return

    history = st.session_state.analysis_history

    # ── Stats Row ──
    render_section_header("📊", "Overview")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("📂 Total Analyses", str(len(history)))
    with c2:
        today_count = sum(
            1 for h in history
            if h.get("timestamp", "").startswith(datetime.now().strftime("%Y-%m-%d"))
        )
        st.metric("📅 Today", str(today_count))
    with c3:
        last_time = history[-1]["timestamp"] if history else "N/A"
        st.metric("🕐 Last Analysis", last_time if last_time == "N/A" else last_time.split(" ")[1][:5])

    render_divider()

    # ── History List ──
    if not history:
        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-state__icon">📋</div>
                <div class="empty-state__title">No Analyses Yet</div>
                <div class="empty-state__desc">
                    Upload a legal document or paste judgment text on the Analyze page
                    to see your history here.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    render_section_header("📄", "Recent Analyses")

    # ── Search ──
    search = st.text_input(
        "🔍 Search analyses...",
        placeholder="Search by document name, prediction, or court...",
        label_visibility="collapsed",
    )

    for i, item in enumerate(reversed(history)):
        # Filter by search
        if search:
            search_lower = search.lower()
            searchable = f"{item.get('name','')} {item.get('prediction','')} {item.get('court','')}".lower()
            if search_lower not in searchable:
                continue

        pred = item.get("prediction", "Unknown")
        conf = item.get("confidence", 0)
        name = item.get("name", "Document")
        timestamp = item.get("timestamp", "")
        court = item.get("court", "Unknown Court")

        # Prediction color
        if pred == "Accepted":
            pred_badge = render_badge(f"✓ {pred}", "green")
        elif pred == "Rejected":
            pred_badge = render_badge(f"✗ {pred}", "red")
        else:
            pred_badge = render_badge(f"◐ {pred}", "gold")

        conf_badge = render_badge(f"{conf:.1f}%", "blue")

        # Render layout with interactive View button
        col_text, col_btn = st.columns([5, 1])
        with col_text:
            st.markdown(
                f"""
                <div class="history-item" style="animation-delay: {i * 0.05}s; margin-bottom: 0px;">
                    <div class="history-item__icon">📄</div>
                    <div class="history-item__info">
                        <div class="history-item__name">{name}</div>
                        <div class="history-item__meta">{court} · {timestamp}</div>
                    </div>
                    <div style="display:flex;gap:6px;align-items:center;">
                        {pred_badge}
                        {conf_badge}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col_btn:
            # Shift button slightly down to align vertically with the list item
            st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
            if st.button("👁 View", key=f"view_{i}", use_container_width=True):
                st.session_state.selected_history_item = item
                st.rerun()

    # ── Clear History ──
    render_divider()

    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🗑 Clear History", use_container_width=True):
            st.session_state.analysis_history = []
            st.session_state.selected_history_item = None
            st.rerun()
