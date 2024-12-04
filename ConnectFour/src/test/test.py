import unittest

from src.board.board import Board
from src.domain.computer import Computer
from src.domain.player import Player


class Test(unittest.TestCase):

    def test_computer(self):
        computer=Computer()
        self.assertEqual(computer.get_chip(),'🔴')
        self.assertEqual(computer.get_enemy_chip(), '🟡')

    def test_player_input(self):
        chip='🟡'
        player=Player('LALA',chip)

        self.assertEqual(player.get_name(),'LALA')
        self.assertEqual(player.get_chip(),'🟡')

    def test_board_str(self):
        board=Board()
        expected_output = "    1    2    3    4    5    6    7  \n  " \
                          "+----+----+----+----+----+----+----+\n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n  " \
                          "+----+----+----+----+----+----+----+ \n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n  " \
                          "+----+----+----+----+----+----+----+ \n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n  " \
                          "+----+----+----+----+----+----+----+ \n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n  " \
                          "+----+----+----+----+----+----+----+ \n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n  " \
                          "+----+----+----+----+----+----+----+ \n " \
                          "| ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ | ⚪ |\n " \
                          " +----+----+----+----+----+----+----+ \n"
        self.assertEqual(str(board), expected_output)

    def test_win_diagonal_left_right(self):
        board = Board()
        self.assertEqual(board.check_win(), False)
        board.move('🟡', 1)
        board.move('🔴', 2)
        board.move('🟡', 2)
        board.move('🔴', 3)
        board.move('🔴', 3)
        board.move('🟡', 3)
        board.move('🔴', 4)
        board.move('🔴', 4)
        board.move('🔴', 4)
        board.move('🟡', 4)
        self.assertEqual(board.check_win(), True)

