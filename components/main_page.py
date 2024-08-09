import streamlit as st

def main_page():
    lcol, ccol, rcol = st.columns(3)
    with ccol:
        st.image("static/img/keenai.png", use_column_width=True)
    st.title("Welcome to KeenAI  😼")
    st.subheader("Making Complex Data Querying Natural and Easy")
    st.write("""
    KeenAI harnesses cutting-edge AI to transform your natural language text into powerful SQL queries, delivering your database results in seconds without you having to write a single SQL statement.
    """)

    # Add more content about the services offered
    st.write("""
    ## Why Choose KeenAI?
    - **Ease of Use:** Simplify data querying with natural language.
    - **Accuracy:** Get precise SQL queries based on your text input.
    - **Efficiency:** Save time and reduce errors in querying databases.
    """)