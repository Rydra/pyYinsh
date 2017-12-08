from enum import Enum


class PlayerColor(Enum):
    BLACK = 0
    WHITE = 1


class Player:
    def __init__(self, color):
        self.color = color
        self.num_rows = 0

    def increase_row_number(self):
        self.num_rows += 1
