import streamlit as st
from pathlib import Path
from PIL import Image

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="CLASSIFIC AI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# LOAD LOGO
# =====================================================

logo_path = Path(__file__).parent / "assets" / "classific_logo.png"

# =====================================================
# HEADER
# =====================================================

if logo_path.exists():

    logo = Image.open(logo_path)

    st.image(
        logo,
        width=550,
    )

else:

    st.title("CLASSIFIC AI")
    st.caption("From Data to Decision")

st.divider()

# =====================================================
# MAIN LAYOUT
# =====================================================

left, center, right = st.columns([1.2, 4.5, 1.5])

# =====================================================
# LEFT NAVIGATION
# =====================================================

with left:

    st.subheader("Navigation")

    st.button("🏠 Home", use_container_width=True)

    st.button("📂 Dataset", use_container_width=True)

    st.button("🤖 Agents", use_container_width=True)

    st.button("📊 Dashboard", use_container_width=True)

    st.button("📄 Reports", use_container_width=True)

# =====================================================
# CENTER PANEL
# =====================================================

with center:

    st.header("Welcome to CLASSIFIC AI")

    st.info(
        "Upload a dataset to begin."
    )

# =====================================================
# RIGHT PANEL
# =====================================================

with right:

    st.subheader("AI Copilot")

    st.text_area(
        "Ask anything",
        height=350,
        placeholder="Type your question here...",
    )