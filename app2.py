import streamlit as st
from airtable_client import save_result

st.title("Airtable Test")

name = st.text_input("Enter a test name", "TestUser")
score = st.number_input("Enter a test score", 0, 10)

if st.button("Send to Airtable"):
    save_result(name, score)
    st.success("Sent! Check your Airtable base.")
