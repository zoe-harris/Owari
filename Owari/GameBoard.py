# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from Pit import Pit


class GameBoard:

    def __init__(self):

        self.owari_board = []

        # make six pits and a goal for myself
        for i in range(0, 6):
            self.owari_board.append(Pit(4))
        self.owari_board.append(Pit(0))
        self.owari_board[6].my_goal = True

        # make six pits and a goal for opponent
        for i in range(7, 13):
            self.owari_board.append(Pit(4))
        self.owari_board.append(Pit(0))
        self.owari_board[13].opponent_goal = True

    def sow(self, pit):
        num_seeds = self.owari_board[pit]
        self.owari_board[pit] = 0
        for x in range(num_seeds):
            self.owari_board[pit + x] = 0

    """def game_over():
        check if all six of either players' pits are empty
        if so, return True

    def display():
        print formatted self.owari_board

    def my_seeds()
        return # of seeds in my goal

    def opponent_seeds()
        return # of seeds in opponent's goal
    """