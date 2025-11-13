import streamlit as st

def results_screen():
    st.title("Quiz Complete 🎉")

    score = st.session_state.score
    name = st.session_state.name

    st.write(f"**{name}**, you scored **{score}/10**!")

    # placeholder for pie chart and Airtable
    st.write("(Pie chart will go here)")

    if st.button("Play again"):
        reset_quiz()
        st.rerun()


def reset_quiz():
    for key in ["screen", "name", "score", "question_number", "question"]:
        if key in st.session_state:
            del st.session_state[key]
