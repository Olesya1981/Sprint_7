import requests
from data import *
from helpers import *


class CourierMethods:

    def create_courier(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_CREATE_URL}", payload)
        return response

    def login_courier(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_LOGIN_URL}", data=payload)
        return response

    def delete_courier(payload):
        response = CourierMethods.login_courier(payload)
        id = response.json().get('id')
        response = requests.delete(f"{Urls.BASE_URL}{Urls.DELETE_COURIER_URL}{id}")
