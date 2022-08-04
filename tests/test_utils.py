import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from src.utils import *

def get_translation(language: str, text: str) -> str:
    translator = Translator(to_lang=language)
    translation = translator.translate(text)
    return "The translation of the text is: " + translation


# import pytest and create a test function to test the `get_translation` function
def test_get_translation():
    assert get_translation("en", "Hello") == "The translation of the text is: Hello"
    assert get_translation("es", "Hello") == "The translation of the text is: Hola"
    assert get_translation("fr", "Hello") == "The translation of the text is: Bonjour"
    assert get_translation("de", "Hello") == "The translation of the text is: Hallo"
    assert get_translation("it", "Hello") == "The translation of the text is: Ciao"
    assert get_translation("pt", "Hello") == "The translation of the text is: Olá"
    assert get_translation("ru", "Hello") == "The translation of the text is: Привет"
    assert get_translation("ja", "Hello") == "The translation of the text is: こんにちは"
    assert get_translation("zh", "Hello") == "The translation of the text is: 你好"
    assert get_translation("ar", "Hello") == "The translation of the text is: أهلا"
    assert get_translation("ko", "Hello") == "The translation of the text is: 안녕하세요"
    assert get_translation("fa", "Hello") == "The translation of the text is: خوش آمدید"
    assert get_translation("hi", "Hello") == "The translation of the text is: नमस्ते"
    assert get_translation("bn", "Hello") == "The translation of the text is: হ্যালো"
    assert get_translation("ta", "Hello") == "The translation of the text is: வணக்கம்"
    assert get_translation("te", "Hello") == "The translation of the text is: నమస్కారం"
    

