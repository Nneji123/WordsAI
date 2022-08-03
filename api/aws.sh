#!/bin/bash
# Update and install requirements
sudo apt-get update
sudo apt install -y uvicorn
sudo apt install -y python3-pip nginx tesseract-ocr portaudio19-dev swig libpulse-dev pocketsphinx
# Copy the configuration file to the nginx enabled sites folder
sudo cp -R fastapi_setup /etc/nginx/sites-enabled/
sudo service nginx restart
cd ~/WordsAI
# Install FastAPI application requirements
pip3 install -r requirements.txt.txt
pip3 install nltk
pip3 install spacy==2.3.5
pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz
python3 -m spacy download en_core_web_sm
python3 -m nltk.downloader words 
python3 -m nltk.downloader stopwords
# Kill any service running on port 80
sudo kill -9 $(sudo lsof -t -i:80)
sudo service nginx restart
# Run the application with nohup so the application runs as a background process
sudo fallocate -l 3G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo free -h
cat /proc/sys/vm/swappiness
nohup uvicorn app:app --reload --host 0.0.0.0