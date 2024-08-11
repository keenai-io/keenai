import streamlit as st
from tabledai import PostgresDB
import json
from streamlit_option_menu import option_menu
import pandas as pd

def test_page():
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'responses' not in st.session_state:
        st.session_state.responses = {"Answer": [], "SQL": [], "JSON": []}
    if 'current_question' not in st.session_state:
        st.session_state.current_question = ""
    
    def handle_input():
        user_input = st.session_state.user_input
        if user_input:
            st.session_state.responses = {"Answer": [], "SQL": [], "JSON": []}
            st.session_state.history.append(("User", user_input))
            st.session_state.current_question = user_input

            db = PostgresDB(name="demo_music")
            resp = db.query(user_input, generative=True)

            if 'generation' in resp:
                st.session_state.responses["Answer"].append(resp.get('generation'))
            st.session_state.responses["SQL"].append(resp.get('sql'))
            st.session_state.responses["JSON"].append(json.dumps(resp, indent=4))

            st.session_state.history.append(("AI", resp))
            st.session_state.user_input = ""

    # Sidebar navigation
    with st.sidebar:
        selected = option_menu(
            "KeenAI Sandbox",
            ["Home", "View Data", "Ask Question"],
            icons=["house", "table", "question-circle"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Home":
        st.title("Welcome to the KeenAI Sandbox")
        st.write("Look through the dataset in 'View Data', then ask some data-related questions.")

    elif selected == "View Data":
        df = pd.read_csv("data/pg_music_slim.csv")
        st.title("Spotify Charts Data")
        st.write("This dataset contains Spotify streaming data for popular top 200 songs.")
        st.write(df)


    elif selected == "Ask Question":
        st.title("Spotify Charts Data")
        user_input = st.text_input("Ask a question:", "", key='user_input', on_change=handle_input)

        if st.session_state.current_question:
            st.markdown("### Question")
            st.text(st.session_state.current_question)

        if any(st.session_state.responses.values()):
            tabs = ["SQL", "JSON"]
            if st.session_state.responses["Answer"]:
                tabs.insert(0, "Answer")

            tab_objects = st.tabs(tabs)

            if "Answer" in tabs:
                with tab_objects[0]:
                    st.session_state.tab_selection = 'Answer'
                    for answer in st.session_state.responses["Answer"]:
                        st.markdown(f"{answer}")

            with tab_objects[tabs.index("SQL")]:
                st.session_state.tab_selection = 'SQL'
                for sql in st.session_state.responses["SQL"]:
                    st.markdown(f"{sql}")

            with tab_objects[tabs.index("JSON")]:
                st.session_state.tab_selection = 'JSON'
                for json_response in st.session_state.responses["JSON"]:
                    st.json(json.loads(json_response))