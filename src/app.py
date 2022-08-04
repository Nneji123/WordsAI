from fastapi import FastAPI, File, Request, Response, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pyresparser import ResumeParser

from utils import *

app = FastAPI()

app = FastAPI(
    title="WordsAI WebApp Backend",
    description="""A collection of NLP Applications served as APIs using FastAPI.""",
    version="0.0.1",
    docs_url=None, 
    redoc_url=None
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="templates")

favicon_path = "favicon.ico"


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)


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


@app.get("/chatbot")
def home(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})


@app.get("/resume")
def home(request: Request):
    return templates.TemplateResponse("resume.html", {"request": request})


@app.post("/resume_parser")
async def resume_parser(request: Request, file: UploadFile) -> str:
    # write a function to save the uploaded file and return the file name
    if request.method == "POST":
        form = await request.form()
        if form["file"]:

            files = form["file"]
            files = await file.read()
            # save the file
            filename = "./temp/file.pdf"

            with open(filename, "wb+") as f:
                f.write(files)
            # open the file and return the file name

            with open(filename, "rb") as f:
                pdf = f.read()
            sumary = ResumeParser(filename).get_extracted_data()
    return templates.TemplateResponse(
        "resume.html", {"request": request, "message": filename, "sumary": sumary})


@app.get("/ocr")
def home(request: Request):
    return templates.TemplateResponse("ocr.html", {"request": request})


@app.post("/ocr_parser")
async def get_ocr(request:Request, file: UploadFile = File(...)):
        # write a function to save the uploaded file and return the file name
    if request.method == "POST":
        form = await request.form()
        if form["file"]:

            files = form["file"]
            contents = io.BytesIO(await files.read())
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
            return templates.TemplateResponse(
        "ocr.html", {"request": request, "sumary": new_string})


@app.post("/named_e_r")
async def home(request: Request):
    sumary = ""
    if request.method == "POST":
        form = await request.form()
        if form["file"]:
            text = form["file"]
            translate = get_ocr(text)
            sumary = translate

    return templates.TemplateResponse(
        "nme.html", {"request": request, "message": text, "sumary": sumary})




# create a bot instance
bot = ChatBot("WordsAI",
              preprocessors=[
                  'chatterbot.preprocessors.clean_whitespace'
              ],
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  'chatterbot.logic.TimeLogicAdapter'],
              storage_adapter='chatterbot.storage.SQLStorageAdapter')




@app.get("/chatbot", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})

@app.get("/getChatBotResponse")
def get_bot_response(msg: str):
    return str(bot.get_response(msg))



@app.get("/speech")
def home(request: Request):
    return templates.TemplateResponse("speech.html", {"request": request})


@app.post("/speech_to_text")
async def speech_to_text(request: Request, file: UploadFile = File(...)) -> str:
        # write a function to save the uploaded file and return the file name
    if request.method == "POST":
        form = await request.form()
        if form["file"]:

            files = form["file"]
            files = await files.read()
            
            filename = "./temp/file.wav"
            with open(filename, "wb+") as f:
                f.write(files)

            r = sr.Recognizer()
            harvard = sr.AudioFile(filename)
            with harvard as source:
                audio = r.record(source)
            text = r.recognize_sphinx(audio)
            return templates.TemplateResponse(
                "speech.html", {"request": request, "sumary": text})


