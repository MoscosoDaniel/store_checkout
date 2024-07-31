from checkout import Checkout


def test_can_add_item_price():
    check_out = Checkout()
    check_out.add_item_price("a", 1)
