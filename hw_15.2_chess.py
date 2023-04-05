class Chessman:
    """
    При створенні об'єкту вкажіть параметр коліру і розташування фігури у вигляді списку чи кортежу
    Наприклад: piece = Chessman('white', ('a', 1))
    """
    _letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    _number_to_letter = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

    def __init__(self, color, place):
        self.color = color
        self.place = place

    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'

    def change_place(self, preferred_place):
        if 0 < self._letter_to_number[preferred_place[0]] < 9 and 0 < preferred_place[1] < 9:
            self.place = (preferred_place[0], preferred_place[1])
        else:
            print('Неправильні координати')

    def try_change_place(self):
        raise NotImplementedError


class Knight(Chessman):
    def try_change_place(self):
        pass
        # TODO: add functionality


class Pawn(Chessman):
    def try_change_place(self):
        pass
        # TODO: add functionality


class King(Chessman):
    def try_change_place(self):
        pass
        # TODO: add functionality


class Queen(Chessman):
    def try_change_place(self):
        pass
        # TODO: add functionality


class Rook(Chessman):
    def try_change_place(self):
        pass
        # TODO: add functionality


class Bishop(Chessman):
    def try_change_place(self):
        pass
    # TODO: add functionality
