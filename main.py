import logging
import streamlit as st
from components._partials.navbar import get_current_page_from_navbar
from components.main_page import main_page
from components.sandbox_page import sandbox_page
from components.about_page import about_page
from components.contact_page import contact_page
from components._partials.footer import add_footer
from components.test_page import test_page

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

st.set_page_config(page_title="KeenAI", page_icon="./static/img/favicon.ico", layout="centered")

current_page = get_current_page_from_navbar()

if current_page == "Home":
    main_page()
elif current_page == "Sandbox":
    sandbox_page()
elif current_page == "About":
    about_page()
elif current_page == "Contact Us":
    contact_page()
# elif current_page == "Test Page":    
#     test_page()

add_footer()
