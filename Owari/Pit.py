# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence


class Pit:

    def __init__(self, seeds=0):
        self.seeds = seeds
        self.next = None


class State:
    def __init__(self, state):
        self.state = state
        self.fitness = -500
        self.branch_num = -1
        self.successors = []
