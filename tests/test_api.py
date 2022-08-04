import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from api.app import *
from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)


def test_sentiment_analysis():
    response = client.post("/sentiment?text=I%20hate%20this%20place")
    assert response.status_code == 200
    assert response.json() == "The sentiment of the text is: Negative and the Score is: -0.57"


def test_translation():
    response = client.post("/translate?language=es&text=i%20hate%20this%20place")
    assert response.status_code == 200
    assert response.json() == "The translation of the text is: Odio este lugar."

def test_translation_error():
    response = client.post("/translate?language=esa&text=i%20hate%20this%20place'")
    assert response.status_code == 200
    assert response.json() == "The translation of the text is: 'ESA' IS AN INVALID TARGET LANGUAGE . EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT"

text = "Thor%3A%20Love%20and%20Thunder%20is%20a%202022%20American%20superhero%20film%20based%20on%20Marvel%20Comics%20featuring%20the%20character%20Thor%2C%20produced%20by%20Marvel%20Studios%20and%20distributed%20by%20Walt%20Disney%20Studios%20Motion%20Pictures.%20It%20is%20the%20sequel%20to%20Thor%3A%20Ragnarok%20%282017%29%20and%20the%2029th%20film%20in%20the%20Marvel%20Cinematic%20Universe%20%28MCU%29.%20The%20film%20is%20directed%20by%20Taika%20Waititi%2C%20who%20co-wrote%20the%20script%20with%20Jennifer%20Kaytin%20Robinson%2C%20and%20stars%20Chris%20Hemsworth%20as%20Thor%20alongside%20Christian%20Bale%2C%20Tessa%20Thompson%2C%20Jaimie%20Alexander%2C%20Waititi%2C%20Russell%20Crowe%2C%20and%20Natalie%20Portman.%20In%20the%20film%2C%20Thor%20attempts%20to%20find%20inner%20peace%2C%20but%20must%20return%20to%20action%20and%20recruit%20Valkyrie%20%28Thompson%29%2C%20Korg%20%28Waititi%29%2C%20and%20Jane%20Foster%20%28Portman%29%E2%80%94who%20is%20now%20the%20Mighty%20Thor%E2%80%94to%20stop%20Gorr%20the%20God%20Butcher%20%28Bale%29%20from%20eliminating%20all%20gods.%20"

def test_summary():
    response = client.post("/summarize?text="+text)
    assert response.status_code == 200
    assert response.json() == {
  "summarize_result": [
    "Thor: Love and Thunder is a 2022 American superhero film based on Marvel Comics featuring the character Thor, produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures.\n",
    " It is the sequel to Thor: Ragnarok (2017) and the 29th film in the Marvel Cinematic Universe (MCU).\n",
    " The film is directed by Taika Waititi, who co-wrote the script with Jennifer Kaytin Robinson, and stars Chris Hemsworth as Thor alongside Christian Bale, Tessa Thompson, Jaimie Alexander, Waititi, Russell Crowe, and Natalie Portman.\n",
    " In the film, Thor attempts to find inner peace, but must return to action and recruit Valkyrie (Thompson), Korg (Waititi), and Jane Foster (Portman)—who is now the Mighty Thor—to stop Gorr the God Butcher (Bale) from eliminating all gods.\n",
    " .\n"
  ],
  "scoring_data": [
    [
      0,
      21.551724137931036
    ],
    [
      1,
      14.222222222222221
    ],
    [
      2,
      30.11764705882353
    ],
    [
      3,
      31.41025641025641
    ],
    [
      4,
      1
    ]
  ]
}



def test_autocorrect():
    response = client.post("/autocorrect?language=es&text=wHat")
    assert response.status_code == 200
    assert response.json() == "The autocorrected text is: what"

def test_named_entity_recognition_api_endpoint():
    response = client.post("named_entity_recognition?text=Bill%20Gates%20is%2029%20years%20old%20living%20in%20Jersey%20in%20the%20year%201999'")
    assert response.status_code == 200
    assert response.json() == [
  [
    "Bill Gates",
    "PERSON"
  ],
  [
    "29 years old",
    "DATE"
  ],
  [
    "Jersey",
    "GPE"
  ],
  [
    "the year 1999",
    "DATE"
  ]
]