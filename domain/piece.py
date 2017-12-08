from enum import Enum

from domain.player import PlayerColor


class PieceType(Enum):
    RING = 0
    TOKEN = 1


class Piece:
    def __init__(self, player_color, piece_type):
        self.player_color = player_color
        self.piece_type = piece_type


class Token(Piece):
    def __init__(self, player_color):
        super(Token, self).__init__(player_color, PieceType.TOKEN)

    def flip_token(self):
        self.player_color = PlayerColor.WHITE if self.player_color == PlayerColor.BLACK else PlayerColor.BLACK


class Ring(Piece):
    def __init__(self, player_color):
        super(Ring, self).__init__(player_color, PieceType.RING)
