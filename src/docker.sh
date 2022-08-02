#!/bin/bash


python -m spacy download en_core_web_sm 
python -m nltk.downloader words 
python -m nltk.downloader stopwords 
python -m nltk.downloader punkt 

uvicorn app:app --host 0.0.0.0 --port 8000 --reload