<p align="center">
  <img width="300" height="300" src="https://user-images.githubusercontent.com/101701760/182023528-7da7205e-1fc6-49c9-832d-b3f40a68eae8.png">
</p>


[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/Keras-darkred.svg?style=flat&logo=keras&logoColor=white)](http://www.Keras.org/news.html)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://lung-cancer-api.herokuapp.com/docs)
[![Framework](https://img.shields.io/badge/Tensorflow-orange.svg?style=flat&logo=tensorflow&logoColor=white)](https://share.streamlit.io/nneji123/lung-cancer-prediction/main)
![hosted](https://img.shields.io/badge/Heroku-430098?style=flat&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)
![Gitpod](https://img.shields.io/badge/Gitpod-orange?style=flat&logo=gitpod&logoColor=white)
![reposize](https://img.shields.io/github/repo-size/Nneji123/Plant-Disease-Detection-Keras)


## Table of Contents
- [Table of Contents](#table-of-contents)
- [Repository File Structure](#repository-file-structure)
- [About](#about)
  * [Features](#features)
- [How to run the Application](#how-to-run-the-application)
  * [Running on Local Machine](#running-on-local-machine)
  * [Running on Local Machine with Docker Compose](#running-on-local-machine-with-docker-compose)
  * [Running in a Gitpod Cloud Environment](#running-in-a-gitpod-cloud-environment)
- [Deployment](#deployment)
  * [Deploying the Application to Heroku](#deploying-the-application-to-heroku)
  * [How to deploy the application on AWS EC2 using a Bash Script](#how-to-deploy-the-application-on-aws-ec2-using-a-bash-script)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>




## Repository File Structure
```bash
├── app.py # main fastapi app
├── aws.txt # requirements for deploying on aws
├── docker-compose.yml # for running docker compose
├── Dockerfile
├── download.py # script to download model hosted on google drive
├── fastapi_setup # for deploying on aws
├── LICENSE
├── Notebook #Notebook folder
   └── plant_disease_detection.ipynb
├── README.md
├── requirements.txt
├── Research_Papers
│   └── R_paper1.pdf
├── setup.sh # bash script for deploying on aws ec2
└── test_images # test images for inference
    ├── 8fd27998ae52a4a6.jpg
    ├── 9be41b823d13e3c6.jpg
    └── 9d0f6e60819f9a5a.jpg
```




## About

### Features




## How to run the Application
### Running on Local Machine
**To run the application on your local system do the following:**
1. Clone the repository:
```bash
git clone https://github.com/Nneji123/Plant-Disease-Detection-Keras.git
```

2. Change the directory:
```
cd Plant-Disease-Detection-Keras
```

3. Install the requirements:
```
pip install -r requirements.txt
```

4. Download the model from google drive
```
python download.py
```
5. Run the application
```
uvicorn app:app --reload --port 8000
```
**You should be able to view the application by going to http://127.0.0.1:8000/**

### Running on Local Machine with Docker Compose
**You can also run the application in a docker container using docker compose(if you have it installed)**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/Plant-Disease-Detection-Keras.git
```

2. Change the directory:
```
cd Plant-Disease-Detection-Keras
```

3. Download the model:
```bash
pip install gdown
python download.py
```

4. Run the docker compose command
```docker
docker compose up -d --build 
```
You should be able to view the application by going to http://localhost:8000/

### Running in a Gitpod Cloud Environment

**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Nneji123/Plant-Disease-Detection-Keras)

## Deployment
### Deploying the Application to Heroku
**Assuming you have git and heroku cli installed just carry out the following steps:**

1. Clone the repository:
```bash
git clone https://github.com/Nneji123/Plant-Disease-Detection-Keras.git
```

2. Change the directory:
```
cd Plant-Disease-Detection-Keras
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

### How to deploy the application on AWS EC2 using a Bash Script
**1. Fork this repository**

**2. Login to AWS, create a new AWS EC2 instance and make sure to allow outside traffic as shown in the screenshots below:**

<img src="https://user-images.githubusercontent.com/101701760/178163392-3c9fc8ec-e58a-420d-a6bb-2885215d8105.png" width="1200" height="400">


<img src="https://user-images.githubusercontent.com/101701760/178163373-e4bb2c92-0f47-4a22-9556-dfc470fd7e8a.png" width="1200" height="400">


**3. When the instance has been launched, copy the Public IP address of your instance and paste it in the 'fastapi_setup' file of your cloned repository as shown below**

<img src="https://user-images.githubusercontent.com/101701760/178163457-2e156379-b542-4d24-aebf-e202dd44ae2c.png" width="1200" height="400">

<img src="https://user-images.githubusercontent.com/101701760/178163536-918818ee-563d-4b0d-a5ec-5c265a75b2b4.png" width="1200" height="400">


**4. Connect to your instance and clone your forked repository, an example in my case:**
```bash
git clone https://github.com/Nneji123/Plant-Disease-Detection-Keras.git
```
**5. cd into your repository which is probably named 'Plant-Disease-Detection-Keras'. You can do that by running:**
```bash
cd Plant-Disease-Detection-Keras 
```
**6. Then run the setup.sh file to get your application up and running:**
```bash
chmod u+x setup.sh
./setup.sh
```
**You can then view the application by going to your Public IP's location, an example in my case will be:
http://3.95.202.74:80/docs**

**You can also watch this video for a more in depth explanation on how to deploy a FastAPI application on AWS EC2:**
[![How to deploy FastAPI on AWS](https://youtube-md.vercel.app/SgSnz7kW-Ko/640/360)](https://www.youtube.com/watch?v=SgSnz7kW-Ko)









