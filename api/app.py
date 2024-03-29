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
from better_profanity import profanity
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# route for generating wordcloud and a more accurate summarizer
from fastapi import FastAPI, File, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (FileResponse, PlainTextResponse,
                               StreamingResponse)
from nltk.tokenize import sent_tokenize
from PIL import Image
from pyresparser import ResumeParser
from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.abstractabledoc.top_n_rank_abstractor import \
    TopNRankAbstractor
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.web_scraping import WebScraping
from starlette.requests import Request
from translate import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import STOPWORDS, WordCloud

app = FastAPI(
    title="WordsAI API",
    description="""A collection of NLP Applications served as APIs using FastAPI.""",
    version="0.0.1",
    debug=True,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

favicon_path = "./images/favicon.ico"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/", response_class=PlainTextResponse, tags=["home"])
async def home():
    """
    The home function returns a welcome message and some instructions.

    Args:

    Returns:
        A note that is displayed when the user accesses the root of our api
    """
    note = """
    WordsAI API 📚
    A collection of NLP Applications served as APIs using FastAPI!
    Note: add "/redoc" to get the complete documentation.
    """
    return note


# Sentiment Route
@app.post("/sentiment")
async def get_sentiment(text: str) -> str:
    """
    The get_sentiment function accepts a string as an argument and returns the sentiment of that string.
    The function uses the VADER SentimentIntensityAnalyzer to determine if the text is positive, negative, or neutral.

    Args:
        text:str: Pass in the text that is being analyzed

    Returns:
        A string that is either positive, negative or neutral

    """
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


@app.post("/summarize")
async def get_summary(text: str) -> dict:
    """
    The get_summary function accepts a string of text and returns a dictionary with the following keys:
        - summary_list: A list of strings containing the most important sentences in the document.
        - title_string: The first sentence in the document, which is usually used as a title.


    Args:
        text:str: Pass in the text that is to be summarized

    Returns:
        A dictionary with the following keys:

    """
    auto_abstractor = AutoAbstractor()

    auto_abstractor.tokenizable_doc = SimpleTokenizer()

    auto_abstractor.delimiter_list = [".", "\n"]

    abstractable_doc = TopNRankAbstractor()

    result_dict = auto_abstractor.summarize(text, abstractable_doc)
    return result_dict


@app.post("/summarize_webpage")
async def get_summary_webpage(url):
    """
    The get_summary_webpage function scrapes a webpage and summarizes it.
    It returns a dictionary with the following keys:
        - summary_list: A list of strings containing the most important sentences in the document.
        - title_string: The first sentence in the document, which is usually used as a title.
    Args:
        url: Specify the url of the website to be summarized

    Returns:
        The summarized text
    """
    # Object of web scraping.
    web_scrape = WebScraping()
    # Web-scraping.
    document = web_scrape.scrape(url)

    # Object of automatic summarization.
    auto_abstractor = AutoAbstractor()
    # Set tokenizer.
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    # Set delimiter.
    auto_abstractor.delimiter_list = [".", "\n"]
    # Object of abstracting and filtering document.
    abstractable_doc = TopNRankAbstractor()
    # Summarize document.
    result_dict = auto_abstractor.summarize(document, abstractable_doc)

    # Output 3 summarized sentences.
    limit = 3
    i = 1
    for sentence in result_dict["summarize_result"]:
        print(sentence)
        if i >= limit:
            break
        i += 1
    return result_dict


@app.post("/translate")
async def get_translation(language: str, text: str) -> str:
    """
    The get_translation function accepts a string as an argument and returns the translation of that string.
    The function uses the Translator library to translate the text.
    Languages available:
        - af: Afrikaans
        - sq: Albanian
        - ar: Arabic
        - hy: Armenian
        - az: Azerbaijani
        - eu: Basque
        - be: Belarusian
        - bg: Bulgarian
        - ca: Catalan
        - zh-CN: Chinese (Simplified)
        - zh-TW: Chinese (Traditional)
        - hr: Croatian
        - cs: Czech
        - da: Danish
        - nl: Dutch
        - en: English
        - et: Estonian
        - fi: Finnish
        - fr: French
        - gl: Galician
        - ka: Georgian
        - de: German
        - el: Greek
        - gu: Gujarati
        - he: Hebrew
        - hi: Hindi
        - hu: Hungarian
        - is: Icelandic
        and many more...
    Args:
        text:str: Pass in the text that is to be translated

    Returns:
        A string that is the translation of the text

    """
    # add a function to select the language
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return "The translation of the text is: " + translation


# add autocorrect route
@app.post("/autocorrect")
async def get_autocorrect(language: str, text: str) -> str:
    """
    The get_autocorrect function accepts a string as an argument and returns the autocorrected text.
    The function uses the AutoCorrect library to autocorrect the text.
    Currently supports English, Polish, Turkish, Russian, Ukrainian, Czech, Portuguese, Greek, Italian, Vietnamese, French and Spanish, but you can easily add new languages.
    Args:
        text:str: Pass in the text that is to be autocorrected

    Returns:
        A string that is the autocorrected text
    """
    spell = Speller(language)
    result = spell(text)
    return "The autocorrected text is: " + result


# create a route for optical character recognition
@app.post("/ocr")
async def get_ocr(file: UploadFile = File(...)):
    """
    The get_ocr function accepts an image as an argument and returns the text extracted from the image.
    The function uses the OCR library to extract text from the image.
    Args:
        image: UploadFile: Pass in the image that is to be extracted

    Returns:
        A string that is the text extracted from the image
    """
    contents = io.BytesIO(await file.read())
    file_bytes = np.asarray(bytearray(contents.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    # Converting image to array
    image_arr = np.array(img)
    # Converting image to grayscale
    gray_img_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2GRAY)
    # Converting image back to rbg
    image = Image.fromarray(gray_img_arr)

    # Extracting text from image
    custom_config = r"-l eng --oem 3 --psm 6"
    text = pytesseract.image_to_string(image, config=custom_config)

    # Remove symbol if any
    characters_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
    new_string = text
    for character in characters_to_remove:
        new_string = new_string.replace(character, "")

    # Converting string into list to dislay extracted text in seperate line
    new_string = new_string.split("\n")
    return new_string


@app.post("/resume_parser")
async def resume_parser(file: UploadFile) -> str:
    """
    The resume_parser function takes a file path to a resume as an argument and returns the parsed data as a dictionary.
    The returned dictionary contains the following fields:
    name, email, phone_number, work_experience (a list of dictionaries), skills (a list).


    Args:
        file:UploadFile: Pass the file that is uploaded to the function

    Returns:
        A string of the file name
    """
    # write a function to save the uploaded file and return the file name
    files = await file.read()
    # save the file
    filename = "./temp/file.pdf"
    with open(filename, "wb+") as f:
        f.write(files)
    # open the file and return the file name

    with open(filename, "rb") as f:
        pdf = f.read()
    data = ResumeParser(filename).get_extracted_data()
    return data


@app.post("/speech_to_text")
async def speech_to_text(file: UploadFile = File(...)) -> str:
    """
    The speech_to_text function accepts an audio file and returns the text transcription of that file.


    Args:
        file:UploadFile=File(...): Pass the file that is uploaded to the function

    Returns:
        A string of the text transcribed from the audio file
    """
    files = await file.read()
    filename = "./temp/file.wav"
    with open(filename, "wb+") as f:
        f.write(files)

    r = sr.Recognizer()
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source)
    text = r.recognize_sphinx(audio)
    return text


@app.post("/wordcloud")
async def wordcloud(text):
    """
    The wordcloud function takes in a string of text and generates a wordcloud image.
    The function also saves the image to the images folder.

    Args:
        text: Pass in the text that will be used to create the wordcloud

    Returns:
        A wordcloud image
    """
    stopwords = set(STOPWORDS)
    wordcloud = (
        WordCloud(
            width=400,
            height=400,
            background_color="white",
            stopwords=stopwords,
            min_font_size=10,
        )
        .generate(text)
        .to_image()
    )
    wordcloud.save("./images/wordcloud.png")

    return FileResponse("./images/wordcloud.png", media_type="image/png")


@app.post("/named_entity_recognition")
async def named_entity_recognition(text: str) -> str:

    """
    The named_entity_recognition function takes in a string of text and returns the named entities in the text.
    The function uses the NLTK library to extract the named entities.
    Args:
        text:str: Pass in the text that is to be parsed

    Returns:
        A string of the named entities in the text
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(X.text, X.label_) for X in doc.ents]


# create a bot instance
bot = ChatBot(
    "WordsAI",
    preprocessors=["chatterbot.preprocessors.clean_whitespace"],
    logic_adapters=["chatterbot.logic.BestMatch", "chatterbot.logic.TimeLogicAdapter"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
)


# train the bot
trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("./train_bot/convo.yml", "chatterbot.corpus.english.greetings",
#              "chatterbot.corpus.english.conversations")


# create a post route
@app.post("/bot", tags=["WordsAI Bot"])
async def get_response(text: str) -> dict:
    answer = bot.get_response(text)
    return {"WordsAI": str(answer)}


@app.post("/wordcloud_streamlit")
async def wordcloud(text):
    """
    The wordcloud function takes in a string of text and generates a wordcloud image.
    The function also saves the image to the images folder.

    Args:
        text: Pass in the text that will be used to create the wordcloud

    Returns:
        A wordcloud image
    """
    stopwords = set(STOPWORDS)
    wordcloud = (
        WordCloud(
            width=400,
            height=400,
            background_color="white",
            stopwords=stopwords,
            min_font_size=10,
        )
        .generate(text)
        .to_image()
    )
    img = BytesIO()
    wordcloud.save(img, "PNG")
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode()
    return img_b64


@app.post("/profanity")
async def profanity(text: str) -> str:
    """
    The profanity function takes in a string of text and returns a string of the profanity words in the text.
    The function uses the profanity library to extract the profanity words.
    Args:
        text:str: Pass in the text that is to be parsed

    Returns:
        A string of the profanity words in the text
    """
    profanity_words = profanity.censor(text)
    return profanity_words
