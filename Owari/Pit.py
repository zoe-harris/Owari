# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence


class Pit:

    # Each pit object represents a pit on the Owari board
    def __init__(self, seeds=0):
        # This represents the number of seeds in a pit
        self.seeds = seeds
        # This is the next pit on the board (the pit a seed will be next dropped into when sown)
        self.next = None


class State:
    def __init__(self, state):
        self.state = state
        self.fitness = -500
        self.branch_num = -1
        self.successors = []
