FROM python:3.8.13-slim-buster

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  tesseract-ocr \
  portaudio19-dev \
  swig \
  libpulse-dev \
  pocketsphinx \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools 
    
COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

CMD ./setup.sh