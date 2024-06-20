import requests
import json
import pytest
import allure
from faker import Faker

url = "https://auth2.fstravel.com/api/v1/account/sign-up-buyer"
email = "pajapat392@kernuo.com"
email2 = 'k1vn9xk2@spymail.one'
email3 = 'ulxskym149@1secmail.ru'

def status_code_test():
    response = requests.get(url)

    assert response.status_code == 200


def content_type_test():
    response1 = requests.get(url)
    
    assert response1.headers["Content-Type"] == "application/json; charset=utf-8"


def registration_test():
    registration_params4 = {
    "email" : email,
    "password": 'Top_secret_password1199',
    "phoneNumber" : '+79168459999',
    "emailing" : 'true',
    "clientId" : 'b2c:ru',
    "grant_type" : 'client_credentials',
    "clientType" : 'b2c.public.client'
}
    response3 = requests.post(url, params=registration_params4)
    assert response3.status_code == 201


def domen_com_test():
    registration_params1 = {
    "email" : email,
    "password": 'Top_secret_password1199',
    "phoneNumber" : '+79168459999',
    "emailing" : 'true',
    "clientId" : 'b2c:ru',
    "grant_type" : 'client_credentials',
    "clientType" : 'b2c.public.client'
}
    response = requests.post(url, params=registration_params1)
    
    assert response.status_code == 201
    

def domen_one_test():
    registration_params2 = {
    "email" : email2,
    "password": 'Top_secret_password1199',
    "phoneNumber" : '+79168459999',
    "emailing" : 'true',
    "clientId" : 'b2c:ru',
    "grant_type" : 'client_credentials',
    "clientType" : 'b2c.public.client'
}
    response2 = requests.post(url, params=registration_params2)
    assert response2.status_code == 201

def domen_one_test():
    registration_params3 = {
    "email" : email3,
    "password": 'Top_secret_password1199',
    "phoneNumber" : '+79168459999',
    "emailing" : 'true',
    "clientId" : 'b2c:ru',
    "grant_type" : 'client_credentials',
    "clientType" : 'b2c.public.client'
}
    response2 = requests.post(url, params=registration_params3)

    assert response2.status_code == 201


def max_password_test():
    registration_params5 = {
    "email" : email,
    "password": '0987654321',
    "phoneNumber" : '+79168459999',
    "emailing" : 'true',
    "clientId" : 'b2c:ru',
    "grant_type" : 'client_credentials',
    "clientType" : 'b2c.public.client'
}
    response3 = requests.post(url, params=registration_params5)
    assert response3.status_code == 201