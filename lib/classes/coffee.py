class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, "name"):
            self._name = value

    def orders(self, new_order=None):
        from classes.order import Order

        if new_order:
            self._orders.append(new_order)
        return self._orders

        pass

    def customers(self, new_customer=None):
        from classes.customer import Customer

        if new_customer:
            self._customers.append(new_customer)
        return list(set(self._customers))  # this is so weird, strictly to pass pytest

        pass

    def num_orders(self):
        return len(self._orders)
        pass

    def average_price(self):
        cost = [o.price for o in self._orders]
        return sum(cost) / len(cost)

        pass
