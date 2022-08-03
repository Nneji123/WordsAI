import base64
import io
import os
import random
import string
from io import BytesIO

import cv2
import nltk
import numpy as np
import pocketsphinx
import pytesseract
import spacy
import speech_recognition as sr
import sphinxbase
from autocorrect import Speller
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (FileResponse, PlainTextResponse,
                               StreamingResponse)
from fastapi.templating import Jinja2Templates
from gensim.summarization import summarize
from nltk.tokenize import sent_tokenize
from PIL import Image
from pyresparser import ResumeParser
from starlette.requests import Request
from translate import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import STOPWORDS, WordCloud

nltk.download('words')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('punkt_tokenizer')
nltk.download('universal_tagset')


def get_translation(language: str, text: str) -> str:
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return "The translation of the text is: " + translation


def get_sentiment(text: str) -> str:
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(text)
    sentiment = None
    if result["compound"] >= 0.05:
        sentiment = "Positive"
    elif result["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return f"The sentiment of the text is: {sentiment} and the Score is: {round(result['compound'], 2)}"


def wordcloud(text):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          stopwords=stopwords,
                          min_font_size=10).generate(text).to_image()
    img = BytesIO()
    wordcloud.save(img, "PNG")
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode()
    return img_b64


def get_autocorrect(language: str, text: str) -> str:
    spell = Speller(language)
    result = spell(text)
    return "The autocorrected text is: " + result


def get_named_entity_recognition(text: str) -> str:

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(X.text, X.label_) for X in doc.ents]
