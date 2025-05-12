from http.client import responses

import requests
from data import *

class OrderMethods:
    def create_order(self, params):
        response = requests.post(f"{Urls.BASE_URL}{Urls.ORDERS_URL}", json=params)
        return response

    def get_orders(self):
        response = requests.get(f"{Urls.BASE_URL}{Urls.ORDERS_URL}")
        return response