import unittest
from BoardHelper import initializeBoard
from BusinessRules import *
from Domain import *

class FindFiveInARowTests(unittest.TestCase):

    def setUp(self):
        self.board = initializeBoard()

    def testDetectOneFiveInARow(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found, row = fiveInARowExists(self.board, self.board.findIntersection(Position("A", 2)), Direction.TopRight)
        self.assertTrue(found)

    def testFindOneFiveInARow(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(1, len(rows))
        print(rows)

    def testFindTwoFiveInARowIntersecting(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))

        self.board.putPieceOnCoord(Position("C", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 6), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 7), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testFindTwoFiveInARowOverlapping(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("F", 7), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testFindTwoFiveInASeparated(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))

        # Random noise
        self.board.putPieceOnCoord(Position("I", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("J", 5), Piece(PlayerColor.White, PieceType.Token))

        self.board.putPieceOnCoord(Position("G", 11), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 10), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 9), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 8), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 7), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testOneBrokenSeq(self):
        self.board.putPieceOnCoord(Position("A", 2), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("B", 3), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("C", 4), Piece(PlayerColor.Black, PieceType.Token))
        self.board.putPieceOnCoord(Position("D", 5), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("E", 6), Piece(PlayerColor.White, PieceType.Token))

        # Random noise
        self.board.putPieceOnCoord(Position("I", 4), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("J", 5), Piece(PlayerColor.White, PieceType.Token))

        self.board.putPieceOnCoord(Position("G", 11), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 10), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 9), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 8), Piece(PlayerColor.White, PieceType.Token))
        self.board.putPieceOnCoord(Position("G", 7), Piece(PlayerColor.White, PieceType.Token))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(1, len(rows))
        print(rows)


if __name__ == '__main__':
    unittest.main()