import unittest
from BoardHelper import initializeBoard
from BusinessRules import *
from Domain import *

class FindFiveInARowTests(unittest.TestCase):

    def setUp(self):
        self.board = initializeBoard()

    def testDetectOneFiveInARow(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        found, row = fiveInARowExists(self.board, self.board.findIntersection(Position("A", 2)), Direction.TopRight)
        self.assertTrue(found)

    def testFindOneFiveInARow(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(1, len(rows))
        print(rows)

    def testFindTwoFiveInARowIntersecting(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))

        self.board.putPieceOnIntersection(Position("C", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 6), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 7), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testFindTwoFiveInARowOverlapping(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("F", 7), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testFindTwoFiveInASeparated(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))

        # Random noise
        self.board.putPieceOnIntersection(Position("I", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("J", 5), Token(PlayerColor.White))

        self.board.putPieceOnIntersection(Position("G", 11), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 10), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 9), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 8), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 7), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(2, len(rows))
        print(rows)

    def testOneBrokenSeq(self):
        self.board.putPieceOnIntersection(Position("A", 2), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("B", 3), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("C", 4), Token(PlayerColor.Black))
        self.board.putPieceOnIntersection(Position("D", 5), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("E", 6), Token(PlayerColor.White))

        # Random noise
        self.board.putPieceOnIntersection(Position("I", 4), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("J", 5), Token(PlayerColor.White))

        self.board.putPieceOnIntersection(Position("G", 11), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 10), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 9), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 8), Token(PlayerColor.White))
        self.board.putPieceOnIntersection(Position("G", 7), Token(PlayerColor.White))

        # When running through the TopRight direction of our setUp example, we should find a five in a row
        rows = findFiveInARow(self.board)
        self.assertEqual(1, len(rows))
        print(rows)


if __name__ == '__main__':
    unittest.main()