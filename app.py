import streamlit as st

st.set_page_config(
    page_title="Audio Video Utility Studio",
    layout="wide"
)

st.title("🎬 Audio Video Utility Studio")

st.sidebar.title("Modules")

menu = st.sidebar.selectbox(
    "Select Module",
    [
        "Audio Toolkit",
        "Video Toolkit",
        "Media Analyzer",
        "Frame Processor",
        "Audio Visualizer",
        "Batch Processor"
    ]
)

st.write("Selected:", menu)
