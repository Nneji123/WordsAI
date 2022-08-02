#!/bin/bash
pip install nltk
pip install spacy==2.3.5
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
pip install pyresparser
python -m spacy download en_core_web_sm
python -m nltk.downloader words 
python -m nltk.downloader stopwords
python -m nltk.downloader punkt
gunicorn -w 3 -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:$PORT