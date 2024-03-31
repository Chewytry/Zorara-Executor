import streamlit as st
from landing import landing
from report import report
from playground import playground
from notebook import notebook

# Page configs
st.set_page_config(
    page_title="CS3244 Brain Tumor Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="assets\logo.png"
)

# Define the pages of the app
PAGES = {
    "Landing": landing,
    "Report": report,
    "Notebook": notebook,
    "Playground": playground,
}

# Sidebar for navigation
st.sidebar.title('Navigation')
selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))

# Render the selected page
page = PAGES[selection]
page()
