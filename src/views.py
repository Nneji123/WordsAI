import base64
from io import BytesIO

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from translate import Translator

app = FastAPI()

templates = Jinja2Templates(directory="templates")


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

def get_translation(language: str, text: str) -> str:
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return "The translation of the text is: " + translation