from pyairtable import Table
import streamlit as st

BASE_ID = st.secrets["base_id"]
API_KEY = st.secrets["api_key"]
TABLE_NAME = "Results"

table = Table(API_KEY, BASE_ID, TABLE_NAME)

def save_result(name: str, score: int):
    """Save quiz results to Airtable."""
    table.create({
        "Name": name,
        "Score": score
    })
