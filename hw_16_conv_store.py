class Product:
    def __init__(self, name: str, price: int | float, unit: int | float):
        self.name = name
        self.price = price
        self.unit = unit

    def __repr__(self):
        return self.name

    def __float__(self):
        return float(self.price)

    def get_total(self, quantity: int | float | None = None) -> int:
        if quantity is None:
            quantity = self.unit
        return self.price * quantity


class ShoppingCart:
    def __init__(self):
        self._products = {}

    def add_product(self, product: Product, quantity):
        if quantity is None:
            quantity = product.unit
        self._products.update({product: quantity})

    def get_total(self):
        total = 0
        for product, quantity in self._products.items():
            total += product.get_total(quantity)
        return total

    def __float__(self):
        return self.get_total()

