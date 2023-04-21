class Product:
    def __init__(self, name: str, price: int | float, unit: int | float):
        self.name = name
        self.price = price
        self.unit = unit

    def __repr__(self):
        return self.name

    def __float__(self):
        return float(self.price)

    def __eq__(self, other):
        return self.price == other.price and self.unit == other.unit and self.name == other.name

    def __hash__(self):
        return id(self)

    def get_total(self, quantity: int | float | None = None) -> int:
        if quantity is None:
            quantity = self.unit
        return self.price * quantity


class ShoppingCart:
    def __init__(self):
        self._products = {}
        self.__purchased = False

    def add_product(self, product, quantity=None):
        if quantity is None:
            quantity = product.unit
        if product in self._products:
            self._products[product] += quantity
        else:
            self._products.update({product: quantity})

    def get_total(self):
        total = 0
        for product, quantity in self._products.items():
            total += product.get_total(quantity)
        return total

    def purchased(self):
        self.__purchased = True

    def get_products(self):
        return self._products

    def remove_product(self, product):
        self._products.pop(product)

    def sub_product(self, product, quantity):
        self._products[product] -= quantity
        if self._products[product] <= 0:
            self._products.pop(product)

    def __float__(self):
        return float(self.get_total())

    def __bool__(self):
        if len(self._products) > 0 and not self.__purchased:
            return True
        else:
            print('Візок проданий або пустий')
            return False

    def __eq__(self, other):
        return self.get_products() == other.get_products()

    def __len__(self):
        return len(self._products)

    def __getitem__(self, item):
        return item, self._products[item]

    def __iter__(self):
        return iter(self._products.items())


class PaymentValidator:
    def is_valid(self):
        raise NotImplementedError


class PaymentProcessor:

    def purchase(self, cart):
        raise NotImplementedError


class CashPaymentValidator(PaymentValidator):

    def is_valid(self):
        return True


class CodeValidator(PaymentValidator):

    def __init__(self, security_code):
        self.security_code = security_code

    def is_valid(self):
        client_code = int(input('Введіть код клієнта: '))
        if client_code == self.security_code:
            return True
        else:
            print('Неправильний код безпеки')
            return False


class CashPaymentProcessor(CashPaymentValidator, PaymentProcessor):
    def purchase(self, cart):
        print('Обробка готівкового платежу…')
        if self.is_valid() and bool(cart):
            print(f'Рахунок у кошику : {float(cart)}')
            print('Оплата успішна')
            cart.purchased()
        else:
            print('Виникла помилка')


class CardPaymentProcessor(CodeValidator, PaymentProcessor):
    def purchase(self, cart):
        print('Обробка платежу карткою…')
        if self.is_valid() and bool(cart):
            print(f'Код безпеки : {self.security_code}')
            print('Оплата успішна')
            cart.purchased()
        else:
            print('Виникла помилка')

