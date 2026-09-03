import streamlit as st
from app.agent import investigate_with_trace


st.set_page_config(
    page_title="IncidentAI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>

/* APP */

.stApp {
    background:
        radial-gradient(circle at 85% 5%, rgba(99, 102, 241, 0.10), transparent 28%),
        radial-gradient(circle at 15% 80%, rgba(16, 185, 129, 0.06), transparent 25%),
        #070b14;
    color: #e5e7eb;
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: #090e19;
    border-right: 1px solid #1e293b;
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}


/* TYPOGRAPHY */

h1, h2, h3 {
    letter-spacing: -0.03em;
}

h1 {
    font-size: 2.6rem !important;
    font-weight: 750 !important;
}

p {
    color: #94a3b8;
}


/* HERO */

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 12px;
    border-radius: 999px;
    border: 1px solid #263449;
    background: rgba(15, 23, 42, 0.85);
    color: #a5b4fc;
    font-size: 13px;
    margin-bottom: 12px;
}

.hero-title {
    font-size: 44px;
    line-height: 1.05;
    font-weight: 750;
    color: #f8fafc;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #94a3b8;
    font-size: 16px;
    max-width: 760px;
    line-height: 1.6;
}


/* CARDS */

.card {
    background: rgba(11, 18, 32, 0.88);
    border: 1px solid #1e293b;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 18px 45px rgba(0,0,0,0.18);
}

.card-title {
    color: #f8fafc;
    font-size: 14px;
    font-weight: 650;
    margin-bottom: 6px;
}

.card-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 700;
}

.card-label {
    color: #64748b;
    font-size: 12px;
}


/* STATUS */

.status-live {
    color: #34d399;
    font-size: 13px;
    font-weight: 600;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #34d399;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    box-shadow: 0 0 10px rgba(52, 211, 153, 0.7);
}


/* TOOL */

.tool-chip {
    display: inline-block;
    padding: 8px 12px;
    margin: 5px 5px 5px 0;
    border-radius: 8px;
    background: #0f172a;
    border: 1px solid #263449;
    color: #cbd5e1;
    font-family: monospace;
    font-size: 12px;
}


/* REPORT */

.report {
    background: rgba(10, 16, 29, 0.94);
    border: 1px solid #263449;
    border-radius: 16px;
    padding: 24px;
    color: #dbeafe;
    line-height: 1.7;
}


/* INPUT */

.stTextArea textarea {
    background-color: #0b1220 !important;
    border: 1px solid #263449 !important;
    border-radius: 12px !important;
    color: #f8fafc !important;
    min-height: 110px;
}

.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 1px #6366f1 !important;
}


/* BUTTON */

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    border: none;
    border-radius: 10px;
    padding: 0.7rem 1rem;
    color: white;
    font-weight: 650;
    transition: 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 10px 30px rgba(79, 70, 229, 0.25);
}


/* DIVIDER */

hr {
    border-color: #1e293b;
}


/* STREAMLIT CLEANUP */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:

    st.markdown("""
    <div style="font-size:24px;font-weight:750;color:#f8fafc;">
        ⚡ Incident<span style="color:#818cf8;">AI</span>
    </div>

    <div style="font-size:12px;color:#64748b;margin-top:3px;margin-bottom:28px;">
        AI Incident Investigator
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Investigation")

    st.markdown("""
    <div style="
        background:#111827;
        border:1px solid #263449;
        border-radius:10px;
        padding:12px;
        color:#c7d2fe;
        margin-bottom:10px;
    ">
        ◉ New Investigation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="color:#64748b;font-size:14px;line-height:2.5;">
        ◇ Evidence<br>
        ◇ Agent Tools<br>
        ◇ Root Cause Reports<br>
        ◇ Investigation History
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <span class="status-dot"></span>
    <span class="status-live">Agent online</span>
    """, unsafe_allow_html=True)

    st.caption("LangChain · OpenAI · Tool Calling")


# -------------------------
# HERO
# -------------------------

st.markdown("""
<div class="hero-badge">
    ● AI INCIDENT RESPONSE
</div>

<div class="hero-title">
    Investigate incidents.<br>
    <span style="color:#818cf8;">Find the evidence.</span>
</div>

<div class="hero-subtitle">
    An autonomous incident investigator that inspects transactions,
    logs, deployments and code changes before determining the most likely root cause.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# -------------------------
# METRIC CARDS
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">Agent Status</div>
        <div class="card-value" style="color:#34d399;">Online</div>
        <div class="card-label">Ready to investigate</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Available Tools</div>
        <div class="card-value">4</div>
        <div class="card-label">Evidence sources</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Investigation Mode</div>
        <div class="card-value">Agentic</div>
        <div class="card-label">Autonomous tool selection</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-title">Environment</div>
        <div class="card-value">Demo</div>
        <div class="card-label">Simulated production data</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)


# -------------------------
# INVESTIGATION
# -------------------------

left, right = st.columns([1.05, 0.95], gap="large")


with left:

    st.markdown("### New Investigation")

    st.caption(
        "Describe the incident. The agent will decide which evidence sources to inspect."
    )

    question = st.text_area(
        "Incident description",
        placeholder="Why are payments failing?",
        label_visibility="collapsed"
    )

    investigate_button = st.button(
        "⚡ Start investigation",
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("#### Available evidence sources")

    st.markdown("""
    <span class="tool-chip">check_transactions()</span>
    <span class="tool-chip">check_logs()</span>
    <span class="tool-chip">check_deployments()</span>
    <span class="tool-chip">check_code_changes()</span>
    """, unsafe_allow_html=True)


with right:

    st.markdown("### Investigation Flow")

    st.markdown("""
    <div class="card">

        <div style="color:#818cf8;font-weight:650;">
            01 · Understand incident
        </div>

        <div style="height:22px;border-left:1px solid #334155;margin-left:7px;"></div>

        <div style="color:#cbd5e1;font-weight:650;">
            02 · Select evidence sources
        </div>

        <div style="height:22px;border-left:1px solid #334155;margin-left:7px;"></div>

        <div style="color:#cbd5e1;font-weight:650;">
            03 · Execute investigation tools
        </div>

        <div style="height:22px;border-left:1px solid #334155;margin-left:7px;"></div>

        <div style="color:#cbd5e1;font-weight:650;">
            04 · Correlate evidence
        </div>

        <div style="height:22px;border-left:1px solid #334155;margin-left:7px;"></div>

        <div style="color:#34d399;font-weight:650;">
            05 · Generate root cause report
        </div>

    </div>
    """, unsafe_allow_html=True)


# -------------------------
# RUN AGENT
# -------------------------

if investigate_button:

    if not question.strip():
        st.warning("Enter an incident description first.")

    else:

        st.markdown("---")

        st.markdown("## Investigation")

        with st.spinner("Agent is investigating the incident..."):

            try:
                result = investigate_with_trace(question)

            except Exception as error:
                st.error(f"Investigation failed: {error}")
                st.stop()

        tools_used = result["tools_used"]
        report = result["report"]

        col_tools, col_status = st.columns([2, 1])

        with col_tools:

            st.markdown("### Evidence sources inspected")

            if tools_used:

                tool_html = ""

                for tool in tools_used:
                    tool_html += (
                        f'<span class="tool-chip">✓ {tool}</span>'
                    )

                st.markdown(
                    tool_html,
                    unsafe_allow_html=True
                )

            else:
                st.caption("No tools were called.")

        with col_status:

            st.markdown("### Status")

            st.success("Investigation complete")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("### Root Cause Report")

        st.markdown(
            '<div class="report">',
            unsafe_allow_html=True
        )

        st.markdown(report)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.caption(
            "Generated by IncidentAI · Evidence-driven AI incident investigation"
        )

