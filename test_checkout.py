import pytest
from checkout import Checkout


@pytest.fixture()
def checkout():
    check_out = Checkout()
    return check_out


def test_can_add_item_price(checkout):
    checkout.add_item_price("a", 1)


def test_can_add_item(checkout):
    checkout.add_item("a")
