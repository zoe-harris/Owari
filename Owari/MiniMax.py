# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence
import copy
import queue
from Pit import State
import math
import GameBoard

# To check for leaf, successors = empty list
# Global variables
LOOK_AHEAD = 1
POSITIVE_INF = float("inf")
NEGATIVE_INF = float("-inf")


# The State class will allow us to create objects that hold the state & its fitness / value of each move to then
# Search through the tree. Need to have a class to create list & make every possible move
class MiniMax:
    def __init__(self, state):
        self.beta = 0
        self.alpha = 0
        self.root = State(state, 0)

    # This method creates every move and inserts them into the successors list of a given state for later navigation
    def generate_moves(self, state):
        moves = queue.Queue(0)
        counter = 0
        curr_state = self.root

        while counter != LOOK_AHEAD:
            # MAX: Check all of OUR possible moves
            for x in range(6):
                option = copy.deepcopy(curr_state)
                option.sow[x]
                curr_state.successors.append(State(option))
                moves.put(option)

            # MIN: Remove the first move from the queue and expand all possible moves from that point
            for y in range(6):
                curr_state = moves.get()
                for x in range(7, 12):
                    option = copy.deepcopy(curr_state)
                    option.sow[x]
                    curr_state.successors.append(State(option))
                    moves.put(option)

            counter += 1

    # This method determines how good of a move the opponent can make
    def calc_fitness(self, state):
        my_fitness = 0
        opp_fitness = 0

        # Determine the fitness value for our side of the board (how good we look)
        for x in range(0, 6):
            my_fitness += state.board[x].seeds

            # If we have an empty pit & the opposite pit is not empty, our fitness increases
            if (state.board[x] == 0) and (state.board[state.opposite.get(x)] != 0):
                my_fitness += 1
        my_fitness += state.board[6].seeds

        # Determine the fitness value for the opponent's side of the board (how good they look)
        for x in range(7, 13):
            opp_fitness += state.board[x].seeds

            # If they have an empty pit & the opposite pit is not empty, their fitness increases
            if (state.board[x] == 0) and (state.board[state.opposite.get(x)] != 0):
                opp_fitness += 1
        opp_fitness += state.board[13].seeds

        return opp_fitness - my_fitness  # Since we'll always start on a MIN field, we need THEIR fitness for pruning

    # This method will return the greater of two given values
    def max(self, val_1, val_2):

        if val_1 >= val_2:
            return val_1
        else:
            return val_2

    # This method will return the list of the successors of a state
    def successors(self, state, v):
        for x in range(len(state.successors)):
            if state.successors[x] == v:
                return state.successors[x]

    # This method returns the largest value in the successors of a given state
    def max_value(self, state, alpha, beta):
        if self.terminal_test(state):
            return self.utility(state)

        v = NEGATIVE_INF

        for s in self.successors(self, state):
            v = max(v, self.min_value(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    # return the greater of two given values
    def min(self, val_1, val_2):
        if val_1 <= val_2:
            return val_1
        else:
            return val_2

    # This method returns the smallest value in the successors of a given state
    def min_value(self, state, alpha, beta):

        if self.terminal_test(state):  # If game over
            return self.utility(state)  # Numeric outcome of game

        v = POSITIVE_INF

        for s in self.successors(state):
            v = min(v, self.max_value(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    # This method does a thing
    def alpha_beta_search(self, curr_state):
        v = self.max_value(curr_state, NEGATIVE_INF, POSITIVE_INF)
        return self.successors(curr_state, v)

    # This method determines if the game is over
    def terminal_test(self, state):
        state.game_over()

    # TO DO: This method determines the numberic outcome of the game
    def utility(self, state):
        test = 0
