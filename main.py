import logging
import streamlit as st
from components.main_page import main_page
from components.about_page import about_page
from components.contact_page import contact_page

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

st.set_page_config(page_title="KeenAI", page_icon=":smirk_cat:", layout="wide")

st.sidebar.title(":smirk_cat:")
page = st.sidebar.radio("Go to", ("Home", "About", "Contact Us"))

if page == "Home":
    main_page()
elif page == "About":
    about_page()
elif page == "Contact Us":
    contact_page()