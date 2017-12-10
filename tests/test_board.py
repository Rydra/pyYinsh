from domain.basic_types import Position
from domain.board import Board
from domain.piece import Token
from domain.player import PlayerColor
from domain.position_service import PositionService


class TestBoard:
    def setup_method(self):
        self.board = Board(PositionService())

    def test_detect_one_five_in_a_row(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 1

    def test_find_one_five_in_a_row(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 1

    def test_find_two_five_in_a_row_intersecting(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))

        self.board.put_piece_on_intersection(Position("C", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 6), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 7), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 2

    def test_find_two_five_in_a_row_overlapping(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("F", 7), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 2

    def test_find_two_five_in_a_separated(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))

        # Random noise
        self.board.put_piece_on_intersection(Position("I", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("J", 5), Token(PlayerColor.WHITE))

        self.board.put_piece_on_intersection(Position("G", 11), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 10), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 9), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 8), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 7), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 2

    def test_one_broken_seq(self):
        self.board.put_piece_on_intersection(Position("A", 2), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("B", 3), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.BLACK))
        self.board.put_piece_on_intersection(Position("D", 5), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("E", 6), Token(PlayerColor.WHITE))

        # Random noise
        self.board.put_piece_on_intersection(Position("I", 4), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("J", 5), Token(PlayerColor.WHITE))

        self.board.put_piece_on_intersection(Position("G", 11), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 10), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 9), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 8), Token(PlayerColor.WHITE))
        self.board.put_piece_on_intersection(Position("G", 7), Token(PlayerColor.WHITE))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found_rows = self.board.find_rows()
        assert len(found_rows) == 1
