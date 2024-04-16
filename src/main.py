import streamlit as st
from landing import landing
from playground import playground
from patient_data import patient_data

# Page configs
st.set_page_config(
    page_title="CS3244 Brain Tumor Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="../assets/logo.png"
)

# Initialize patient data list in session state
if 'patient_data_list' not in st.session_state:
    st.session_state['patient_data_list'] = []

if 'page' not in st.session_state:
    st.session_state['page'] = "Home"


# Define the pages of the app
PAGES = {
    "Home": landing,
    "Patient Details Form": playground,
    "Patient Database": patient_data
}

# Sidebar for navigation
st.sidebar.title('Navigation')
with st.sidebar:
    for key, value in PAGES.items():
        if st.button(key):
            selection = key
            st.session_state['page'] = key

#selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Render the selected page
page = PAGES[st.session_state.get('page')]
page()
