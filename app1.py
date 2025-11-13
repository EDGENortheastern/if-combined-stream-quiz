import streamlit as st
from welcome import welcome_screen
from quiz import quiz_screen
from results import results_screen

if "screen" not in st.session_state:
    st.session_state.screen = "welcome"

if st.session_state.screen == "welcome":
    welcome_screen()
elif st.session_state.screen == "quiz":
    quiz_screen()
elif st.session_state.screen == "results":
    results_screen()
