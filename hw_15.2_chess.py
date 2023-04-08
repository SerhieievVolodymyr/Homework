def reformat_coordinates(coordinates):
    letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    if coordinates[0] in letter_to_number and coordinates[1] in '123456789':
        return int(coordinates[1:]), letter_to_number[coordinates[0]]


def is_on_desk(coordinates):
    row, column = reformat_coordinates(coordinates)
    if 0 < row < 9 and 0 < column < 9:
        return True
    return False


class Chessman:
    """
    Всі методи приймають координати у шаховому форматі.
    Наприклад: 'a1',  'e5', 'h8'
    """
    _number_to_letter = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}

    def __init__(self, color, place):
        self.color = color
        self._row, self._column = reformat_coordinates(place)
        self.place = place

    def change_color(self):
        if self.color == 'white':
            self.color = 'black'
        else:
            self.color = 'white'

    def change_place(self, preferred_place):
        preferred_row, preferred_column = reformat_coordinates(preferred_place)
        if is_on_desk(preferred_place):
            self._row, self._column = preferred_row, preferred_column
            self.place = self._number_to_letter[self._column] + str(self._row)
        else:
            print('Виходить за дошку')

    def try_move(self, move_to):
        raise NotImplementedError


class Knight(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if abs(row - self._row) == 2 and abs(column - self._column) == 1 and is_on_desk(move_to):
            return True
        elif abs(row - self._row) == 1 and abs(column - self._column) == 2 and is_on_desk(move_to):
            return True
        return False


class Pawn(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if self.color == 'white':
            if row == self._row + 1 and column == self._column and is_on_desk(move_to):
                return True
        else:
            if row == self._row - 1 and column == self._column and is_on_desk(move_to):
                return True
        return False


class King(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if abs(row - self._row) <= 1 and abs(column - self._column) <= 1 and is_on_desk(move_to):
            return True
        return False


class Queen(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if abs(row - self._row) == abs(column - self._column) or row == self._row or column == self._column \
                and is_on_desk(move_to):
            return True
        return False


class Rook(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if row == self._row or column == self._column and is_on_desk(move_to):
            return True
        return False


class Bishop(Chessman):
    def try_move(self, move_to):
        row, column = reformat_coordinates(move_to)
        if abs(row - self._row) == abs(column - self._column) and is_on_desk(move_to):
            return True
        return False


def possible_moves(pieces_list, cell):
    possible_moves_pieces = []
    for piece in pieces_list:
        if piece.try_move(cell):
            possible_moves_pieces.append(piece)
    return possible_moves_pieces
