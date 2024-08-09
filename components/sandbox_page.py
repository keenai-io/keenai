import streamlit as st

import streamlit as st

def sandbox_page():
    st.markdown(
        """
        <style>
        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;  /* Adjust height as needed */
            text-align: center;
            font-size: 2.5rem;
        }
        </style>
        <div class="centered">
            Under Construction 🚧
        </div>
        """,
        unsafe_allow_html=True
    )