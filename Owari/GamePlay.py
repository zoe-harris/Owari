# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from GameBoard import GameBoard
from MiniMax import MiniMax


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
        if first_player == "COMPUTER":

            while True:
                self.board.sow(self.get_computer_move())
                self.board.display()
                if self.board.game_over():
                    break
                self.board.sow(self.get_human_move())
                self.board.display()
                if self.board.game_over():
                    break

        # game plays with human player taking the first turn
        if first_player == "HUMAN":

            while True:
                self.board.sow(self.get_human_move())
                self.board.display()
                if self.board.game_over():
                    break
                computer_move = self.get_computer_move()
                print("\nThe computer chose pit ", computer_move)
                self.board.sow(computer_move)
                self.board.display()
                if self.board.game_over():
                    break

        print("~~~~~~~~~~~~~~~~~~ GAME OVER ~~~~~~~~~~~~~~~~~")
        self.board.display()
        # print("HUMAN'S TOTAL SEEDS: ", self.board.human_seeds())
        # print("COMPUTER'S TOTAL SEEDS: ", self.board.computer_seeds())

        if self.board.human_goal.seeds > self.board.computer_goal.seeds:
            print("~~~~~~~~~~~~~~~~~ HUMAN WINS ~~~~~~~~~~~~~~~~~")
        elif self.board.human_goal.seeds < self.board.computer_goal.seeds:
            print("~~~~~~~~~~~~~~~ COMPUTER WINS ~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~ It's a draw! ~~~~~~~~~~~~~~~~")

    # prompt user until a valid move has been input
    def get_human_move(self):

        human_move = -1
        valid = False

        while not valid:
            valid = True
            try:
                human_move = int(input("\nEnter move: "))
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

        move = MiniMax(self.board)
        move.generate_moves()
        computer_move = move.alpha_beta_search()
        """computer_move = -1
        valid = False

        while not valid:
            valid = True
            try:
                computer_move = int(input("COMPUTER MOVE: "))
            except ValueError:
                print("Input must be a positive integer. ", end='')
                valid = False
            if valid is True and (computer_move < 7 or computer_move > 12):
                print("You must enter a pit number 7-12. ", end='')
                valid = False
            if valid is True and (self.board.board[computer_move].seeds == 0):
                print("The pit you selected is empty. ", end='')
                valid = False"""

        return computer_move
