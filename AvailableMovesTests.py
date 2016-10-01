import unittest
from BoardHelper import initializeBoard
from BusinessRules import *
from Domain import *

class AvailableMovesTests(unittest.TestCase):

    def setUp(self):
        self.board = initializeBoard()

    def testOnEmptyBoard(self):
        positions = getValidMoves(self.board, Position("A", 2))
        # From A2 in a Yinsh board, we have access to 18 moves
        self.assertEqual(18, len(positions))

        positions = getValidMoves(self.board, Position("F", 6))
        self.assertEqual(24, len(positions))

    def testWithOneRingBlockingTheWay(self):
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Ring))

        positions = getValidMoves(self.board, Position("A", 2))
        # With one wring blocking B3 we should have way less possible moves
        self.assertEqual(9, len(positions))

    def testWithOneTokenBlockingTheWay(self):
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))

        positions = getValidMoves(self.board, Position("A", 2))
        # With one wring blocking B3 we should have way less possible moves
        self.assertEqual(11, len(positions))


if __name__ == '__main__':
    unittest.main()