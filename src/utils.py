import base64
from io import BytesIO

import nltk
import spacy
from autocorrect import Speller
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from gensim.summarization import summarize
from nltk.tokenize import sent_tokenize
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


# # create a bot instance
# bot = ChatBot("WordsAI",
#               preprocessors=[
#                   'chatterbot.preprocessors.clean_whitespace'
#               ],
#               logic_adapters=[
#                   'chatterbot.logic.BestMatch',
#                   'chatterbot.logic.TimeLogicAdapter'],
#               storage_adapter='chatterbot.storage.SQLStorageAdapter')


# # train the bot
# trainer = ChatterBotCorpusTrainer(bot)
# trainer.train("./temp/convo.yml", "chatterbot.corpus.english.greetings",
#               "chatterbot.corpus.english.conversations")


# # create a post route
# @app.post("/bot", tags=["WordsAI Bot"])
# async def get_response(text: str) -> dict:
#     answer = bot.get_response(text)
#     return {"WordsAI": str(answer)}
