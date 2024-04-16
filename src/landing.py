import streamlit as st

def landing():
    t1,t2 = st.columns((0.15,1))

    t1.image("assets/logo.png", width = 120)
    t2.title("CS3244 Brain Tumor - Welcome")

    st.markdown('## Motivation')

    st.markdown("""Traditional methods for diagnosing brain tumours often involve manual analysis, which is characterised by laboriousness, subjectivity, and a high potential for errors.
        To address this issue, we aim to automate and enhance the accuracy of brain tumour identification through the use of deep learning and machine learning techniques which will be elaborated on later. 
        This enables early detection, which is crucial for improving patient outcomes and increases the likelihood of successful treatments. 
        Furthermore, high-accuracy models capable of detecting subtle patterns and abnormalities in medical images can prevent unnecessary treatments and false negatives. 
        Ultimately, this effort aims to revolutionise the diagnosis and treatment of brain tumours by implementing advanced deep learning and machine learning techniques, 
        which have the potential to significantly impact patient care and advance the field of medical imaging analysis.""")
    
    st.markdown('## Description of Project')

    st.markdown("""We will build a machine learning model that will predict the presence of a brain tumour via image classification based on a dataset that consists of scanned
    (Magnetic Resonance Imaging (MRI) images of brains of patients diagnosed with brain tumours. """)

    st.markdown('## How to use this app?')

    st.markdown('### Notebook')
    st.markdown("""This tab brings you to the notebook of our project""")

    st.markdown('### Playground')
    st.markdown("""The playground allows users (e.g. our target users - medical personnel) to upload MRI images of their patients, together with their details.
                Theese images are processed using our trained CNN model to detect the presence of tumors. Subsequently, all gathered information is stored in the patient database.
                There are example MRI images for user to drag and drop to try out the form.""")
    
    st.markdown('### Patient Data')
    st.markdown("""This is where all the patient's data are stored in the current session. """)