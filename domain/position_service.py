from domain.basic_types import Position, InvalidIntersectionException
from domain.board import possible_directions
from domain.direction import Direction


class PositionService:
    letter_orders = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

    valid_ranges = {
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

    def __init__(self):
        self._positions = {Position(letter, num)
                           for letter, lst in self.valid_ranges.items()
                           for num in lst}

    def determine_direction(self, pos_A, pos_B):
        number_A = pos_A.number
        letter_A = pos_A.letter

        number_B = pos_B.number
        letter_B = pos_B.letter

        dirs = list(possible_directions)

        if number_B > number_A:
            dirs = filter(
                lambda el: el not in [Direction.BOTTOM, Direction.BOTTOM_LEFT, Direction.BOTTOM_RIGHT,
                                      Direction.TOP_LEFT],
                dirs)

        if number_B == number_A:
            dirs = filter(
                lambda el: el not in [Direction.TOP, Direction.BOTTOM, Direction.BOTTOM_LEFT,
                                      Direction.TOP_RIGHT],
                dirs)

        if number_B < number_A:
            dirs = filter(
                lambda el: el not in [Direction.TOP, Direction.TOP_LEFT, Direction.TOP_RIGHT,
                                      Direction.BOTTOM_RIGHT],
                dirs)

        if letter_B == letter_A:
            dirs = filter(
                lambda el: el not in [Direction.BOTTOM_RIGHT, Direction.BOTTOM_LEFT, Direction.TOP_RIGHT, Direction.TOP_LEFT],
                dirs)

        if letter_B > letter_A:
            dirs = filter(
                lambda el: el not in [Direction.BOTTOM_LEFT, Direction.TOP_LEFT, Direction.TOP, Direction.BOTTOM],
                dirs)

        if letter_B < letter_A:
            dirs = filter(
                lambda el: el not in [Direction.BOTTOM_RIGHT, Direction.TOP_RIGHT, Direction.TOP, Direction.BOTTOM],
                dirs)

        dirs = list(dirs)
        assert len(dirs) == 1, print(dirs)

        return dirs[0]

    def get_all_positions(self):
        return self._positions

    def next_position_from(self, pos, direction, distance):
        """
        Get the next progression given a direction and distance
        """
        num = pos.number
        letter = pos.letter

        if direction in [Direction.TOP, Direction.TOP_RIGHT]:
            next_num = num + distance
        elif direction in [Direction.TOP_LEFT, Direction.BOTTOM_RIGHT]:
            next_num = num
        else:
            next_num = num - distance

        if direction in [Direction.TOP, Direction.BOTTOM]:
            next_letter = letter
        elif direction in [Direction.TOP_LEFT, Direction.BOTTOM_LEFT]:
            next_letter = self._get_letter_by_index(self._find_letter_index(letter) - distance)
        else:
            next_letter = self._get_letter_by_index(self._find_letter_index(letter) + distance)

        position = Position(next_letter, next_num)

        if not self._is_valid_position(position):
            raise InvalidIntersectionException

        return position

    def _is_valid_position(self, position):
        return position in self._positions

    def _find_letter_index(self, letter):
        return self.letter_orders.index(letter)

    def _get_letter_by_index(self, idx):
        return None if idx < 0 or idx > len(self.letter_orders) - 1 else self.letter_orders[idx]
