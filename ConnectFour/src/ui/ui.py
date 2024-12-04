from colorama import Fore, Style

from src.board.board import Board
from src.domain.computer import Computer
from src.domain.player import Player

COMPUTER = 1
PLAYER = 2
EXIT = 0


class Ui:
    @staticmethod
    def print_menu():
        print(f"{Fore.MAGENTA}  Welcome to Connect Four! {Style.RESET_ALL}")
        print()
        print(f"{Fore.CYAN}         MENU        ")
        print()
        print("1 - Player VS Computer")
        print("2 - Player VS Player")
        print(f"0 - Exit the game{Style.RESET_ALL}")

    def run_menu(self):
        self.print_menu()
        while True:
            while True:
                try:
                    print()
                    option = int(input("Enter the desired option: "))
                    print()
                    break
                except ValueError as ve:
                    print(f"{Fore.GREEN}Invalid option!{Style.RESET_ALL}", ve)

            if option == COMPUTER:
                self.player_vs_computer()
            elif option == PLAYER:
                self.player_vs_player()
            elif option == EXIT:
                print(f"{Fore.MAGENTA}Thank you for playing!{Style.RESET_ALL}")
                break
            else:
                print("Invalid option!")

    def valid_column(self, column):
        try:
            column = int(column)
        except ValueError:
            return False
        if not 1 <= column <= 7:
            return False
        return True

    def player_vs_computer(self):
        column1 = None
        print(f"{Fore.MAGENTA} You choose to play with the computer")
        player_name = input(f"{Fore.YELLOW}Enter your name:{Style.RESET_ALL}")
        chip_player = '🟡'
        player = Player(player_name, chip_player)
        print(player)
        computer = Computer()
        chip_computer = '🔴'
        board = Board()
        print(board)
        print(f"{Fore.YELLOW}{player_name} you start:{Style.RESET_ALL}")

        while board.still_drawing():
            column1 = input(f"{Fore.YELLOW}Your turn! Choose a column{Style.RESET_ALL}")
            while not self.valid_column(column1):
                column1 = input("Column must be an integer between 1 and 7:")

            column1 = int(column1)
            column1 -= 1
            while not board.check_if_not_full(column1):
                print("The column is full!Try another one!")
                while not self.valid_column(column1):
                    column1 = input("The chosen column is full! Please choose another one:")
                column1 = int(column1)
                column1 -= 1

            board.move(chip_player, column1)
            print(board)

            if board.check_win():
                print(f"{Fore.GREEN}{player_name} won!!!!!!{Style.RESET_ALL}")
                break

            print(f"{Fore.RED} Computer's turn: {Style.RESET_ALL}")
            column2 = computer.move(board)
            board.move(chip_computer, column2)
            print(board)

            if board.check_win():
                print(f"{Fore.GREEN}Computer won!!!!!!{Style.RESET_ALL}")
                break


    def player_vs_player(self):
        column1 = None
        column2 = None
        board = Board()
        player1_name = input(f"{Fore.RED}Enter first player name:{Style.RESET_ALL}")
        chip1 = '🔴'
        player1 = Player(player1_name, chip1)
        print(player1)

        player2_name = input(f"{Fore.YELLOW}Enter second player name:{Style.RESET_ALL}")
        chip2 = '🟡'
        player2 = Player(player2_name, chip2)
        print(player2)
        print(board)

        print(f"{Fore.RED}{player1_name} you start!{Style.RESET_ALL}")
        while board.still_drawing():
            column1 = input(f"{Fore.RED}Choose a column{Style.RESET_ALL}")
            while not self.valid_column(column1):
                column1 = input("Column must be an integer between 1 and 7:")

            column1 = int(column1)
            column1 -= 1
            while not board.check_if_not_full(column1):
                print("The column is full!Try another one!")
                while not self.valid_column(column1):
                    column1 = input("The chosen column is full! Please choose another one:")
                column1 = int(column1)
                column1 -= 1

            board.move(chip1, column1)
            print(board)

            if board.check_win():
                print(f"{Fore.GREEN}{player1_name} won!!!!!!{Style.RESET_ALL}")
                break

            column2 = input(f"{Fore.YELLOW}Choose a column{Style.RESET_ALL}")
            while not self.valid_column(column2):
                column2 = input("Column must be an integer between 1 and 7:")

            column2 = int(column2)
            column2 -= 1

            while not board.check_if_not_full(column2):
                print("The column is full!Try another one!")
                while not self.valid_column(column2):
                    column2 = input("The chosen column is full! Please choose another one:")

                column2 = int(column2)
                column2 -= 1

            board.move(chip2, column2)
            print(board)

            if board.check_win():
                print(f"{Fore.GREEN}{player2_name} won!!!!!!{Style.RESET_ALL}")
                break
