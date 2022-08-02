import streamlit as st
import json
import requests as re

st.title("Text Summarizer App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This Text Summarizer app uses the WordsAI API to summarize a block of text
""")
texts = st.text_input("Input text: ")
# make a post request to the fastapi server

if st.button ("Get Summary"):
    response = re.post("http://wordsai-api.herokuapp.com/summarize"+"?text="+texts)
    response_json = response.json()
    st.write(response_json)