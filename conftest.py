import pytest
from methods.courier_methods import *

@pytest.fixture()
def courier_methods():
    return CourierMethods()
