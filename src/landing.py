import streamlit as st

def landing():
    t1,t2 = st.columns((0.15,1))

    t1.image("../assets/logo.png", width = 120)
    t1.image("assets/logo.png", width = 120)
    t2.title("CS3244 Brain Tumor - Welcome")

    st.markdown('## Motivation')

    st.markdown("""Traditional methods for diagnosing brain tumours often involve manual analysis, which is characterised by laboriousness, subjectivity, and a high potential for errors.
        To address these challenges, we aim to automate and refine the accuracy of brain tumor identification through cutting-edge deep learning and machine learning techniques.
        This enables early detection, which is crucial for improving patient outcomes and increases the likelihood of successful treatments. 
        Furthermore, high-accuracy models capable of detecting subtle patterns and abnormalities in medical images can reduce unnecessary treatments and false negatives. 
        Ultimately, this effort aims to revolutionise the diagnosis and treatment of brain tumours by leveraging advanced deep learning and machine learning techniques, 
        which have the potential to significantly impact patient care and advance the field of medical imaging analysis.""")
    
    st.markdown('## Description of Project')

    st.markdown("""Our project entails the development of a machine learning model designed to predict the presence of brain tumors through image classification. Leveraging a dataset 
                comprising Magnetic Resonance Imaging (MRI) scans of patients diagnosed with brain tumors, our model aims to provide accurate and efficient diagnoses, thereby 
                contributing to the advancement of brain tumor detection and treatment. """)

    st.markdown('## App Details')

    st.markdown('### Patient Details Form')
    st.markdown("""This page serves as a platform for users, specifically medical personnels, to upload MRI images of their patients along with corresponding patient details.
                These images are processed using our trained CNN model to detect the presence of tumors. Subsequently, all gathered information is stored in the patient database.
                Users have the option to experiment with the form by dragging and dropping example MRI images provided.""")
    
    st.markdown('### Patient Databse')
    st.markdown("""This section functions as the repository for all patient data collected during the current session.""")
