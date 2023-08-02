class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    def orders(self, new_order=None):
        from classes.order import Order

        if new_order:
            self._orders.append(new_order)
        return self._orders

        pass

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee

        if new_coffee:
            self._coffees.append(new_coffee)
        return list(set(self._coffees))
        pass

    def create_order(self, coffee, price):
        from classes.order import Order

        Order(self, coffee, price)
