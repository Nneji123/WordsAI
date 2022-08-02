import json
import os

import requests as re

import streamlit as st

st.title("Speech to Text App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This speech to text app uses the WordsAI API to get the text from a wav file
""")

# write a file uploader using st.file_uploader
wav_file = st.file_uploader("Upload a wav file", type=["wav"])
# save the file to a temporary directory
if st.button ("Get text"):
    if wav_file is not None:
        files = wav_file.read()
        # save the file
        filename = "./temp/temp.wav"
        with open(filename, "wb+") as f:
            f.write(files)
        # make a post request to the fastapi server
        response = re.post("http://wordsai-api.herokuapp.com/speech_to_text", files={"file": open("./temp/temp.wav", "rb")})
        response_json = response.json()
        st.write(response_json)
