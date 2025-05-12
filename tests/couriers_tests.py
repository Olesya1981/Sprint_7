from conftest import *
import allure
from data import *


class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_new_courier_success(self):
        response = CourierMethods.create_courier(new_courier_data())
        assert (response.status_code, response.text) == Couriers.CREATED

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_similar_couriers_error(self):
        payload = new_courier_data()
        response = CourierMethods.create_courier(payload)
        response1 = CourierMethods.create_courier(payload)
        assert (response1.status_code, response1.text) == Couriers.SAME_LOGIN

    @allure.title("Для создания курьера нужно передать все обязательные поля")
    def test_create_courier_with_all_required_fields_success(self):
        payload = new_courier_data()
        del payload['login']
        response = CourierMethods.create_courier(payload)
        assert (response.status_code, response.text) != Couriers.CREATED

    @allure.title("Запрос возвращает правильный код ответа")
    def test_correct_response_code_successful_registration(self):
        response = CourierMethods.create_courier(new_courier_data())
        assert response.status_code == 201

    @allure.title("Успешный запрос возвращает 'ok':true'")
    def test_successful_request_returns_true(self):
        response = CourierMethods.create_courier(new_courier_data())
        assert response.text == Couriers.CREATED[1]

    @allure.title("Eсли одного из полей нет, запрос возвращает ошибку")
    def test_one_field_is_missing_request_returns_error(self):
        payload = new_courier_data()
        del payload['login']
        response = CourierMethods.create_courier(payload)
        assert (response.status_code, response.text) == Couriers.MISSED_DATA

    @allure.title("При создании курьера с существующим логином возвращается ошибка")
    def test_create_courier_with_exist_login_returns_error(self):
        payload = new_courier_data()
        response = CourierMethods.create_courier(payload)
        payload_new = new_courier_data()
        payload_new['login'] = payload['login']
        response1 = CourierMethods.create_courier(payload_new)
        assert (response1.status_code, response1.text) == Couriers.SAME_LOGIN


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_courier_successful_authorization(self):
        response = CourierMethods.login_courier(Couriers.EXISTING_COURIER)
        assert response.status_code == 200

    @allure.title("Для авторизации нужно передать все обязательные поля")
    def test_required_fields_submitted_for_authorization(self):
        response = CourierMethods.login_courier(Couriers.EXISTING_COURIER_NO_LOGIN)
        assert response.status_code != 200

    @allure.title("Система возвращает ошибку, если отсутствуют обязательные поля")
    def test_missing_required_field_returns_error(self):
        response = CourierMethods.login_courier(Couriers.EXISTING_COURIER_NO_LOGIN)
        assert (response.status_code, response.text) == Couriers.MISSED_LOGIN_DATA

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_authorization_with_wrong_login_returns_error(self):
        response = CourierMethods.login_courier(Couriers.NOT_EXISTING_COURIER)
        print(response.status_code, response.text)
        # assert (response.status_code, response.text) == Couriers.MISSED_LOGIN_DATA

    @allure.title("Успешный запрос возвращает id.")
    def test_successful_request_returns_id(self):
        response = CourierMethods.login_courier(Couriers.EXISTING_COURIER)
        assert response.json().get('id', False)
