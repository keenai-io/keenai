import streamlit as st
from streamlit_navigation_bar import st_navbar

def get_current_page_from_navbar():
    styles = {
        "nav": {
            "background-color": "rgb(36, 37, 42)",
        },
        "div": {
            "max-width": "32rem",
        },
        "span": {
            "border-radius": "0.5rem",
            "color": "rgb(255, 255, 255)",
            "margin": "0 0.125rem",
            "padding": "0.4375rem 0.625rem",
        },
        "active": {
            "background-color": "rgb(70, 70, 75)",
        },
        "hover": {
            "background-color": "rgb(58, 58, 63)",
        },
    }
    options = {
        "show_menu": False,
    }

    pages = [
        "Home", 
        "Sandbox", 
        "About", 
        "Contact Us", 
        # "Test Page"
        ]

    page = st_navbar(pages=pages, styles=styles, options=options)
    return page