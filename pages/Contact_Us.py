import streamlit as st
from send_email import send_email


st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Enter your email")
    raw_message = st.text_area("Enter your message")
    message=f"""\
    Subject: Mail from {user_email}

    From: {user_email}
    {raw_message}
    """
    button=st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(message)
        st.info("Email sent successfully")
