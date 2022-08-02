import json

import requests as re

import streamlit as st

st.title("Webpage Summarizer App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This webpage summarizer app uses the WordsAI API to summarize a webpage
""")
texts = st.text_input("Input text: ")
# make a post request to the fastapi server

if st.button ("Get Summary"):
    response = re.post("http://wordsai-api.herokuapp.com/summarize_webpage"+"?url="+texts)
    response_json = response.json()
    st.write(response_json)