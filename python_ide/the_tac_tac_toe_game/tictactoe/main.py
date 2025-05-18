from player import Player
from game import Game
from board_element import BoardElement

def main():
    player1 = Player(BoardElement.X)
    player2 = Player(BoardElement.O)
    game = Game(player1, player2)
    print("Welcome to Tic-Tac-Toe!")
    print("Enter a position (1-9):")


    while not game.is_game_over():
        game.board.display()
        print("Player " + game.current_player.symbol.value + "'s turn.")
        try:
            position = int(input("Enter position (1-9): "))
            row_index, col_index = game.convert_position(position)
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        if game.board.get_cell(row_index, col_index) != BoardElement.EMPTY:
            print("That spot is taken! Try again.")
            continue
        game.make_move(row_index, col_index)

    game.board.display()
    if game.get_winner() == "Draw":
        print("It's a tie!")
    else:
        print("Game Over! Player " + game.get_winner() + " wins!")

if __name__ == "__main__":
    main()