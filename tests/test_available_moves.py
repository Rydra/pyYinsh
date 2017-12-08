from domain.basic_types import Position
from domain.board import Board
from domain.piece import Token, Ring
from domain.player import PlayerColor
from domain.position_service import PositionService


class TestAvailableMoves:
    def setup_method(self):
        self.board = Board(PositionService())

    def test_on_empty_board(self):
        positions = self.board.get_valid_moves(Position("A", 2))
        # From A2 in a Yinsh board, we have access to 18 moves
        assert len(positions) == 18

        positions = self.board.get_valid_moves(Position("F", 6))
        assert len(positions) == 24

    def test_with_one_ring_blocking_the_way(self):
        self.board.put_piece_on_intersection(Position("B", 3), Ring(PlayerColor.WHITE))

        positions = self.board.get_valid_moves(Position("A", 2))
        # With one wring blocking B3 we should have way less possible moves
        assert len(positions) == 9

    def test_with_one_token_blocking_the_way(self):
        self.board.put_piece_on_intersection(Position("C", 4), Token(PlayerColor.WHITE))

        positions = self.board.get_valid_moves(Position("A", 2))
        # With one wring blocking B3 we should have way less possible moves
        assert len(positions) == 11
