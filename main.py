import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.FileHandler("/tmp/email_errors.log"),
        logging.StreamHandler()
    ]
)

# Function to send an email
def send_email(name, email, message):
    sender_email = "admin@keenai.io"
    receiver_email = "vince@keenai.io"
    app_password = os.getenv("APP_PASSWORD")

    if app_password is None:
        logging.error("APP_PASSWORD environment variable is not set")
        print("APP_PASSWORD environment variable is not set")
        return False

    print(f"APP_PASSWORD is set to: {app_password}")

    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = f"New Contact Us Message from {name}"

    # Create the email body
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    msg.attach(MIMEText(body, "plain"))

    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        logging.error("Error sending email: %s", str(e))
        print(f"Error sending email: {str(e)}")
        return False

# Function to create the main page
def main_page():
    st.title("Welcome to KeenAI")
    st.subheader("Transforming Text into SQL Queries Effortlessly")
    st.write("""
    KeenAI leverages advanced AI algorithms to convert natural language text into SQL queries. 
    Our service is designed to help you query your database without needing to write complex SQL statements.
    """)

    # Add more content about the services offered
    st.write("""
    ## Why Choose KeenAI?
    - **Ease of Use:** Simplify data querying with natural language.
    - **Accuracy:** Get precise SQL queries based on your text input.
    - **Efficiency:** Save time and reduce errors in querying databases.
    """)

# Function to create the about page
def about_page():
    st.title("About KeenAI")
    st.write("""
    KeenAI is at the forefront of AI-driven data querying technology. Our mission is to empower users to interact with their data intuitively and efficiently.

    ### Our Vision
    To make data querying as simple as asking a question, enabling everyone to access and leverage the power of their data.

    ### Our Team
    We are a group of passionate AI and data experts committed to innovation and excellence. Our team combines deep technical expertise with a strong focus on user experience to deliver top-notch solutions.

    ### Comparison Table
    Unlock the power of your company's structured and historical data with KeenAI's enhanced Text to SQL and Gen AI model embedded in your core platforms.
    Leverage your current data while benefitting from retrieval tools based on YOUR data.
    """)

    # Creating the comparison table data
    data = {
        "Comparison Area": [
            "Corpus Data", "Customization", "Security", "Accuracy", 
            "Ease of Integration", "Scalability", "Cost", "Support", 
            "Data Privacy", "Update Frequency", "Community and Collaboration"
        ],
        "Open-Source Generative AI Tools": [
            "Open-source data, answer general questions", "High, but requires technical expertise", 
            "Depends on implementation", "Variable, community-driven", 
            "Flexible, requires integration effort", "High, community-supported", 
            "Free or low cost", "Community-driven support", 
            "Depends on usage and implementation", "Frequent updates from community", 
            "Large, active community"
        ],
        "Text-to-SQL AI Tool with Company-Specific Corpus Data": [
            "Company specific data, answer questions specific to your company", "Tailored to company needs", 
            "High, company-controlled", "High, context-specific", 
            "Easy, designed for specific systems", "Customizable to company growth", 
            "Potentially higher, but justified", "Dedicated professional support", 
            "High, company-controlled data", "Scheduled, company-controlled", 
            "Focused on company needs"
        ]
    }

    # Configuring the AgGrid table
    df = pd.DataFrame(data)
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(wrapText=True, autoHeight=True)
    grid_options = gb.build()

    # Displaying the table
    AgGrid(df, gridOptions=grid_options, height=400, fit_columns_on_grid_load=True)

# Function to create the contact us page
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

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Contact Us"))

# Show the selected page
if page == "Home":
    main_page()
elif page == "About":
    about_page()
elif page == "Contact Us":
    contact_page()
