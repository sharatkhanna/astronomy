import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images\photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hi there! Welcome to my page. I'm Sharat and I
    'm learning Python programming.
    This page is currently under development. 
    I'm creating this using Python. Hope 
    to see you around soon. Have a great day.
    """
    st.info(content)

content2 = """
Here are some of the apps that I've built using Python. 
Feel free to download and try them. Contact me to know more
or to provide feedback!
"""
st.write(content2)

