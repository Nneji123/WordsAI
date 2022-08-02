import json

import requests as re

import streamlit as st

st.title("Sentiment Analyzer App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This sentiment analyzer app uses the WordsAI API to get the sentiments of a text
""")

texts = st.text_input("Input text: ")
# make a post request to the fastapi server

if st.button ("Get sentiment"):
    response = re.post("http://wordsai-api.herokuapp.com/sentiment"+"?text="+texts)
    response_json = response.json()
    st.write(response_json)