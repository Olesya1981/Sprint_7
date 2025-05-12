import requests
from data import *
from helpers import *

class CourierMethods:

    def create_courier(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_CREATE_URL}", data = payload)
        return response

    def login_courier(payload):
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_LOGIN_URL}", data=payload)
        return response

