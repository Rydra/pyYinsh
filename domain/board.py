from collections import defaultdict

from domain.basic_types import InvalidIntersectionException, InvalidMoveException
from queue import Queue

from domain.direction import Direction
from domain.piece import PieceType, Token, Ring


class IntersectionStatus:
    OCCUPIED = 0
    EMPTY = 1


class Intersection:
    def __init__(self, status, position, piece=None):
        self.status = status
        self.position = position
        self.piece = piece

    def place_piece(self, piece):
        self.piece = piece
        self.status = IntersectionStatus.OCCUPIED

    def remove_piece(self):
        self.status = IntersectionStatus.EMPTY
        self.piece = None

    def occupied_by(self):
        if self.piece:
            return self.piece.player_color
        else:
            return None

    def is_jumpable(self):
        return self.piece.piece_type == PieceType.TOKEN

    def is_empty(self):
        return self.status == IntersectionStatus.EMPTY

    def is_occupied(self):
        return self.status == IntersectionStatus.OCCUPIED

    def flip_token(self):
        if self.is_occupied() and self.piece.piece_type == PieceType.TOKEN:
            self.piece.flip_color()


# A Node embeds a state for the BFS
class Node:
    def __init__(self, intersection, direction=None, has_jumped=False):
        self.intersection = intersection

        # The allowed_dirs helps determine the direction it has to follow on the search
        self.direction = direction
        self.has_jumped = has_jumped


class Board:
    def __init__(self, position_service):
        self._position_service = position_service
        positions = position_service.get_all_positions()
        self._intersections = dict(zip(positions, [Intersection(IntersectionStatus.EMPTY, pos) for pos in positions]))

    def _get_intersection(self, pos):
        try:
            return self._intersections[pos]
        except KeyError:
            raise InvalidIntersectionException(pos)

    @property
    def intersections(self):
        return self._intersections.values()

    def make_move(self, player, src_pos, dest_pos):
        self._do_move(player, src_pos, dest_pos)
        rows = self.find_five_in_a_row()

        if rows:
            # TODO
            pass


    def _do_move(self, player, src_pos, dest_pos):
        intersection = self._get_intersection(src_pos)
        if intersection.is_empty():
            raise InvalidMoveException('The intersection is empty')
        if intersection.occupied_by() != player.color:
            raise InvalidMoveException('You cannot move a piece which is not your own')
        if intersection.piece.piece_type != PieceType.RING:
            raise InvalidMoveException('You can only move rings')

        dest_intersection = self._get_intersection(dest_pos)
        valid_moves = self.get_valid_moves(start_position=src_pos)
        if dest_intersection not in valid_moves:
            raise InvalidMoveException(f'You cannot move to {dest_pos}')

        self.put_piece_on_intersection(src_pos, Token(player))
        self.put_piece_on_intersection(dest_pos, Ring(player))

        direction = self._position_service.determine_direction(src_pos, dest_pos)

        current_intersection = self._get_next_intersection(intersection, direction)
        while current_intersection.position != dest_pos:
            current_intersection.flip_token()
            current_intersection = self._get_next_intersection(current_intersection, direction)

    def put_piece_on_intersection(self, pos, piece):
        intersection = self._get_intersection(pos)
        intersection.place_piece(piece)

    def remove_piece_on_intersection(self, pos):
        intersection = self._get_intersection(pos)
        intersection.remove_piece()

    # Obtains the valid positions that you can move from the specified starting position
    def get_valid_moves(self, start_position):
        def valid_movepoint(intersection):
            return intersection.is_empty()

        # Given a node, returns all the possible next states that node can go
        def get_neighbors(node):
            found_neighs = []
            for dir in [node.direction] if node.direction else possible_directions:
                # Now we need to consider a few things depending on conditions for the neighbor we are
                # analyzing. It is not a valid neighbor if the coordinate is occupied by a ring,
                # or if the previous node has jumped and the new neighbor is an empty space
                if node.intersection.is_empty() and node.has_jumped:
                    continue

                next_intersection = self._get_next_intersection(node.intersection, dir)

                if next_intersection is None:
                    continue

                if next_intersection.is_occupied() and not next_intersection.is_jumpable():
                    continue

                if next_intersection.is_occupied() and next_intersection.is_jumpable():
                    # Valid neighbor, but we need to mark it as a jump
                    found_neighs.append(Node(next_intersection, direction=dir, has_jumped=True))
                elif next_intersection.is_empty():
                    # Valid neighbor. It is possible we find an empty space while jumping or not,
                    # so we need to keep track of it
                    found_neighs.append(Node(next_intersection, direction=dir, has_jumped=node.has_jumped))
                else:
                    raise Exception("Unconsidered situation!")

            return found_neighs

        found_intersections = []
        node = Node(self._get_intersection(start_position))

        # We will perform a "kind-of" BFS to find all the possible moves. In BFS usually you check
        # if the starting node is a solution, but in Yinsh the starting move is NEVER a solution. You also
        # have a frontier and explored lists to check which are the next nodes to analyze, but since we can
        # guarantee through neighbors that we won't access the same node twice, you just need the frontier

        frontier = Queue()
        frontier.enqueue(node)

        while not frontier.is_empty():
            node = frontier.dequeue()
            for next_node in get_neighbors(node):
                if valid_movepoint(next_node.intersection):
                    found_intersections.append(next_node.intersection)
                frontier.enqueue(next_node)

        return found_intersections

    def find_five_in_a_row(self):
        # Preconditions:
        # 1- a Five in a row means there are 5 token of the same color in a single direction
        # 2- Rows can overlap. if there are 6 in a row, we must detect in this situation 2 5 in a row
        found_rows = []

        # Create an ignore list. This list tells, for certain positions, which directions can be
        # ignored, so that you do not look twice for a five in a row or follow useless paths
        ignored_directions_list = defaultdict(list)

        for intersection in self._find_intersections_with_tokens():
            dirs_to_ignore = ignored_directions_list.get(intersection.position, [])
            for dir in [d
                        for d in [Direction.TOP, Direction.TOP_LEFT, Direction.TOP_RIGHT]
                        if d not in dirs_to_ignore]:
                found, analyzed_intersections = self._five_in_a_row_exists(intersection, dir)
                if found:
                    found_rows.append(analyzed_intersections)
                if not found:
                    # we can safely ignore for every analyzed token in a certain direction.
                    # Pointless to follow them in the same direction if we haven't already found any row
                    for itsect in analyzed_intersections:
                        ignored_directions_list[itsect.position].append(dir)

        return found_rows

    def _find_intersections_with_tokens(self):
        return [intersection
                for intersection in self.intersections
                if intersection.is_occupied()
                and intersection.piece.piece_type == PieceType.TOKEN]

    def _five_in_a_row_exists(self, src_intersection, direction):
        """
        Takes a point and looks 5 moves ahead in a direction to assess whether a row exists.
        If it does, returns it. Otherwise, returns None.
        """
        if src_intersection.is_empty():
            return False, None

        player_color = src_intersection.piece.player_color

        def continuity(intersection):
            return intersection is not None and intersection.is_occupied() and \
                   intersection.piece.player_color == player_color and \
                   intersection.piece.piece_type == PieceType.TOKEN

        analyzed_intersections = []
        found = True
        for distance in range(0, 5):
            intersection = self._get_next_intersection(src_intersection, direction, distance)
            if continuity(intersection):
                analyzed_intersections.append(intersection)
            else:
                found = False
                break

        return found, analyzed_intersections

    def _get_next_intersection(self, intersection, direction, distance=1):
        """
        Given a position and a direction, get the next coordinate. If the
        Coordinate is not valid for a Yinsh board, this function returns None
        """
        try:
            position = self._position_service.next_position_from(intersection.position, direction, distance)
        except InvalidIntersectionException:
            return None
        else:
            return self._get_intersection(position)


possible_directions = [
    Direction.TOP,
    Direction.TOP_LEFT,
    Direction.TOP_RIGHT,
    Direction.BOTTOM,
    Direction.BOTTOM_LEFT,
    Direction.BOTTOM_RIGHT
]
