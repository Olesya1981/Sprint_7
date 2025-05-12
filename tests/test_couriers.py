from conftest import *
from helpers import *
import allure
import pytest
from data import *


class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_new_courier_success(self, create_courier):
        response = create_courier
        assert (response.status_code, response.text) == Couriers.CREATED

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_two_similar_couriers_error(self):
        response = CourierMethods.create_courier(Couriers.EXISTING_COURIER)
        assert (response.status_code, response.text) == Couriers.SAME_LOGIN

    @allure.title("Для создания курьера нужно передать все обязательные поля")
    def test_create_courier_with_all_required_fields_success(self):
        response = CourierMethods.create_courier(Couriers.ONLY_PASSWORD)
        assert (response.status_code, response.text) != Couriers.CREATED

    @allure.title("Запрос возвращает правильный код ответа")
    def test_correct_response_code_successful_registration(self, create_courier):
        response = create_courier
        assert response.status_code == 201

    @allure.title("Успешный запрос возвращает 'ok':true'")
    def test_successful_request_returns_true(self, create_courier):
        response = create_courier
        assert response.text == Couriers.CREATED[1]

    @allure.title("Eсли одного из полей нет, запрос возвращает ошибку")
    def test_one_field_is_missing_request_returns_error(self):
        response = CourierMethods.create_courier(Couriers.ONLY_PASSWORD)
        assert (response.status_code, response.text) == Couriers.MISSED_DATA

    @allure.title("При создании курьера с существующим логином возвращается ошибка")
    def test_create_courier_with_exist_login_returns_error(self):
        response = CourierMethods.create_courier(Couriers.EXISTING_COURIER)
        assert (response.status_code, response.text) == Couriers.SAME_LOGIN


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
        assert (response.status_code, response.text) == Couriers.NOT_EXISTING_DATA

    @allure.title("Успешный запрос возвращает id.")
    def test_successful_request_returns_id(self):
        response = CourierMethods.login_courier(Couriers.EXISTING_COURIER)
        assert response.json().get('id', False)
