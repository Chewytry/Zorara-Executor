import streamlit as st

def patient_data():
    st.title("Stored Patient Data")
    patient_data_list = st.session_state.get('patient_data_list', [])
    if patient_data_list:
        st.dataframe(patient_data_list)
    else:
        st.write("No patient data available.")