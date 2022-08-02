import json
import os

import requests as re

import streamlit as st

st.title("Optical Character Recognition App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This Optical Character Recognition app uses the WordsAI API to recognize characters in a text
""")

# write a file uploader using st.file_uploader
wav_file = st.file_uploader("Upload an image file", type=["png", "jpg", "jpeg", "gif", "webp"])
# save the file to a temporary directory
if st.button ("Get Text"):
    if wav_file is not None:
        files = wav_file.read()
        # save the file
        filename = "./temp/temp2.png"
        with open(filename, "wb+") as f:
            f.write(files)
        # make a post request to the fastapi server
        response = re.post("http://wordsai-api.herokuapp.com/ocr", files={"file": open("./temp/temp2.png", "rb")})
        response_json = response.json()
        st.write(response_json)

