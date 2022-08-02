from io import BytesIO
import base64
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
import nltk
from nltk.tokenize import sent_tokenize
from gensim.summarization import summarize
from wordcloud import WordCloud, STOPWORDS 

app = FastAPI()

templates = Jinja2Templates(directory="templates")


nltk.download('punkt') # download this
@app.get("/")
def home(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def home(request: Request):
    """
    The home function returns the home page of the web app.
    It also accepts a POST request with a form that contains two fields:
    a message and word_count. The message is then summarized based on 
    the word count provided by user.
    
    Args:
        request:Request: Get the request data from the user
    
    Returns:
        A string that contains the summarized text.
    """
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
    return templates.TemplateResponse("index.html", {"request": request, "sumary": sumary, "wordcloud": word_cloud})



def wordcloud(text):
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width = 400, height = 400, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(text).to_image()
    img = BytesIO()
    wordcloud.save(img, "PNG")
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode()
    return img_b64