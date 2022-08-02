#!/bin/bash 

python -m nltk.downloader words 
python -m nltk.downloader stopwords 
python -m nltk.downloader punkt 
python -m nltk.downloader wordnet
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader maxent_treebank_pos_tagger
python -m nltk.downloader punkt_tokenizer
python -m nltk.downloader universal_tagset


gunicorn -w 3 -k uvicorn.workers.UvicornWorker app:app --bind 0.0.0.0:$PORT