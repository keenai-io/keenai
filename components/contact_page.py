import streamlit as st
from utils.send_email import send_email

def contact_page():
    st.title("Contact Us")
    st.write("""
    We'd love to hear from you! Whether you have a question about features, pricing, need a demo, or anything else, our team is ready to answer all your questions.

    ### Contact Information
    - **Email:** vince@keenai.io
    - **Phone:** +1-610-368-7379

    ### Get In Touch
    Fill out the form below and we'll get back to you as soon as possible.
    """)

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            if send_email(name, email, message):
                st.success("Thank you for reaching out! We'll get back to you soon.")
            else:
                st.error("There was an error sending your message. Please try again later.")