from utils import *

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.get("/translation")
def home(request: Request):
    return templates.TemplateResponse("translation.html", {"request": request})


@app.post("/translate")
async def home(request: Request):
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["message"] and form["language"]:
            language = form["language"]
            text = form["message"]
            translate = get_translation(language, text)
            sumary = " ".join(translate)

    return templates.TemplateResponse(
        "translation.html", {"request": request, "message": text, "language": language , "sumary": sumary})


@app.get("/sentiment")
def home(request: Request):
    return templates.TemplateResponse("sentiment.html", {"request": request})


@app.post("/sentiment_analysis")
async def home(request: Request):
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["message"]:
            text = form["message"]
            translate = get_sentiment(text)
            sumary = " ".join(translate)

    return templates.TemplateResponse(
        "sentiment.html", {"request": request, "message": text, "sumary": sumary})


@app.get("/summary")
def home(request: Request):
    return templates.TemplateResponse("summary.html", {"request": request})



@app.post("/summary_normal")
async def home(request: Request):
    sumary=""
    if request.method == "POST": 
        form = await request.form()
        if form["message"] and form["word_count"]: 
            word_count = form["word_count"]
            text = form["message"]
            sumary = summarize(text, word_count=int(word_count))
            sentences = sent_tokenize(sumary) # tokenize it
            sents = set(sentences)
            sumary = ' '.join(sents) 
            word_cloud = wordcloud(sumary)

    return templates.TemplateResponse("summary.html", {"request": request, "sumary": sumary, "wordcloud": word_cloud})



