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
POSITIVE_INF = 1000  #float("inf")
NEGATIVE_INF = -1000  #float("-inf")


# The State class will allow us to create objects that hold the state & its fitness / value of each move to then
# Search through the tree. Need to have a class to create list & make every possible move
class MiniMax:
    def __init__(self, state):
        self.beta = 0
        self.alpha = 0
        self.root = State(state)
        self.node = None

    # TO DO: Figure out why we always start with pit 7?
    # This method creates every move and inserts them into the successors list of a given state for later navigation
    def generate_moves(self):
        moves = queue.Queue(0)
        counter = 0
        curr_state = self.root

        # MAX: Check all of the COMPUTER'S possible moves
        for x in range(7, 13):
            if curr_state.state.board[x].seeds != 0:
                # If the current pit is not empty, generate a sow
                option = copy.deepcopy(curr_state)
                option.state.sow(x)
                option.branch_num = x
                option.fitness = self.calc_fitness(option)
                curr_state.successors.append(option)
                moves.put(option)

        while counter != LOOK_AHEAD:
            size = moves.qsize()
            # MIN: Remove the first move from the queue and expand all possible HUMAN moves from that point
            for y in range(size):  # Ensures we are only looping + creating enough options for what exists
                curr_state = moves.get()
                for x in range(6):
                    # If the current pit is not empty, generate a sow
                    if curr_state.state.board[x].seeds != 0:
                        option = copy.deepcopy(curr_state)
                        option.state.sow(x)
                        option.fitness = self.calc_fitness(option)
                        curr_state.successors.append(option)
                        moves.put(option)

            size = moves.qsize()
            # MAX: Check all of the COMPUTER'S possible moves
            for y in range(size):  # Ensures we are only looping + creating enough options for what exists
                curr_state = moves.get()
                for x in range(7, 13):
                    # If the current pit is not empty, generate a sow
                    if curr_state.state.board[x].seeds != 0:
                        option = copy.deepcopy(curr_state)
                        option.state.sow(x)
                        option.fitness = self.calc_fitness(option)
                        curr_state.successors.append(option)
                        moves.put(option)

            counter += 1

    # TO DO: Determine "better" fitness
    # This method determines how good of a move the opponent can make
    def calc_fitness(self, state):
        """ Computer Wants:
                -Minimize pit < 3 seeds on our side
                -Maximize pit < 3 on opponent side
                -Large number of seeds into 1 pit on our side
                """
        fitness = 0
        curr_state = state.state
        for x in range(0, 6):
            if curr_state.board[x].seeds < 3:
                fitness += 3

        for x in range(7, 13):
            if curr_state.board[x].seeds == 0:
                fitness += 4
            elif curr_state.board[x].seeds > 12:
                fitness += 2
            elif curr_state.board[x].seeds > 3:
                fitness += 3
            else:
                fitness -= 3

        if curr_state.board[6].seeds < curr_state.board[13].seeds:
            fitness += 1

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
            return self.utility(curr_state)  # Numeric outcome of game

        # We are at a leaf (bottom of the tree), return the fitness
        if not curr_state.successors:
            return curr_state.fitness  # self.calc_fitness(curr_state)

        v = POSITIVE_INF

        for s in curr_state.successors:
            v = min(v, self.max_value(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
            s.fitness = v
        return v

    # This method kicks off the alpha-beta pruning
    def alpha_beta_search(self):
        curr_state = self.root
        # If there is only one move to make, then don't waste time
        if len(self.root.successors) == 1:
            return self.root.successors[0].branch_num

        # Else, perform alpha beta pruning to find the best move
        v = self.max_value(curr_state, NEGATIVE_INF, POSITIVE_INF)
        return self.successors(curr_state, v).branch_num

    # TO DO: Clean this up / find a better way to handle this.
    # This method determines the numeric outcome of the game
    def utility(self, state):
        if state.state.board[6].seeds > state.state.board[13].seeds:
            return -500
        else:
            return 500
