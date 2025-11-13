import streamlit as st
from welcome import welcome_screen
from quiz import quiz_screen
from results import results_screen   # you will create this soon


def main():
    if "screen" not in st.session_state:
        st.session_state.screen = "welcome"

    screen = st.session_state.screen

    if screen == "welcome":
        welcome_screen()

    elif screen == "quiz":
        quiz_screen()

    elif screen == "results":
        results_screen()


if __name__ == "__main__":
    main()
