import requests
import pytest

url="http://localhost/login"
vals={'username': 'USER', 'password': 'PASS'}

def login():
    r=requests.post(url, data=vals)
    return b"Welcome admin!!!" in r.content

def test_wrong():
    assert login() == False