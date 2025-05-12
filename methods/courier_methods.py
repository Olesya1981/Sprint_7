import requests
from data import *
from helpers import *

class CourierMethods:
    @staticmethod
    def create_courier():
        payload = register_new_courier_and_return_login_password()
        response = requests.post(f"{BASE_URL}{COURIER_URL}", data = payload)
        return payload, response

class Courier:

    def __init__(self, payload):
        self.login = payload['login']
        self.password = payload['password']
        self.first_name = payload['firstName']
