import copy
from random import randint


class Computer:
    def __init__(self):
        self.chip = '🔴'
        self.enemy_chip = '🟡'

    def get_chip(self):
        return self.chip

    def get_enemy_chip(self):
        return self.enemy_chip

    def __str__(self):
        return f"Computer is playing with {self.chip}"

    @staticmethod
    def simulation_move(board, column, chip):
        temporary_board = copy.deepcopy(board)
        temporary_board.move(chip, column)
        return temporary_board

    def move(self, board):
        for column in range(7):
            if board.check_if_not_full(column):
                temporary_board = self.simulation_move(board, column, self.chip)
                if temporary_board.check_win():
                    return column

        for column in range(7):
            if board.check_if_not_full(column):
                temporary_board = self.simulation_move(board, column, self.enemy_chip)
                if temporary_board.check_win():
                    return column

        while True:
            column = randint(0, 6)
            if board.check_if_not_full(column):
                return column
