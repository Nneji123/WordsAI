from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pysummarization.web_scraping import WebScraping
from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from translate import Translator
from autocorrect import Speller
import os
import cv2
import numpy as np
from PIL import Image
import random
import string
import pytesseract


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



#create a route for optical character recognition
@app.post("/ocr")
async def get_ocr(image: UploadFile = File(...)):
    """
    The get_ocr function accepts an image as an argument and returns the text extracted from the image.
    The function uses the OCR library to extract text from the image.
    Args:
        image: UploadFile: Pass in the image that is to be extracted
    
    Returns:
        A string that is the text extracted from the image
    """
    # read the image
    img = image.file.read()
    # convert the image to a numpy array
    img = np.frombuffer(img, dtype=np.uint8)
    # convert the numpy array to a cv2 image
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # convert the image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # apply thresholding to the image
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # apply dilation and erosion to remove noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # apply contour detection to extract the text
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # sort the contours by area
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    # create a mask for the contour
    mask = np.zeros(img.shape, np.uint8)
    # create a bounding rectangle for the contour
    x, y, w, h = cv2.boundingRect(contours[0])
    # create a new image with the bounding rectangle
    new_img = img[y:y + h, x:x + w]
    # create a new image with the bounding rectangle
    new_img = cv2.bitwise_not(new_img)
    # create a new image with the bounding rectangle
    new_img = cv2.bitwise_not(new_img)

	# Execute if request is get
	if request.method == "GET":
		full_filename =  'images/white_bg.jpg'
		return render_template("index.html", full_filename = full_filename)

	# Execute if reuqest is post
	if request.method == "POST":
		image_upload = request.files['image_upload']
		