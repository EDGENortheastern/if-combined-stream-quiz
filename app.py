import streamlit as st

st.title("Times Tables Quiz")

st.write("Welcome to the quiz!")

# One hard-coded question for now
number1 = 3
number2 = 4

answer = st.number_input("What is 3 × 4?", step=1)

if st.button("Check answer"):
    if answer == number1 * number2:
        st.success("Correct!")
    else:
        st.error("Try again.")
