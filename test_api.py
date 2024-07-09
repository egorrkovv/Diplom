import requests
import json
import pytest
import allure
from faker import Faker

url = "https://fstravel.com/"
url2 = 'https://fstravel.com/api/get-countries-cards'
url3 = 'https://fstravel.com/api/search/wishList'
url4 = 'https://avia-new.fstravel.com/api/avia/external/cities/get-popular-cities'
email = "pajapat392@kernuo.com"
email2 = 'k1vn9xk2@spymail.one'
email3 = 'ulxskym149@1secmail.ru'

def test_status_code():
    response = requests.get(url)

    assert response.status_code == 200


def test_content_type():
    response1 = requests.get(url)
    
    assert response1.headers["Content-Type"] == 'text/html; charset=UTF-8'


def test_get_countries_cards():
    response2 = requests.get(url2)

    assert response2.status_code == 200


def test_get_wish_list():
    response3 = requests.get(url3,)
    
    assert response3.status_code == 200
    

def test_get_popular_cities():
    response4 = requests.get(url4)

    assert response4.status_code == 200

