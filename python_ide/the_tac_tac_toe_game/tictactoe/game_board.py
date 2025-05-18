from board_element import BoardElement

class GameBoard:
    def __init__(self):
        self.grid = []
        for fill_grid in range(3):
            row = [BoardElement.EMPTY, BoardElement.EMPTY, BoardElement.EMPTY]
            self.grid.append(row)
            

    def is_valid_index(self, row, col):
        is_row_valid = row >= 0 and row < 3
        is_col_valid = col >= 0 and col < 3
        return is_row_valid and is_col_valid


    def is_full(self):
        for row in range(3):
            for col in range(3):
                if self.grid[row][col] == BoardElement.EMPTY:
                    return False
        return True



    def get_cell(self, row, col):
        if self.is_valid_index(row, col):
            return self.grid[row][col]
        return None



    def place_symbol(self, row, col, symbol):
        if self.is_valid_index(row, col):
            if self.grid[row][col] == BoardElement.EMPTY:
                self.grid[row][col] = symbol



    def check_winner(self, symbol):
        for row in range(3):
            row_wins = True
            for col in range(3):
                if self.grid[row][col] != symbol:
                    row_wins = False
            if row_wins:
                return True


        for col in range(3):
            col_wins = True
            for row in range(3):
                if self.grid[row][col] != symbol:
                    col_wins = False
            if col_wins:
                return True


        main_diag_wins = True
        for i in range(3):
            if self.grid[i][i] != symbol:
                main_diag_wins = False
        if main_diag_wins:
            return True


        other_diag_wins = True
        for i in range(3):
            if self.grid[i][2 - i] != symbol:
                other_diag_wins = False
        if other_diag_wins:
            return True
        return False


    def display(self):
        for row in range(3):
            for col in range(3):
                pos = row * 3 + col + 1
                if self.grid[row][col] == BoardElement.EMPTY:
                    value = str(pos)
                else:
                    value = self.grid[row][col].value
                print(value, end=" ")
            print()
        print()