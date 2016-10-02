from scipy.interpolate.interpolate import interp1d

from Domain import *
from Structures import Queue

# A Node embeds a state for the BFS
class Node:

    def __init__(self, intersection, allowedDirs, hasJumped):
        self.intersection = intersection
        self.allowedDirs = allowedDirs
        self.hasJumped = hasJumped

# Obtains the valid positions that you can move from the specified starting position
def getValidMoves (board, position):

    def validMovepoint (intersection):
        return type(intersection.status) is Empty

    # Given a node, returns all the possible next states that node can go
    def getPossibleNeighbors(node):
        foundNeighs = []
        for dir in node.allowedDirs:
            nextIntersection = board.getNextIntersection(node.intersection.position, dir)

            if nextIntersection is None:
                continue

            # Now we need to consider a few things depending on conditions for the neighbor we are
            # analyzing. It is not a valid neighbor if the coordinate is occupied by a ring,
            # or if the previous node has jumped and the new neighbor is an empty space
            if type(node.intersection.status) is Empty and node.hasJumped:
                continue

            if type(nextIntersection.status) is Filled and nextIntersection.status.piece.pieceType == PieceType.Ring:
                continue

            if type(nextIntersection.status) is Filled and nextIntersection.status.piece.pieceType == PieceType.Token:
                # Valid neighbor, but we need to mark it as a jump
                foundNeighs.append(Node(nextIntersection, [dir], True))
            elif type(nextIntersection.status) is Empty:
                # Valid neighbor. It is possible we find an empty space while jumping or not,
                # so we need to keep track of it
                foundNeighs.append(Node(nextIntersection, [dir], node.hasJumped))
            else: raise Exception("Unconsidered situation!")

        return foundNeighs

    foundIntersections = []
    node = Node(board.findIntersection(position), possibleDirections, False)

    # We will perform a "kind-of" BFS to find all the possible moves. In BFS usually you check
    # if the starting node is a solution, but in Yinsh the starting move is NEVER a solution. You also
    # have a frontier and explored lists to check which are the next nodes to analyze, but since we can
    # guarantee through neighbors that we won't access the same node twice, you just need the frontier

    frontier = Queue()
    frontier.enqueue(node)

    while not frontier.isEmpty():
        node = frontier.dequeue()
        for nextNode in getPossibleNeighbors(node):
            if validMovepoint(nextNode.intersection):
                foundIntersections.append(nextNode.intersection.position)
            frontier.enqueue(nextNode)

    return foundIntersections

# A dictionary to ease defining which one is the opposite of the other.
# Maybe I could use negative numbers in the enum declaration
# so that -Top would implicitly be Bottom?
opposites = {
    Direction.Top: Direction.Bottom,
    Direction.Bottom: Direction.Top,
    Direction.TopLeft: Direction.BottomRight,
    Direction.TopRight: Direction.BottomLeft,
    Direction.BottomLeft: Direction.TopRight,
    Direction.BottomRight: Direction.TopLeft,
}

# Takes a point and looks 5 moves ahead in a direction to assess whether a row exists.
# If it does, returns it. Otherwise, returns None.
def fiveInARowExists(board, intersection, dir):
    if type(intersection.status) is Empty: return None

    playerColor = intersection.status.piece.playerColor
    def condition(intersection):
        return intersection is not None and type(intersection.status) is Filled and \
               intersection.status.piece.playerColor == playerColor and \
               intersection.status.piece.pieceType == PieceType.Token

    analyzedIntersections = []
    found = True
    for i in range(0, 5):
        itsect = board.getNextIntersection(intersection.position, dir, i)
        if condition(itsect):
            analyzedIntersections.append(itsect.position)
        else:
            found = False
            break

    return found, analyzedIntersections

def findFiveInARow(board):
    # Preconditions:
    # 1- a Five in a row means there are 5 token of the same color in a single direction
    # 2- Rows can overlap. if there are 6 in a row, we must detect in this situation 2 5 in a row
    foundRows = []

    # Create an ignore list. This list tells, for certain positions, which directions can be
    # ignored, so that you do not look twice for a five in a row or follow useless paths
    ignoreList = { }

    # Brute force: Look every intersection with a token and assess if row exists
    intersectionsWithTokens = [ itsect
                             for itsect in board.intersections
                             if type(itsect.status) is not Empty and itsect.status.piece.pieceType == PieceType.Token ]

    for intersection in intersectionsWithTokens:
        dirsToIgnore = [] if intersection.position not in ignoreList else ignoreList[intersection.position]
        for dir in [ d
                     for d in [Direction.Top, Direction.TopLeft, Direction.TopRight]
                     if d not in dirsToIgnore]:
            found, row = fiveInARowExists(board, intersection, dir)
            if found: foundRows.append(row)
            if not found:
                # we can safely ignore for every analyzed token in a certain direction.
                # Pointless to follow them in the same direction if we haven't already found any row
                for r in row:
                    if r not in ignoreList: ignoreList[r] = []
                    ignoreList[r].append(dir)

    return foundRows

