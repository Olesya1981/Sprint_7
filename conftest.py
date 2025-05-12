import pytest
from data import *
from methods.courier_methods import *

@pytest.fixture(scope='function')
def new_courier_data():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем в словарь
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


@pytest.fixture(scope='function')
def create_courier():
    response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_CREATE_URL}", Couriers.NOT_EXISTING_COURIER)
    yield response
    CourierMethods.delete_courier(Couriers.NOT_EXISTING_COURIER)