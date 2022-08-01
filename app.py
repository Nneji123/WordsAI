from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pysummarization.web_scraping import WebScraping
from pysummarization.abstractabledoc.std_abstractor import StdAbstractor
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
from pysummarization.nlpbase.auto_abstractor import AutoAbstractor


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
