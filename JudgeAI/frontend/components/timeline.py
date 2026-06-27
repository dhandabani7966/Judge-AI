import streamlit as st


def render_pipeline_step(icon, label, state="pending", step_num=None):
    """
    Render a single pipeline step.
    state: 'done', 'active', 'pending'
    """

    state_class = f"pipeline-step--{state}"
    check = ""
    if state == "done":
        check = '<span class="pipeline-step__check">✓</span>'
    elif state == "active":
        check = '<span class="pipeline-step__loader"></span>'

    num_html = ""
    if step_num is not None:
        num_html = f'<span class="pipeline-step__num">{step_num}</span>'

    st.markdown(
        f"""
        <div class="pipeline-step {state_class}">
            <div class="pipeline-step__indicator">
                {num_html}
                <span class="pipeline-step__icon">{icon}</span>
            </div>
            <span class="pipeline-step__label">{label}</span>
            <span class="pipeline-step__status">{check}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_analysis_timeline(steps, current_step=-1):
    """
    Render a full analysis timeline.
    steps = [(icon, label), ...]
    current_step = index of active step (-1 = all pending, len = all done)
    """

    st.markdown('<div class="analysis-timeline">', unsafe_allow_html=True)

    for i, (icon, label) in enumerate(steps):
        if i < current_step:
            state = "done"
        elif i == current_step:
            state = "active"
        else:
            state = "pending"

        render_pipeline_step(icon, label, state, step_num=i + 1)

    st.markdown("</div>", unsafe_allow_html=True)
