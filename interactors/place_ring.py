class PlaceRingInteractor:
    def __init__(self, board_service, game_service, presenter):
        self.board_service = board_service
        self.game_service = game_service
        self.presenter = presenter

    def execute(self, request):
        game = self.game_service.get_game(request.game_id)
        board = self.board_service.get_board(game.board_id)

        game.place_ring(board, request.position)