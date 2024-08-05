import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

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
    Unlock the power of your company's structured and historical data with Keen AI's enhanced Text to SQL and Gen AI model embedded in your core platforms.
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
    - **Email:** support@keenai.com
    - **Phone:** +1-234-567-890
    - **Address:** 123 AI Drive, Tech City, TC 12345

    ### Get In Touch
    Fill out the form below and we'll get back to you as soon as possible.
    """)

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for reaching out! We'll get back to you soon.")

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
