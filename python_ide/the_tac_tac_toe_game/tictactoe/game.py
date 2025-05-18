from player import Player
from game_board import GameBoard
from board_element import BoardElement

class Game:
    def __init__(self, player1, player2):
        self.board = GameBoard()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.game_over = False
        self.winner = None


    def is_game_over(self):
        return self.game_over


    def get_winner(self):
        return self.winner


    def make_move(self, row, col):
        if not self.game_over:
            if self.board.get_cell(row, col) == BoardElement.EMPTY:
                self.board.place_symbol(row, col, self.current_player.symbol)
                self.check_game_state()
                if not self.game_over:
                    if self.current_player == self.player1:
                        self.current_player = self.player2
                    else:
                        self.current_player = self.player1



    def check_game_state(self):
        symbol = self.current_player.symbol
        if self.board.check_winner(symbol):
            self.game_over = True
            self.winner = symbol.value
        else:
            if self.board.is_full():
                self.game_over = True
                self.winner = "Draw"



    def convert_position(self, position):
        if position < 1 or position > 9:
            raise ValueError("Position must be between 1 and 9")
        row = (position - 1) // 3
        col = (position - 1) % 3
        return row, col