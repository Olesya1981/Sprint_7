import pytest
import allure
from data import *

from methods.order_methods import OrderMethods


class TestOrders:

    @pytest.mark.parametrize(
        'order_data',
        [
            OrderData.ORDER_DATA_1,
            OrderData.ORDER_DATA_2,
            OrderData.ORDER_DATA_3
        ]
    )
    @allure.title("Проверяем создание заказа: 'black' or 'black&grey' or 'no color'")
    def test_specify_color_black_or_white_when_create_order_success(self, order_data):
        order_methods = OrderMethods()
        response_order = order_methods.create_order(order_data)
        assert response_order.status_code == 201

    @allure.title("При успешном создании заказа тело ответа содержит track")
    def test_response_body_contains_a_track(self):
        order_methods = OrderMethods()
        response_order = order_methods.create_order(OrderData.ORDER_DATA_1)
        assert response_order.json().get('track', False)

    @allure.title("Тело ответа возвращает список заказов")
    def test_create_order_response_body_contains_orders_list(self):
        order_methods = OrderMethods()
        response_order_list = order_methods.get_orders()
        assert response_order_list.json().get('orders', False)
