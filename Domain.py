from enum import Enum
class PlayerColor(Enum):
    Black = 0
    White = 1


class PieceType(Enum):
    Ring = 0
    Token = 1

class Direction(Enum):
    Top = 0
    TopLeft = 1
    TopRight = 2
    Bottom = 3
    BottomLeft = 4
    BottomRight = 5

letterOrders = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

validRanges = {
        "A": list(range(2, 6)),
        "B": list(range(1, 8)),
        "C": list(range(1, 9)),
        "D": list(range(1, 10)),
        "E": list(range(1, 11)),
        "F": list(range(2, 11)),
        "G": list(range(2, 12)),
        "H": list(range(3, 12)),
        "I": list(range(4, 12)),
        "J": list(range(5, 12)),
        "K": list(range(7, 11))
    }

possibleDirections = [
    Direction.Top,
    Direction.TopLeft,
    Direction.TopRight,
    Direction.Bottom,
    Direction.BottomLeft,
    Direction.BottomRight
]

class Piece:

    def __init__(self, playerColor, pieceType):
        self.playerColor = playerColor
        self.pieceType = pieceType

class Status: pass

class Filled(Status):

    def __init__(self, piece):
        self.piece = piece

class Empty(Status): pass

class Position:

    def __init__(self, letter, number):
        self.letter = letter
        self.number = number

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return "({0}, {1})".format(self.letter, self.number)

    def __repr__(self):
        return "({0}, {1})".format(self.letter, self.number)


class Intersection:
    def __init__(self, status, position):
        self.status = status
        self.position = position


def findLetterIndex (letter):
    return letterOrders.index(letter)

def getLetterByIndex (idx):
    return None if idx < 0 or idx > len(letterOrders) - 1 else letterOrders[idx]

def validateNum (n):
    return n if n >= 1 and n <= 11 else None

# TODO: This check can be way further optimized.
# Tells whether a given coordinate is in the range of the board and exists
def coordinateExists(position):
    return position.number in validRanges[position.letter]

class Board:
    def __init__(self, intersections):
        self.intersections = intersections

    def findIntersection(self, pos):
        return next((i for i in self.intersections if i.position == pos), None)

    # Given a position and a direction, get the next coordinate. If the
    # Coordinate is not valid for a Yinsh board, this function returns None
    def getNextIntersection(self, pos, dir, i = 1):
        num = pos.number
        letter = pos.letter

        # obtain the next progression given a direction
        if dir in [Direction.Top, Direction.TopRight]:
            nextnum = validateNum(num + i)
        elif dir in [Direction.TopLeft, Direction.BottomRight]:
            nextnum = validateNum(num)
        else:
            nextnum = validateNum(num - i)

        if dir in [Direction.Top, Direction.Bottom]:
            nextLetter = letter
        elif dir in [Direction.TopLeft, Direction.BottomLeft]:
            nextLetter = getLetterByIndex(findLetterIndex(letter) - i)
        else:
            nextLetter = getLetterByIndex(findLetterIndex(letter) + i)

        if nextnum is not None and nextLetter is not None:
            newPos = Position(nextLetter, nextnum)
            if coordinateExists(newPos):
                return self.findIntersection(newPos)
        else:
            return None

    def putPieceOnCoord (self, pos, piece):
        intersection = self.findIntersection(pos)
        intersection.status = Filled(piece)