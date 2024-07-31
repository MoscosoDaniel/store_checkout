class Checkout:
    def __init__(self) -> None:
        self.prices = {}
        self.total = 0

    def add_item_price(self, item: str, price: float) -> None:
        self.prices[item] = price

    def add_item(self, item: str) -> None:
        self.total += self.prices[item]

    def calculate_total(self) -> int:
        return self.total
