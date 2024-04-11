import streamlit as st
from model_predict import predict_with_cnn

def playground():
    t1,t2 = st.columns((0.15,1))

    t1.image("assets\logo.png", width = 120)
    t2.title("CS3244 Brain Tumor -  Hands On")
    
    st.markdown("**Images you can drag and input into the form for example:**", unsafe_allow_html=True)
    st.text("In order: no tumour, no tumour, tumour, tumour")

    t4,t5,t6,t7 = st.columns(4)
    t4.image("assets/no_tumour_1.jpg")
    t5.image("assets/no_tumour_2.jpg")
    t6.image("assets/tumour_1.jpg")
    t7.image("assets/tumour_2.jpg")
    

    with st.form("Patient's Details"):
        #Let user type in their patients' name, birthday, and remarks 
        name = st.text_input("Name")
        dob = st.date_input("Date of Birth", format="DD/MM/YYYY", value=None)
        remarks = st.text_input("Remarks")
        uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])
        submit = st.form_submit_button("Submit")

        if submit:
            st.text("Submitted. Check `Patient Data` tab for details.")
            if uploaded_file is not None:
                st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
                label = predict_with_cnn(uploaded_file)
                # Append patient data to session state
                st.session_state['patient_data_list'].append({"name": name, "dob": dob, "remarks": remarks, "tumour": label})
            