# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from GameBoard import GameBoard


class GamePlay:

    def __init__(self):
        self.board = GameBoard()

    # prompt user to choose which player moves first, computer or human
    def get_moves_first(self):

            valid = False
            user_input = ''

            while not valid:
                user_input = input("Who Moves First? [HUMAN / COMPUTER] ")
                if user_input == "HUMAN" or user_input == "COMPUTER":
                    valid = True

            return user_input

    # get + play human and computer moves until game_over() returns True
    def play(self):

        print("~~~~~~~~~~~~~ LET THE GAME BEGIN ~~~~~~~~~~~~~")

        # get which player will take the first turn
        first_player = self.get_moves_first()

        # game plays with computer player taking the first turn
        if first_player is "COMPUTER":

            while True:
                self.board.sow(self.get_computer_move)
                self.board.display()
                if self.board.game_over():
                    break
                self.board.sow(self.get_human_move)
                self.board.display()
                if self.board.game_over():
                    break

        # game plays with human player taking the first turn
        if first_player is "HUMAN":

            while True:
                self.board.sow(self.get_human_move)
                self.board.display()
                if self.board.game_over():
                    break
                self.board.sow(self.get_computer_move)
                self.board.display()
                if self.board.game_over():
                    break

        print("~~~~~~~~~~~~~~~~~~ GAME OVER ~~~~~~~~~~~~~~~~~")
        print("HUMAN'S TOTAL SEEDS: ", self.board.human_seeds())
        print("COMPUTER'S TOTAL SEEDS: ", self.board.computer_seeds())

    # prompt user until a valid move has been input
    def get_human_move(self):

        human_move = -1
        valid = False

        while not valid:
            valid = True
            try:
                human_move = int(input("Enter move: "))
            except ValueError:
                human_move = int(input("Input must be a positive integer. Enter move: "))
                valid = False
            if human_move < 0 or human_move > 6:
                human_move = input("You must enter a pit number 0-6. Enter move: ")
                valid = False
            if self.board.board[human_move].seeds == 0:
                human_move = input("The pit you selected is empty. Enter move: ")
                valid = False

        return human_move

    # generate computer move using mini-max with alpha-beta pruning
    # FIXME: this method currently returns a user-input pit for the sake of testing.
    #  Once mini-max is completed it should be rewritten accordingly.
    def get_computer_move(self):

        computer_move = -1
        valid = False

        while not valid:
            valid = True
            try:
                computer_move = int(input("Enter move: "))
            except ValueError:
                computer_move = int(input("Input must be a positive integer. Enter move: "))
                valid = False
            if computer_move < 7 or computer_move > 12:
                computer_move = input("You must enter a pit number 7-12. Enter move: ")
                valid = False
            if self.board.board[computer_move].seeds == 0:
                computer_move = input("The pit you selected is empty. Enter move: ")
                valid = False

        return computer_move
