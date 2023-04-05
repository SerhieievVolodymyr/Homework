class Phone:
    phone_number = 0
    _call_counter = 0

    def add_number(self, num):
        self.phone_number = num

    def number_calls(self):
        return self.__call_counter

    def take_call(self):
        self.__call_counter += 1

