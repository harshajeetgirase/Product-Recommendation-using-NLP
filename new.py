import streamlit as st

# Page config
st.set_page_config(page_title="Simple Background Demo", layout="wide")

# --- Simple Background (colorful gradient) ---
page_bg = """
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 25%, #fbc2eb 50%, #a18cd1 75%, #fbc2eb 100%);
    background-size: cover;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)


# --- Content ---
st.title("🌈 Simple Background Example")
st.write("This page has a clean colorful gradient background.")
