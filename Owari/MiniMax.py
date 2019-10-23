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
POSITIVE_INF = 1000#float("inf")
NEGATIVE_INF = -1000#float("-inf")


# The State class will allow us to create objects that hold the state & its fitness / value of each move to then
# Search through the tree. Need to have a class to create list & make every possible move
class MiniMax:
    def __init__(self, state):
        self.beta = 0
        self.alpha = 0
        self.root = State(state)
        self.node = None

    # This method creates every move and inserts them into the successors list of a given state for later navigation
    def generate_moves(self):
        moves = queue.Queue(0)
        counter = 0
        curr_state = self.root

        while counter != LOOK_AHEAD:
            # MAX: Check all of OUR possible moves
            for x in range(6):
                option = copy.deepcopy(curr_state)
                option.state.sow(x)
                option.pit = x
                option.branch_num = x
                curr_state.successors.append(option)
                moves.put(option)

            # MIN: Remove the first move from the queue and expand all possible moves from that point
            for y in range(6):
                curr_state = moves.get()
                for x in range(7, 13):
                    option = copy.deepcopy(curr_state)
                    option.state.sow(x)
                    option.pit = x
                    option.branch_num = y
                    self.calc_fitness(option)
                    curr_state.successors.append(option)
                    moves.put(option)

            counter += 1

    # This method determines how good of a move the opponent can make
    def calc_fitness(self, state):
        my_side = 0
        opp_side = 0
        fitness = 0
        curr_state = state.state
        for x in range(0, 6):
            my_side += curr_state.board[x].seeds

        for x in range(7, 13):
            opp_side += curr_state.board[x].seeds
            if (curr_state.board[x] == 0) and (curr_state.board[curr_state.opposite.get(x)] != 0):
                fitness += 1

        if my_side < opp_side:
            fitness += (opp_side - my_side)

        if curr_state.board[6].seeds < curr_state.board[13].seeds:
            fitness += 1

        state.fitness = fitness
        print(fitness)
        return fitness

    # This method will return the greater of two given values
    def max(self, val_1, val_2):

        if val_1 >= val_2:
            return val_1
        else:
            return val_2

    # This method searches the successors for the node that v came from
    def successors(self, state, v):
        # If value is found, return that state
        if state.fitness == v:
            print("Value found ", v)
            return state

        # Starting at the current state, check all possible moves
        for s in state.successors:
            # Search deeper in the branch
            if s.successors:
                search = self.successors(s, v)
                if search is not None:
                    return search

        return None

    # This method returns the largest value in the successors of a given state
    def max_value(self, curr_state, alpha, beta):
        if curr_state.state.game_over():  # Terminal Test
            return self.utility(curr_state)

        # We are at a leaf (bottom of the tree), return the fitness
        if not curr_state.successors:
            return curr_state.fitness

        v = NEGATIVE_INF

        for s in curr_state.successors:
            v = max(v, self.min_value(s, alpha, beta))
            if v >= beta:
                self.node = s
                return v
            alpha = max(alpha, v)
            s.fitness = v
        return v

    # return the greater of two given values
    def min(self, val_1, val_2):
        if val_1 <= val_2:
            return val_1
        else:
            return val_2

    # This method returns the smallest value in the successors of a given state
    def min_value(self, curr_state, alpha, beta):
        if curr_state.state.game_over():  # If game over
            curr_state.state.display()
            return self.utility(curr_state)  # Numeric outcome of game

        # We are at a leaf (bottom of the tree), return the fitness
        if not curr_state.successors:
            return curr_state.fitness  # self.calc_fitness(curr_state)

        v = POSITIVE_INF

        for s in curr_state.successors:
            v = min(v, self.max_value(s, alpha, beta))
            if v <= alpha:
                self.node = s
                return v
            beta = min(beta, v)
            s.fitness = v
        return v

    # This method does a thing
    def alpha_beta_search(self):
        curr_state = self.root
        v = self.max_value(curr_state, NEGATIVE_INF, POSITIVE_INF)
        return self.successors(curr_state, v).branch_num

    # This method determines the numberic outcome of the game
    def utility(self, state):
        if state.board[6].seeds > state.board[13].seeds:
            print("I win.")
        else:
            print("Opponent Wins")
