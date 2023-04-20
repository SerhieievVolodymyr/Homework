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
        self._products.update({product: quantity})

    def get_total(self):
        total = 0
        for product, quantity in self._products.items():
            total += product.get_total(quantity)
        return total

    def purchased(self):
        self.__purchased = True

    def __float__(self):
        return float(self.get_total())

    def __bool__(self):
        if len(self._products) > 0 and not self.__purchased:
            return True
        else:
            print('Візок проданий або пустий')
            return False

    def __eq__(self, other):
        return self._products == other._products

    def __len__(self):
        return len(self._products)

    def __getitem__(self, item):
        return item, self._products[item]


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


if __name__ == '__main__':
    apple = Product('apple', 1200, 1)
    peach = Product('peach', 3000, 1.0)
    cart1 = ShoppingCart()
    cart1.add_product(apple)
    cart1.add_product(peach, 3.5)
    cart2 = ShoppingCart()
    cart2.add_product(apple)
    cart2.add_product(peach, 3.4)
    print(str(apple))
    print(float(apple))
    print(float(cart2))
    print(cart1 == cart2)
    print(apple == peach)

    # card_processor = CardPaymentProcessor(1234)
    # card_processor.purchase(cart1)
    # cash_processor = CashPaymentProcessor()
    # cash_processor.purchase(cart1)  # Error
    #
    # cash_processor2 = CashPaymentProcessor()
    # cash_processor2.purchase(cart2)
