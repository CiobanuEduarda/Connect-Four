class Board:

    def __init__(self):
        self.data_board = [['⚪' for _ in range(7)] for _ in range(6)]

    def get_board(self):
        return self.data_board

    def __str__(self):
        table = "    1    2    3    4    5    6    7  \n"
        table += "  +----+----+----+----+----+----+----+\n"
        for i in range(6):
            for j in range(7):
                table += ' | '
                table += str(self.data_board[i][j])
            table += ' |\n'
            table += "  +----+----+----+----+----+----+----+ \n"
        return table

    def still_drawing(self):
        for i in range(6):
            for j in range(7):
                if self.data_board[i][j] == '⚪':
                    return True
        return False
    def check_win(self):
        # four chips with the same color on the same row

        for i in range(6):
            for j in range(4):
                if self.data_board[i][j] != '⚪':
                    if self.data_board[i][j] == self.data_board[i][j + 1]:
                        if self.data_board[i][j] == self.data_board[i][j + 2]:
                            if self.data_board[i][j] == self.data_board[i][j + 3]:
                                return True

        # four chips with the same color on the same column
        for i in range(3):
            for j in range(7):
                if self.data_board[i][j] != '⚪':
                    if self.data_board[i][j] == self.data_board[i + 1][j]:
                        if self.data_board[i][j] == self.data_board[i + 2][j]:
                            if self.data_board[i][j] == self.data_board[i + 3][j]:
                                return True
        # four chips with the same color on the same diagonal (left to right)
        for i in range(3):
            for j in range(4):
                if self.data_board[i][j] != '⚪':
                    if self.data_board[i][j] == self.data_board[i + 1][j + 1]:
                        if self.data_board[i][j] == self.data_board[i + 2][j + 2]:
                            if self.data_board[i][j] == self.data_board[i + 3][j + 3]:
                                return True

        # four chips with the same color on the same diagonal ( right to left)
        for i in range(3):
            for j in range(6, 2, -1):
                if self.data_board[i][j] != '⚪':
                    if self.data_board[i][j] == self.data_board[i + 1][j - 1]:
                        if self.data_board[i][j] == self.data_board[i + 2][j - 2]:
                            if self.data_board[i][j] == self.data_board[i + 3][j - 3]:
                                return True
        return False

    def check_if_not_full(self,column):
        i=5
        while i>=0:
            if self.data_board[i][column]== '⚪':
                return True
            i-=1
        return False

    def move(self, chip,column):
        i=5
        while i>=0:
            if self.data_board[i][column] == '⚪':
                self.data_board[i][column] =chip
                return True
            i-=1
        return False


