import pytest
from checkout import Checkout


@pytest.fixture()
def checkout_single_instance():
    check_out_var = Checkout()
    check_out_var.add_item_price("a", 1)
    check_out_var.add_item_price("b", 2)
    return check_out_var


def test_can_calculate_total(checkout_single_instance):
    checkout_single_instance.add_item("a")
    assert checkout_single_instance.calculate_total() == 1


def test_get_correct_total_with_multiple_items(checkout_single_instance):
    checkout_single_instance.add_item("a")
    checkout_single_instance.add_item("b")
    assert checkout_single_instance.calculate_total() == 3


def test_can_add_discount_rule(checkout_single_instance):
    checkout_single_instance.add_discount("a", 3, 2)


def test_can_apply_discount_rule(checkout_single_instance):
    checkout_single_instance.add_discount("a", 3, 2)
    checkout_single_instance.add_item("a")
    checkout_single_instance.add_item("a")
    checkout_single_instance.add_item("a")
    assert checkout_single_instance.calculate_total() == 2
