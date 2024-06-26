import streamlit as st
from send_email import send_email

st.header("Contact Us: ")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")

    user_message = st.text_area("Your message: ")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Email sent successfully", )
