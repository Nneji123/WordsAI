import json
import os

import requests as re

import streamlit as st

st.title("Resume Parser App using WordsAI")

st.image("./images/logo.png")

st.write("""
## About
This Resume Parser app uses the WordsAI API to parse a resume
""")

# write a file uploader using st.file_uploader
wav_file = st.file_uploader("Upload a wav file", type=["pdf"])
# save the file to a temporary directory
if st.button ("Get Parsed Resume"):
    if wav_file is not None:
        files = wav_file.read()
        # save the file
        filename = "./temp/temp.pdf"
        with open(filename, "wb+") as f:
            f.write(files)
        # make a post request to the fastapi server
        response = re.post("http://wordsai-api.herokuapp.com/resume_parser", files={"file": open("./temp/temp.pdf", "rb")})
        response_json = response.json()
        st.write(response_json)

