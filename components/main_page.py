import streamlit as st

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