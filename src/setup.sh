#!/bin/bash
pip install chatterbot==1.0.4
pip install spacy==2.3.5 
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz 
pip install pyresparser 

python -m spacy download en_core_web_sm 
python -m nltk.downloader words 
python -m nltk.downloader stopwords 
python -m nltk.downloader punkt 
python -m nltk.downloader wordnet
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader maxent_treebank_pos_tagger
python -m nltk.downloader punkt_tokenizer
python -m nltk.downloader universal_tagset

pip install --upgrade numpy
pip install fastapi[all]

gunicorn -w 3 -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:$PORT