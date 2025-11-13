import streamlit as st # for web Ui with Python
from utils import generate_question, check_answer # import custom modules

st.title("Times Tables Quiz")

# Generate a question when the app first loads
if "question" not in st.session_state:
    num1, num2, answer = generate_question()
    st.session_state.question = (num1, num2, answer)

num1, num2, correct_answer = st.session_state.question

st.write(f"What is {num1} × {num2}?")

user_answer = st.number_input("Your answer:", step=1)

if st.button("Check"):
    if check_answer(user_answer, correct_answer):
        st.success("Correct!")
    else:
        st.error("Try again.")