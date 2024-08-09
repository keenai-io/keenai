import streamlit as st

def add_footer():
    footer = """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117; /* Match background to blend in */
        color: #888; /* Lighter gray to blend in */
        text-align: center;
        font-size: 12px; /* Smaller font size */
        padding: 5px 0;
        box-shadow: none; /* Remove shadow */
    }
    </style>
    <div class="footer">
        © 2024 KeenAI Technologies, LLC. All rights reserved.
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)