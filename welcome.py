import streamlit as st
from utils import generate_question

def welcome_screen():
    st.title("Times Tables Quiz 🎯")

    # Store name in session_state instantly when typed
    name = st.text_input("Enter your name:")
    st.session_state.name = name

    if st.button("Start Quiz"):
        if not name.strip():
            st.error("Please enter your name.")
            return

        # Initialise quiz state
        st.session_state.score = 0
        st.session_state.question_number = 1
        st.session_state.question = generate_question()
        st.session_state.screen = "quiz"

        st.rerun()
