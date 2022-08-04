import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from src.utils import *

# import pytest and create a test function to test the `get_translation` function
def test_get_translation():
    assert get_translation("en", "Hello") == "The translation of the text is: Hello"
    assert get_translation("es", "Hello") == "The translation of the text is: Hola"
    assert get_translation("fr", "Hello") == "The translation of the text is: Bonjour"
    assert get_translation("de", "Hello") == "The translation of the text is: Hallo"

    
def test_get_sentiment():
    assert get_sentiment("Hello") == "The sentiment of the text is: Neutral and the Score is: 0.0"
    assert get_sentiment("I am happy") == "The sentiment of the text is: Positive and the Score is: 0.57"
    assert get_sentiment("I am sad") == "The sentiment of the text is: Negative and the Score is: -0.48"
    assert get_sentiment("I am neutral") == "The sentiment of the text is: Neutral and the Score is: 0.0"
    assert get_sentiment("I am not happy") == "The sentiment of the text is: Negative and the Score is: -0.46"
    assert get_sentiment("I am not sad") == "The sentiment of the text is: Positive and the Score is: 0.37"
    assert get_sentiment("I am not neutral") == "The sentiment of the text is: Neutral and the Score is: 0.0"



# import pytest and create a test function to test the `wordcloud` function
def get_autocorrect(language: str, text: str) -> str:
    spell = Speller(language)
    result = spell(text)
    return "The autocorrected text is: " + result


def get_named_entity_recognition(text: str) -> str:

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return [(X.text, X.label_) for X in doc.ents] 

def test_get_autocorrect():
    assert get_autocorrect("en", "wHat") == "The autocorrected text is: what"

def test_named_entity_recognition():
    assert get_named_entity_recognition("Bill Gates is 20 years old living in Jersey in the year 1999") == [('Bill Gates', 'PERSON'), ('20 years old', 'DATE'), ('Jersey', 'GPE'), ('the year 1999', 'DATE')]

def test_remove_profanity():
    assert remove_profanity("go to hell") == "go to ****"