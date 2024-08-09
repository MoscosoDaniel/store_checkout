class Checkout:
    class Discount:
        def __init__(self,
                     num_of_items: int,
                     price: float) -> None:
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self) -> None:
        self.prices = {}
        self.discounts = {}
        self.items_dict = {}

    def add_discount(self,
                     item: str,
                     num_of_items: int,
                     discount_price: float):
        discount = self.Discount(num_of_items, discount_price)
        self.discounts[item] = discount

    def add_item_price(self,
                       item: str,
                       price: float) -> None:
        self.prices[item] = price

    def add_item(self, item: str) -> None:
        if item not in self.prices:
            raise Exception("Bad item")

        if item in self.items_dict:
            self.items_dict[item] += 1
        else:
            self.items_dict[item] = 1

    def calculate_total(self) -> int:
        total_amount = 0
        for item_name, items_added in self.items_dict.items():
            total_amount += self.calculate_single_item_total(item_name, items_added)
        return total_amount

    def calculate_single_item_total(self,
                                    item_name: str,
                                    items_added: int):
        total_amount = 0

        # If the item does NOT exist in the discounts dictionary, then it is
        # a regular item:
        if item_name not in self.discounts:
            total_amount += self.prices[item_name] * items_added
            return total_amount

        # If the item exists in the discounts dictionary, copy the contents
        # into a new variable:
        discount = self.discounts[item_name]

        # If the amount of items does not hit the threshold for the discount,
        # then treat it as a regular item:
        if items_added < discount.num_of_items:
            total_amount += self.prices[item_name] * items_added
            return total_amount

        # If the item DOES exist in the discounts dictionary AND hits the
        # threshold for the discount, then apply it:
        total_amount += self.calculate_total_when_discount(item_name, items_added, discount)

        return total_amount

    def calculate_total_when_discount(self,
                                      item_name: str,
                                      items_added: int,
                                      discount_info: Discount):
        total_amount = 0

        discounts_to_apply = items_added / discount_info.num_of_items
        total_amount += discounts_to_apply * discount_info.price
        remaining = items_added % discount_info.num_of_items
        total_amount += remaining * self.prices[item_name]

        return total_amount