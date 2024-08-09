import logging
import streamlit as st
from components.navbar import get_current_page_from_navbar
from components.main_page import main_page
from components.sandbox_page import sandbox_page
from components.about_page import about_page
from components.contact_page import contact_page

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

st.set_page_config(page_title="KeenAI", page_icon=":smirk_cat:", layout="wide")

smirk_cat = "😼"
# styles = {
#     "nav": {
#         "background-color": "rgb(36, 37, 42)",
#     },
#     "div": {
#         "max-width": "32rem",
#     },
#     "span": {
#         "border-radius": "0.5rem",
#         "color": "rgb(255, 255, 255)",
#         "margin": "0 0.125rem",
#         "padding": "0.4375rem 0.625rem",
#     },
#     "active": {
#         "background-color": "rgb(70, 70, 75)",
#     },
#     "hover": {
#         "background-color": "rgb(58, 58, 63)",
#     },
# }

# # Include the smirk cat icon in the "Home" label
# pages = [smirk_cat, "Sandbox", "About", "Contact Us"]

# # Use st_navbar to render the navigation bar
# page = st_navbar(pages=pages, styles=styles)

current_page = get_current_page_from_navbar()

# Navigation based on the page selected
if current_page == "Home":
    main_page()
elif current_page == "Sandbox":
    sandbox_page()
elif current_page == "About":
    about_page()
elif current_page == "Contact Us":
    contact_page()
