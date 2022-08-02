import streamlit as st
import json
import requests as re

st.title("AutoCorrect App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This AutoCorrect app uses the WordsAI API to get the sentiments of a text
""")

texts = st.text_input("Input text: ")
language = st.selectbox("Select language", ["en", "de", "es", "fr", "it", "pt", "ru", "tr"])
# make a post request to the fastapi server

if st.button ("Get Autocorrect"):
    response = re.post("http://wordsai-api.herokuapp.com/autocorrect"+"?language="+language+"&text="+texts)
    response_json = response.json()
    st.write(response_json)