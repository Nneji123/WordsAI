from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from utils import *

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
        "translation.html", {"request": request, "message": text, "language": language, "sumary": sumary})


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
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["message"] and form["word_count"]:
            word_count = form["word_count"]
            text = form["message"]
            sumary = summarize(text, word_count=int(word_count))
            sentences = sent_tokenize(sumary)  # tokenize it
            sents = set(sentences)
            sumary = ' '.join(sents)
            word_cloud = wordcloud(sumary)

    return templates.TemplateResponse("summary.html", {"request": request, "sumary": sumary, "wordcloud": word_cloud})

favicon_path = "favicon.ico"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


@app.get("/autocorrect")
def home(request: Request):
    return templates.TemplateResponse("autocorrect.html", {"request": request})


@app.post("/auto_correct")
async def home(request: Request):
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["message"] and form["language"]:
            language = form["language"]
            text = form["message"]
            translate = get_autocorrect(language, text)
            sumary = " ".join(translate)

    return templates.TemplateResponse(
        "autocorrect.html", {"request": request, "message": text, "language": language, "sumary": sumary})


@app.get("/nme")
def home(request: Request):
    return templates.TemplateResponse("nme.html", {"request": request})


@app.post("/named_e_r")
async def home(request: Request):
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["message"]:
            text = form["message"]
            translate = get_named_entity_recognition(text)
            sumary = translate

    return templates.TemplateResponse(
        "nme.html", {"request": request, "message": text, "sumary": sumary})
