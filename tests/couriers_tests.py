from methods.courier_methods import *
from methods.courier_methods import Courier
import pytest

payload, response = CourierMethods.create_courier()
courier_1 = Courier(payload)
print(courier_1.login, courier_1.password, courier_1.first_name)

class TestCreateCourier:

    def test_create_new_courier(self):

    def test_create_two_similar_couriers(self):

    def test_create_courier_with_all_required_fields(self):

    def test_correct_response_code_successful_registration(self):

    def test_successful_request_returns_true(self):

    def test_one_field_is_missing_request_returns_error(self):

    def test_create_courier_with_exist_login_returns_error(self):


class TestLoginCourier:

    def test_courier_successful_authorization(self):

    def test_required_fields_submitted_for_authorization(self):

    def test_missing_required_field_returns_error(self):

    def test_authorization_with_wrong_login_returns_error(self):

    def test_successful_request_returns_id(self):


