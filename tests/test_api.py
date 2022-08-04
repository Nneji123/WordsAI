#Write test for all the functions usef later
# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'config')))

from api.app import *
from fastapi import FastAPI
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/favicon.ico")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
