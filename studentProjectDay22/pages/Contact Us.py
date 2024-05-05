import streamlit as st
import pandas
from send_email import send_email

st.header("Contact Us")
df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_option = st.selectbox(label="Select Topic", options=df["topic"])
    user_message = st.text_area("Your message")
    message = f"""\
Subject: Email from {user_email}

From: {user_email}
Topic: {user_option}
{user_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Message sent successfully!")
