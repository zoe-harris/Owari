# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from Pit import Pit


class GameBoard:

    def __init__(self):

        self.owari_board = []

        # make six pits and a goal for myself
        for i in range(0, 6):
            self.owari_board.append(Pit(3))
        self.owari_board.append(Pit(0))
        self.owari_board[6].my_goal = True

        # make six pits and a goal for opponent
        for i in range(7, 13):
            self.owari_board.append(Pit(3))
        self.owari_board.append(Pit(0))
        self.owari_board[13].opponent_goal = True

        # set next for all pits on the board
        for i in range(13):
            self.owari_board[i].next = self.owari_board[i + 1]
        self.owari_board[13].next = self.owari_board[0]

    def display(self):

        # start with new blank line
        print('')

        # print opponent pits
        print("    ", end='')
        for i in range(12, 6, -1):
            print(f'{self.owari_board[i].seeds}  ', end='')

        # print both goal pits
        print(f'\n {self.owari_board[13].seeds}                    {self.owari_board[6].seeds}')

        # print my pits
        print("    ", end='')
        for i in range(0, 6):
            print(f'{self.owari_board[i].seeds}  ', end='')

        # end with new blank line
        print('')

    def sow(self, pit):

        print("\nSow from pit ", pit, ":")

        # dictionary of which pits are opposite each other on the board
        opposite = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7}

        # sow one seed from the given pit into each of the following
        # pits (unless that pit is your opponent's goal) until you are out of seeds
        curr_pit = self.owari_board[pit]
        curr_pit_index = pit
        for i in range(self.owari_board[pit].seeds):
            if not curr_pit.opponent_goal:
                curr_pit.seeds += 1
            curr_pit = curr_pit.next
            curr_pit_index += 1

        # if landed on an empty pit on my side, capture seeds opposite
        if curr_pit.seeds == 0 and 0 <= curr_pit_index <= 6:
            opponent_pit = self.owari_board[opposite.get(curr_pit_index)]
            self.owari_board[6].seeds += opponent_pit.seeds
            opponent_pit.seeds = 0
            curr_pit.seeds += 1

        # the starting pit now has zero seeds
        self.owari_board[pit].seeds = 0

    def game_over(self):

        # check if all pits on my side are empty
        my_side_empty = True
        for i in range(0, 6):
            if self.owari_board[i].seeds > 0:
                my_side_empty = False

        # check if all opponent pits are empty
        opponent_side_empty = True
        for i in range(7, 13):
            if self.owari_board[i].seeds > 0:
                opponent_side_empty = False

        # if all pits on either side are empty, game over
        if my_side_empty or opponent_side_empty:
            return True
        else:
            return False

    def my_seeds(self):
        return self.owari_board[6].seeds

    def opponent_seeds(self):
        return self.owari_board[13].seeds
