import uuid

from domain.piece import Ring
from domain.player import Player, PlayerColor


class Game:
    def __init__(self, board, initial_state):
        self.board = board
        self.id = uuid.uuid4()
        self.white_player = Player(PlayerColor.WHITE)
        self.black_player = Player(PlayerColor.BLACK)
        self.current_player = self.white_player
        self.current_state = initial_state

    def end_turn(self):
        self.current_player = self.white_player if self.current_player == self.black_player else self.black_player

    def place_ring(self, position):
        self.current_state = self.current_state.place_ring(position)

    def play_token(self, src_position, dest_position):
        self.current_state = self.current_state.play_token(src_position, dest_position)


class PlaceRingsState:
    def __init__(self, board, game, placed_rings):
        self.game = game
        self.board = board
        self.placed_rings = placed_rings

    def place_ring(self, position):
        self.board.put_piece_on_intersection(position, Ring(self.game.current_player.player_color))
        self.placed_rings += 1
        self.game.end_turn()

        if self.placed_rings == 10:
            next_state = PlayTokenState(self.board, self.game)
        else:
            next_state = self

        return next_state


class PlayTokenState:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def play_token(self, src_position, dest_position):
        self.board.make_move(self.game.current_player, src_position, dest_position)

        if self.board.has_rows():
            next_state = RemoveRowState(self.board, self.game)
        else:
            next_state = self
            self.game.end_turn()

        return next_state


class RemoveRowState:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def remove_row(self, row_id):
        row = self.board.get_row(row_id)
        self.board.remove_row(row)

        if self.board.has_rows():
            next_state = self
        else:
            next_state = PlayTokenState(self.board, self.game)
            self.game.end_turn()
        return next_state

class TakeRingOutState:
    def __init__(self, board, game):
        self.board = board
        self.game = game

    def take_ring_out(self, position):
        pass




class BoardService:
    def __init__(self):
        self.boards = {}

    def add_board(self, board):
        self.boards[board.id] = board

    def get_board(self, id):
        return self.boards[id]


class GameService:
    def __init__(self):
        self.games = {}

    def add_game(self, game):
        self.games[game.id] = game

    def get_game(self, id):
        return self.games[id]
