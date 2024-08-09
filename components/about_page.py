import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Function to create the About page
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