import base64
import json

import requests as re

import streamlit as st

st.title("Wordcloud Generator App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This wordcloud generator app uses the WordsAI API to generate a wordcloud
""")
texts = st.text_input("Input text: ")
# make a post request to the fastapi server

if st.button ("Get Wordcloud"):
    response = re.post("http://wordsai-api.herokuapp.com/wordcloud_streamlit"+"?text="+texts)
    # get the response and convert the base64 string to a png image
    response_json = response.json()
    img = base64.b64decode(response_json)
    st.image(img, width=300)
    