import streamlit as st
import boto3
import pandas as pd
from PIL import Image
import io

# Page config
st.set_page_config(
    page_title="Akwaaba 🇬🇭",
    page_icon="🌍",
    layout="wide"
)

# Header
st.title("🌍 Akwaaba — Your AI Tourism Guide")
st.markdown("_Snap a photo. Discover the story._")

# Sidebar — language picker
with st.sidebar:
    st.header("⚙️ Settings")
    language = st.selectbox(
        "Tell me in...",
        ["English", "French", "Spanish", "Twi", "Mandarin"]
    )
    st.divider()
    st.caption("Built by Team [YOUR-TEAM-NAME] · cloudwithshad bootcamp")

# Main column — photo upload
uploaded = st.file_uploader(
    "Drop a photo of any Ghanaian landmark, dish, or sign",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    img = Image.open(uploaded)
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(img, caption="Your photo", use_container_width=True)
    with col2:
        with st.spinner("Analyzing..."):
            # MVP — mock response. Real AWS calls in Step 5.
            st.success("### 📍 Kwame Nkrumah Mausoleum")
            st.write("Built in 1992, this monument honours Ghana's first president...")
      