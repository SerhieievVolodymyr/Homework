class Phone:
    __call_counter = 0

    def __init__(self, number):
        self.phone_number = number

    def add_number(self, num):
        self.phone_number = num

    def number_calls(self):
        return self.__call_counter

    def take_call(self):
        self.__call_counter += 1


samsung = Phone(380951111111)
iphone = Phone(380952222222)
pixel = Phone(380953333333)

samsung.add_number(380951111112)
iphone.add_number(380952222223)
pixel.add_number(380953333334)

samsung.take_call()

iphone.take_call()
iphone.take_call()

pixel.take_call()
pixel.take_call()
pixel.take_call()

phones = [samsung, iphone, pixel]


def calls(phones_list):
    calls_counter = 0
    for phone in phones_list:
        calls_counter += phone.number_calls()
    return calls_counter
