import streamlit as st
import json
import requests as re

st.title("Translation App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This translation app uses the WordsAI API to translate a text
""")

texts = st.text_input("Input text: ")
language = st.selectbox("Select language", ["zh", "de", "es", "fr", "it", "pt", "ru", "tr"])
# make a post request to the fastapi server

if st.button ("Get Translation"):
    response = re.post("http://wordsai-api.herokuapp.com/translate"+"?language="+language+"&text="+texts)
    response_json = response.json()
    st.write(response_json)