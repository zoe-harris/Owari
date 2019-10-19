# Zoe Harris & Rachel Lewis
# Programming Assignment #3
# CSCE405 Artificial Intelligence

from Pit import Pit


class GameBoard:

    def __init__(self):

        # initialize board, which will be a list of fourteen Pit nodes
        self.board = []

        # dictionary of which pits are opposite each other on the board
        self.opposite = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7,
                         12: 0, 11: 1, 10: 2, 9: 3, 8: 3, 7: 5}

        # make six pits and a goal for myself
        for i in range(0, 6):
            self.board.append(Pit(3))
        self.board.append(Pit(0))
        self.board[6].my_goal = True

        # make six pits and a goal for opponent
        for i in range(7, 13):
            self.board.append(Pit(3))
        self.board.append(Pit(0))
        self.board[13].opponent_goal = True
        
        # set next for all pits on the board
        for i in range(13):
            self.board[i].next = self.board[i + 1]
        self.board[13].next = self.board[0]

    # Method prints the current state of the game board.
    def display(self):

        # start with new blank line
        print('')

        # print opponent pits
        print("    ", end='')
        for i in range(12, 6, -1):
            print(f'{self.board[i].seeds}  ', end='')

        # print both goal pits
        print(f'\n {self.board[13].seeds}                    {self.board[6].seeds}')

        # print my pits
        print("    ", end='')
        for i in range(0, 6):
            print(f'{self.board[i].seeds}  ', end='')

        # end with new blank line
        print('')

    def human_capture(self, curr_pit, curr_pit_index):
        # determine if last pit sown was empty and on human side
        if curr_pit.seeds == 0 and 0 <= curr_pit_index <= 5:
            # find the pit opposite the current pit
            opposite_pit = self.board[self.opposite.get(curr_pit_index)]
            # add that pit's seeds to human goal
            self.board[6].seeds += opposite_pit.seeds
            # zero out the opposite pit
            opposite_pit.seeds = 0

    def computer_capture(self, curr_pit, curr_pit_index):
        # determine if last pit sown was empty and on computer side
        if curr_pit.seeds == 0 and 7 <= curr_pit_index <= 12:
            # find the pit opposite the current pit
            opposite_pit = self.board[self.opposite.get(curr_pit_index)]
            # add that pit's seeds to computer goal
            self.board[13].seeds += opposite_pit.seeds
            # zero out the opposite pit
            opposite_pit.seeds = 0

    # 'Sow' the seeds from the given pit by depositing one seed in each subsequent
    # pit until no seeds are left. A capture method is called so that if the last
    # pit sown was empty, the opponent's seeds will be captured.
    def sow(self, pit):

        # determine whether play is human or computer using pit index
        human = False
        computer = False

        if 0 <= pit <= 6:
            human = True
        else:
            computer = True

        # store the Pit object and index you are starting with
        curr_pit = self.board[pit]
        curr_pit_index = pit

        if human:
            for i in range(self.board[pit].seeds):
                if curr_pit_index != 13:
                    curr_pit.seeds += 1
                curr_pit = curr_pit.next
                curr_pit_index += 1
            self.human_capture(curr_pit, curr_pit_index)

        if computer:
            for i in range(self.board[pit].seeds):
                if curr_pit_index != 6:
                    curr_pit.seeds += 1
                curr_pit = curr_pit.next
                curr_pit_index += 1
            self.computer_capture(curr_pit, curr_pit_index)

        # add final seed to last pit and zero out starting pit
        curr_pit.seeds += 1
        self.board[pit].seeds = 0

    # Determine whether the game of Owari is over: if all six pits on either side are empty
    # then the game is over and 'True' will be returned.
    def game_over(self):

        # check if all pits on my side are empty
        my_side_empty = True
        for i in range(0, 6):
            if self.board[i].seeds > 0:
                my_side_empty = False

        # check if all opponent pits are empty
        opponent_side_empty = True
        for i in range(7, 13):
            if self.board[i].seeds > 0:
                opponent_side_empty = False

        # if all pits on either side are empty, game over
        if my_side_empty or opponent_side_empty:
            return True
        else:
            return False

    def human_seeds(self):
        return self.board[6].seeds

    def computer_seeds(self):
        return self.board[13].seeds
