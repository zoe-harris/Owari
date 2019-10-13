# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence


class Gameplay:
    def __init__(self):
        print("Lets get it started!")
        #game_board = GameBoard() #Initialize game board

    """This method (GetWhoMovesFirst) will interactively prompt the human opponent to select whether he or she wants
    to move first or second."""
    def get_moves_first(self):
        """Steps:
            1. Prompt opponent to determine if they move first or second.
                1a. Repeat prompt if incorrect
            2. gameplay_loop(user_input) """

    """This method will run the general gameplay loop."""
    def gameplay_loop(self, moves_first):
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
        """Steps:
            1. Prompt human for correct pit number. (7-12)
                1a. If empty, error message & redisplay
            2. pit_num = user_input
            3. sow(pit_num)"""
        print("Woooooo humans rule!")

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
