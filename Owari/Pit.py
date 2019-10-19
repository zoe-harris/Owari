# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence


class Pit:

    def __init__(self, seeds=0):
        self.seeds = seeds
        self.opponent_goal = False
        self.my_goal = False
        self.next = None
