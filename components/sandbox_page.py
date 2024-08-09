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

    # st.title("Sandbox")
    # st.write("""
    # Welcome to the Sandbox! This is a safe space to test out your SQL queries and see the results instantly.
    # Try out different queries and see how they interact with the database.
    # """)

    # with st.form("sandbox_form"):
    #     query = st.text_area("Enter your SQL query here")
    #     submitted = st.form_submit_button("Run Query")
    #     if submitted:
    #         # Execute the SQL query and display the results
    #         st.write("Query Results:")
    #         st.table([("ID", "Name", "Age"),
    #                   (1, "Alice", 25),
    #                   (2, "Bob", 30),
    #                   (3, "Charlie", 35)])