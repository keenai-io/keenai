import logging
import streamlit as st
from components._partials.navbar import get_current_page_from_navbar
from components.main_page import main_page
from components.sandbox_page import sandbox_page
from components.about_page import about_page
from components.contact_page import contact_page
from components._partials.footer import add_footer

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Set layout to 'wide' for better mobile responsiveness
st.set_page_config(page_title="KeenAI", page_icon="./static/img/favicon.ico", layout="wide")

# Ensure the navbar is responsive (this part may require custom CSS)
current_page = get_current_page_from_navbar()

if current_page == "Home":
    main_page()
elif current_page == "Sandbox":
    sandbox_page()
elif current_page == "About":
    about_page()
elif current_page == "Contact Us":
    contact_page()

add_footer()

# Optionally, you can add custom CSS for better mobile support
st.markdown(
    """
    <style>
    /* Responsive text scaling */
    body, h1, h2, h3, h4, h5, h6 {
        font-size: calc(12px + 0.5vw);
    }

    /* Navbar responsiveness */
    .navbar {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
    }

    @media only screen and (max-width: 600px) {
        .navbar {
            flex-direction: column;
        }

        .navbar-item {
            font-size: 14px;
        }
    }

    /* Ensure all elements scale with screen size */
    .container, .main {
        max-width: 100%;
        padding: 0 5%;
    }

    .footer {
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True
)