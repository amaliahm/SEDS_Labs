import pytest

def serve_beer(age):
    if (age is None) or (age < 18):
        return "No beer"
    else:
        return "Have beer"

def test_serve_beer_legal():
    adult = 25
    assert serve_beer(adult) == "Have beer"

def test_serve_beer_illegal():
    child = 10
    assert serve_beer(child) == "No beer"
