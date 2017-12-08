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


class InvalidIntersectionException(Exception):
    pass

class InvalidMoveException(Exception):
    pass
