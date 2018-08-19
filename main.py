import numpy as np


class Piece:

    def __init__(self, piece, color, location):
        self.piece = piece
        self.color = color
        self.location = location
        self.multiplier = 1 if color == 'white' else -1


    def valid_move(self):
        pass

    def get_valid_moves(self):
        pass

    def __repr__(self):
        return self.piece[0] + self.color[0]

    def __str__(self):
        return self.piece[0] + self.color[0]


class Pawn(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'pawn', color, location)

    def get_valid_moves(self):
        # add ability to move two steps in first move
        # and add en passant
        # basic valid moves:
        # move forward
        # move diagonal if you want to take a piece
        # step one: query the board to find current positions of other pieces
        # find pieces that are eligible for capture, and squares that are eligible for moving
        pass


class Board:

    def __init__(self):
        self.board = np.empty((8, 8), dtype=object)
        self.positions = dict()

        for i in range(8):
            self.board[1][i] = Pawn('black', (1, i))
            self.board[6][i] = Pawn('white', (6, i))

    def poll_board(self):
        for i in range(8):
            for j in range(8):
                self.positions[(i, j)] = self.board[i][j]



    def print(self):
        print('     a  b  c  d  e  f  g  h')
        print('     0  1  2  3  4  5  6  7')
        for i, row in enumerate(self.board):
            print_row = str(i) + ': |' + '|'.join([item.__repr__() if item is not None else '  ' for item in row]) + '|'
            print(print_row)


my_board = Board()
my_board.print()
