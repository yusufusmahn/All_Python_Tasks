import unittest
from game import Game
from player import Player
from board_element import BoardElement

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player(BoardElement.X)
        self.player2 = Player(BoardElement.O)
        self.game = Game(self.player1, self.player2)

    def test_initial_game_state(self):
        self.assertFalse(self.game.is_game_over())
        self.assertEqual(self.game.current_player, self.player1)

    def test_make_valid_move(self):
        self.game.make_move(0, 0)
        self.assertEqual(self.game.board.get_cell(0, 0), BoardElement.X)
        self.assertEqual(self.game.current_player, self.player2)
        self.assertFalse(self.game.is_game_over())

    def test_move_on_occupied_cell(self):
        self.game.make_move(0, 0)
        before = self.game.board.get_cell(0, 0)
        self.game.make_move(0, 0)
        self.assertEqual(self.game.board.get_cell(0, 0), before)
        self.assertEqual(self.game.current_player, self.player2)

    def test_horizontal_win(self):
        self.game.make_move(0, 0)
        self.game.make_move(1, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(0, 2)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_winner(), "X")

    def test_draw_scenario(self):
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (2, 0), (2, 2), (1, 2), (2, 1)]
        for row, col in moves:
            self.game.make_move(row, col)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_winner(), "Draw")

    def test_convert_position_valid(self):
        self.assertEqual(self.game.convert_position(1), (0, 0))
        self.assertEqual(self.game.convert_position(5), (1, 1))
        self.assertEqual(self.game.convert_position(9), (2, 2))


    def test_vertical_win(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 0)
        self.game.make_move(0, 2)
        self.game.make_move(2, 0)
        self.assertEqual(self.game.board.get_cell(0, 0), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(1, 0), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(2, 0), BoardElement.X)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_winner(), "X")



    def test_main_diagonal_win(self):
        self.game.make_move(0, 0)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(0, 2)
        self.game.make_move(2, 2)
        self.assertEqual(self.game.board.get_cell(0, 0), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(1, 1), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(2, 2), BoardElement.X)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_winner(), "X")

    def test_other_diagonal_win(self):
        self.game.make_move(0, 2)
        self.game.make_move(0, 1)
        self.game.make_move(1, 1)
        self.game.make_move(0, 0)
        self.game.make_move(2, 0)
        self.assertEqual(self.game.board.get_cell(0, 2), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(1, 1), BoardElement.X)
        self.assertEqual(self.game.board.get_cell(2, 0), BoardElement.X)
        self.assertTrue(self.game.is_game_over())
        self.assertEqual(self.game.get_winner(), "X")



#
# if __name__ == "__main__":
#     unittest.main()