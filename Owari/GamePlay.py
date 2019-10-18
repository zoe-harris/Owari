# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from GameBoard import GameBoard


class GamePlay:

    def __init__(self):
        self.board = GameBoard()

    # prompt user to choose which player moves first, computer or human
    def get_moves_first(self):

            valid_input = ["HUMAN", "COMPUTER"]
            user_input = ''

            while user_input not in valid_input:
                user_input = input("Who Moves First? [HUMAN / COMPUTER] ")

            return user_input

    # method controls flow of game play, exits when game is over
    def play(self):
        """Steps:
            1. Determine whose moving first
                1a. If moves_first = 1
                    while game_over() is false:
                        get_human_move()
                        get_computer_move()
                1b. If moves_first = 2
                    while game_over() is false:
                        get_computer_move()
                        get_human_move() """
        print("Time is an illusion.")

    """This routine (GetHumanPlayerMove) will prompt the human opponent (NORTH) to specify the pit from which they
     want to move stones."""
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

    """This routine (GenerateComputerPlayerMove) will call GenerateMoves() for the min-max algorithm."""
    def get_computer_move(self):
        """Steps:
            1. Call GenerateMoves()
            2. pit_num = returned from generate_moves
            3. sow(pit_num)"""
        print("Prepare for the robotic overlords.")

    def sow(self, pit_num):
        """Steps:
        """
        print("You reap what you sow.")

    def steal(self, pit_num):
        """Steps:"""
        print("Yoink.")

    def game_over(self):
        """Steps:"""
        print("Have we finished yet??")
