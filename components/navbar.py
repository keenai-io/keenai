from streamlit_navigation_bar import st_navbar

def get_current_page_from_navbar():
    smirk_cat = "😼"
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

    # Include the smirk cat icon in the "Home" label
    pages = ["Home", "Sandbox", "About", "Contact Us"]

    # Use st_navbar to render the navigation bar
    page = st_navbar(pages=pages, styles=styles)

    return page