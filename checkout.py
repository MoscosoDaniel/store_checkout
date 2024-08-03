class Checkout:
    class Discount:
        def __init__(self, num_of_items: int, price: float) -> None:
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self) -> None:
        self.prices = {}
        self.discounts = {}
        self.items_dict = {}

    def add_discount(self, item: str, num_of_items: int, price: float):
        discount = self.Discount(num_of_items, price)
        self.discounts[item] = discount

    def add_item_price(self, item: str, price: float) -> None:
        self.prices[item] = price

    def add_item(self, item: str) -> None:
        if item in self.items_dict:
            self.items_dict[item] += 1
        else:
            self.items_dict[item] = 1

    def calculate_total(self) -> int:
        total_amount = 0
        for item_name, items_added in self.items_dict.items():
            if item_name in self.discounts:
                discount = self.discounts[item_name]
                if items_added >= discount.num_of_items:
                    discounts_to_apply = items_added / discount.num_of_items
                    total_amount += discounts_to_apply * discount.price
                    remaining = items_added % discount.num_of_items
                    total_amount += remaining * self.prices[item_name]
                else:
                    total_amount += self.prices[item_name] * items_added
            else:
                total_amount += self.prices[item_name] * items_added
        return total_amount
