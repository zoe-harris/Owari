# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

"""

class MiniMax:

    def __init__():
        self.beta = 0
        self.alpha = 0

    # return the greater of two given values
    def max(val_1, val_2):

        if val_1 >= val_2:
            return val_1
        else:
            return val_2

    # generate all the successors of a state
    def successors(state):
        return list of successors

    def max_value(state, alpha, beta):

        if terminal_test(state):
            return utility(state)

        v = negative infinity

        for s in successors(state):
            v = max(v, min_value(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    # return the greater of two given values
    def min(val_1, val_2):

        if val_1 <= val_2:
            return val_1
        else:
            return val_2

    def min_value():

        if terminal_test(state):
            return utility(state)

        v = positive infinity

        for s in successors(state)
            v = min(v, max_value(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v

    def alpha_beta_search(curr_state):
        v = max_value(curr_state, negative infinity, positive infinity)
        return action in Successors(curr_state) with value v

"""