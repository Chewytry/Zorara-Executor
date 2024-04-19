import streamlit as st
import datetime

# Set custom range of years for date of birth
current_year = datetime.date.today().year
min_year = current_year - 100  # Set the minimum year to 100 years ago
max_year = current_year  # Set the maximum year to the current year

from model_predict import predict_with_cnn

def playground():
    st.title("Input Patient Data")
    
    st.markdown("**Sample images to drag and drop into the form:**", unsafe_allow_html=True)
    st.text("In order: no tumor, no tumor, tumor, tumor")

    t4,t5,t6,t7 = st.columns(4)
    t4.image("../assets/no_tumour_1.jpg")
    t5.image("../assets/no_tumour_2.jpg")
    t6.image("../assets/tumour_1.jpg")
    t7.image("../assets/tumour_2.jpg")
    

    with st.form("Patient's Details"):
        #Let user type in their patients' name, birthday, and remarks 
        name = st.text_input("Name")
        dob = st.date_input("Date of Birth", 
                     min_value=datetime.date(min_year, 1, 1),
                     max_value=datetime.date(max_year, 12, 31),
                     format="DD/MM/YYYY",
                     value=None)
        remarks = st.text_input("Remarks")
        uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
        submit = st.form_submit_button("Submit")

        if submit:
            st.write("Submitted! Check the `Patient Database` tab for details.")
            if uploaded_file is not None:
                st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
                label = predict_with_cnn(uploaded_file)
                # Append patient data to session state
                st.session_state['patient_data_list'].append({"name": name, "dob": dob, "remarks": remarks, "tumour": label})
            