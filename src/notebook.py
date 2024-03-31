import streamlit as st
import streamlit.components.v1 as components

def notebook():
    t1,t2 = st.columns((0.15,1))

    t1.image("assets\logo.png", width = 120)
    t2.title("CS3244 Brain Tumor -  Notebook")

    st.markdown('### This is our Notebook')

    with open("CS3244.html", "r") as f:
        html_content = f.read()

    # Embed the HTML in the Streamlit app
    components.html(html_content, height=30000)