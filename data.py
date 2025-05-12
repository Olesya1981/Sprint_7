class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    COURIER_CREATE_URL = '/api/v1/courier'
    COURIER_LOGIN_URL = '/api/v1/courier/login'
    DELETE_COURIER_URL = '/api/v1/courier/'
    ORDERS_URL = '/api/v1/orders'
    ORDERS_LIST_URL = '/api/v1/orders/track'


class Total:
    OK_TRUE = {'ok': 'true'}


class Couriers:
    CREATED = 201, '{"ok":true}'
    SAME_LOGIN = 409, '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'
    LOGIN_SUCCESS = 200, "id"
    MISSED_DATA = 400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'
    MISSED_LOGIN_DATA = 400, '{"code":400,"message":"Недостаточно данных для входа"}'
    NOT_EXISTING_DATA = 404, '{"code":404,"message":"Учетная запись не найдена"}'
    EXISTING_COURIER = {'login': 'xgcbjlebnp', 'password': 'fpmvijzuvf'}
    NOT_EXISTING_COURIER = {'login': 'MisterFrodoBaggins', 'password': 'TheRing'}
    EXISTING_COURIER_NO_LOGIN = {'password': 'fpmvijzuvf'}
    ONLY_PASSWORD = {'password': 'fpmvijzuvf'}

    CREATED_ORDER = 201, 'track'
    ORDERS_LIST = 200, 'orders', list


class OrderData:
    ORDER_DATA_1 = {
        "firstName": "Frodo",
        "lastName": "Beggins",
        "address": "Sheer, 1 apt.",
        "metroStation": 4,
        "phone": "+7 800 555 55 55",
        "rentTime": 5,
        "deliveryDate": "2025-06-06",
        "comment": "Saske, come back ",
        "color": [
            "BLACK"
        ]
    }
    ORDER_DATA_2 = {
        "firstName": "SubZero",
        "lastName": "Kombat",
        "address": "Sheer, 2 apt.",
        "metroStation": 6,
        "phone": "+7 800 555 53 53",
        "rentTime": 4,
        "deliveryDate": "2025-06-07",
        "comment": "Saske, come back ",
        "color": [
            "BLACK",
            "GREY"
        ]
    }
    ORDER_DATA_3 = {
        "firstName": "Zero",
        "lastName": "KombatSub",
        "address": "Sheer, 3 apt.",
        "metroStation": 8,
        "phone": "+7 800 333 53 53",
        "rentTime": 5,
        "deliveryDate": "2025-06-07",
        "comment": "Saske, come back ",
        "color": [

        ]
    }
