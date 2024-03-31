import streamlit as st

def playground():
    t1,t2 = st.columns((0.15,1))

    t1.image("assets\logo.png", width = 120)
    t2.title("CS3244 Brain Tumor -  Hands On")

    uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # To read and display the image, we use st.image
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)