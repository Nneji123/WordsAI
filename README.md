<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/101701760/182023528-7da7205e-1fc6-49c9-832d-b3f40a68eae8.png">
</p>


[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://wordsai-api.herokuapp.com/docs)
[![Framework](https://img.shields.io/badge/Streamlit-darkred.svg?style=flat&logo=streamlit&logoColor=white)](https://share.streamlit.io/nneji123/lung-cancer-prediction/main)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)
[![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)](https://gitpod.io/#https://github.com/Nneji123/WordsAI)
![reposize](https://img.shields.io/github/repo-size/Nneji123/WordsAI)

## About
>WordsAI is a collection of NLP/text and audio based applications served as APIs using the FastAPI framework. Visit the official documentation website for more details [wordsai-api.herokuapp.com/redoc](wordsai-api.herokuapp.com/redoc)

Also you can visit this [link](https://nneji123-wordsai-streamlithome-x32anq.streamlitapp.com/) to play around with the APIs!

## Table of Contents
  * [About](#about)
    + [Features](#features)
  * [Repository File Structure](#repository-file-structure)
  * [Demo](#demo)
  * [How to run the Application](#how-to-run-the-application)
  * [Deployment](#deployment)
- [Todo](#todo)
- [License](#license)

### Features
- Speech Recognition
- Auto Correct
- Machine Translation across multiple languages
- Resume Parser
- Text Summarizer
- Webpage Summarizer
- Sentiment Analyzer
- Optical Character Recognition or OCR(extract text from images)
- Named Entity Recognizer
- Chatbot
- Wordcloud Generator

**Visit wordsai-app.herokuapp.com** to see all the available feautures!


## Repository File Structure
```bash
├───.github
│   └───workflows #Github Actions
├───api           #FastAPI Application
│   ├───images
│   ├───temp
│   └───train_bot
├───src           #HTML Web Application
│   ├───images
│   ├───temp
│   ├───templates
│   │   └───assets
│   └───__pycache__
├───streamlit     #Streamlit Application
│   ├───functions
│   ├───images
│   ├───pages
│   └───temp
└───tests         #Tests
```

## Demo

## How to run the Application
<details> 
  <summary><b>Running on Local Machine</b></summary>

**To run the application on your local system do the following:**
1. Clone the repository:
```bash
git clone https://github.com/Nneji123/WordsAI.git
```

2. Change the directory:
```
cd WordsAI
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Run the application
```
uvicorn app:app --reload --port 8000
```
**You should be able to view the application by going to http://127.0.0.1:8000/**
</details>

<details> 
  <summary><b>Running on Local Machine with Docker Compose</b></summary>

**You can also run the application in a docker container using docker compose(if you have it installed)**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/WordsAI.git
```

2. Change the directory:
```
cd WordsAI
```

3. Run the docker compose command
```docker
docker compose up -d --build 
```
You should be able to view the application by going to http://localhost:8000/
</details>


<details> 
  <summary><b>Running in a Gitpod Cloud Environment</b></summary>


**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Nneji123/WordsAI)
</details>

## Deployment

<details> 
  <summary><b>Deploying the Application to Heroku</b></summary>

**Assuming you have git and heroku cli installed just carry out the following steps:**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/WordsAI.git
```

2. Change the directory:
```
cd WordsAI
```

3. Login to Heroku

``` 
heroku login
heroku container:login
```

4. Create your application
```
heroku create your-app-name
```
Replace **your-app-name** with the name of your choosing.

5. Build the image and push to Container Registry:

```
heroku container:push web
```

6. Then release the image to your app:
 
```
heroku container:release web
```
</details>

<details> 
  <summary><b>How to deploy the application on AWS EC2 using a Bash Script</b></summary>

**1. Fork this repository**

**2. Login to AWS, create a new AWS EC2 instance and make sure to allow outside traffic as shown in the screenshots below:**

<img src="https://user-images.githubusercontent.com/101701760/178163392-3c9fc8ec-e58a-420d-a6bb-2885215d8105.png" width="1200" height="400">


<img src="https://user-images.githubusercontent.com/101701760/178163373-e4bb2c92-0f47-4a22-9556-dfc470fd7e8a.png" width="1200" height="400">


**3. When the instance has been launched, copy the Public IP address of your instance and paste it in the 'fastapi_setup' file of your cloned repository as shown below**

<img src="https://user-images.githubusercontent.com/101701760/178163457-2e156379-b542-4d24-aebf-e202dd44ae2c.png" width="1200" height="400">

<img src="https://user-images.githubusercontent.com/101701760/178163536-918818ee-563d-4b0d-a5ec-5c265a75b2b4.png" width="1200" height="400">


**4. Connect to your instance and clone your forked repository, an example in my case:**
```bash
git clone https://github.com/Nneji123/WordsAI.git
```
**5. cd into your repository which is probably named 'WordsAI'. You can do that by running:**
```bash
cd WordsAI 
```
**6. Then run the setup.sh file to get your application up and running:**
```bash
chmod u+x aws.sh
./aws.sh
```
**You can then view the application by going to your Public IP's location, an example in my case will be:
http://3.95.202.74:80/docs**

**You can also watch this video for a more in depth explanation on how to deploy a FastAPI application on AWS EC2:**
[![How to deploy FastAPI on AWS](https://youtube-md.vercel.app/SgSnz7kW-Ko/640/360)](https://www.youtube.com/watch?v=SgSnz7kW-Ko)
</details>

# Todo
- [x] Add a frontend interface for the APIs with streamlit and html, css , javascript
- [ ] Add more interesting features like; title generator and song finder, text2speech, pdf text extractor,  etc
- [x] Add functional chatbot

# License
[Apache License](https://github.com/Nneji123/WordsAI/LICENSE.md)









