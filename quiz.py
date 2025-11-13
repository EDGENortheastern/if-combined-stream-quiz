import streamlit as st
import random
from utils import generate_question
from airtable_client import save_result


def quiz_screen():
    """
    Main quiz screen: shows questions until 10 have been asked.
    After 10 questions, shows final score and saves to Airtable.
    """

    # If we've already done 10 questions, show the end screen
    if st.session_state.question_number > 10:
        end_of_quiz()
        return

    # --- 1. Process any pending answer from the previous click ---
    # We do this BEFORE drawing the next question, to avoid skipped/ignored answers.
    if "pending_choice" in st.session_state and st.session_state.pending_qnum == st.session_state.question_number:
        num1, num2, correct = st.session_state.question
        choice = st.session_state.pending_choice

        _handle_answer(choice, correct)

        # Clear pending state so it doesn't process twice
        del st.session_state.pending_choice
        del st.session_state.pending_qnum

        st.rerun()
        return

    # --- 2. Normal question display ---
    st.title(f"Question {st.session_state.question_number} of 10")

    # Current question
    num1, num2, correct = st.session_state.question
    st.write(f"What is {num1} × {num2}?")

    # Generate 4 answer choices
    choices = [correct]
    while len(choices) < 4:
        wrong = random.randint(1, 144)
        if wrong not in choices:
            choices.append(wrong)
    random.shuffle(choices)

    cols = st.columns(2)
    for i, choice in enumerate(choices):
        with cols[i % 2]:
            label = str(choice)
            key = f"q{st.session_state.question_number}_choice{i}"
            if st.button(label, key=key):
                # Store the choice and process it on the next rerun
                st.session_state.pending_choice = choice
                st.session_state.pending_qnum = st.session_state.question_number
                st.rerun()
                return


def _handle_answer(choice, correct):
    """Update score and move to the next question."""
    if choice == correct:
        st.session_state.score += 1

    # Always move to the next question (even if wrong)
    st.session_state.question_number += 1

    # If there are still questions to ask, generate a new one
    if st.session_state.question_number <= 10:
        st.session_state.question = generate_question()
    # If > 10, quiz_screen will show end_of_quiz next time


def end_of_quiz():
    """Show final score and automatically save to Airtable."""
    st.title("Quiz Complete!")

    score = st.session_state.score
    name = st.session_state.name

    st.subheader(f"Your score: {score} / 10")

    # Save only once
    if "saved_to_airtable" not in st.session_state:
        save_result(name, score)
        st.session_state.saved_to_airtable = True
        st.success("Your score has been saved to Airtable ✔")

    if st.button("Play Again"):
        reset_quiz()


def reset_quiz():
    """Reset quiz state and restart."""
    st.session_state.question_number = 1
    st.session_state.score = 0
    st.session_state.question = generate_question()
    st.session_state.screen = "quiz"
    st.rerun()
