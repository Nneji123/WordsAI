#!/bin/bash
sudo apt-get -y update  && sudo apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  tesseract-ocr \
  portaudio19-dev \
  swig \
  libpulse-dev \
  pocketsphinx \

pip install chatterbot==1.0.4
pip install spacy==2.3.5 
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz 
pip install pyresparser 

python -m spacy download en_core_web_sm 
python -m nltk.downloader words 
python -m nltk.downloader stopwords 
python -m nltk.downloader punkt 
pip install --upgrade numpy
pip install fastapi[all]
#pip install -r requirements.txt 
