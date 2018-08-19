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
        # todo two steps in first move and add en passant
        # basic valid moves:
        # move forward
        # move diagonal if you want to take a piece
        # step one: query the board to find current positions of other pieces
        # find pieces that are eligible for capture, and squares that are eligible for moving
        possible_positions = [(self.location[0] - (1 * self.multiplier), self.location[1] - 1)
                              , (self.location[0] - (1 * self.multiplier), self.location[1])
                              , (self.location[0] - (1 * self.multiplier), self.location[1] + 1)]
        valid_moves_0 = []
        for position in possible_positions:
            if not (position[0] < 0 or position[0] > 7 or position[1] < 0 or position[1] > 7):
                valid_moves_0.append(position)
        locations = my_board.positions.copy()
        relevant_squares = {key: locations[key] for key in valid_moves_0}
        valid_moves_1 = []
        for square in relevant_squares:
            if not relevant_squares[square] or relevant_squares[square].color != self.color:
                valid_moves_1.append(square)
        if relevant_squares[(self.location[0] - (1 * self.multiplier), self.location[1])]is not None:
            valid_moves_1.append((self.location[0] - (1 * self.multiplier), self.location[1]))
        return valid_moves_1


class Rook(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'rook', color, location)

    def get_valid_moves(self):
        # TODO add castling
        locations = my_board.positions.copy()
        valid_moves = []
        for ii in [1, -1]:
            i = 1
            while 0 <= self.location[0] + i*ii < 8:
                new_x = self.location[0] + i*ii
                if not locations[(new_x, self.location[1])]:
                    valid_moves.append((new_x, self.location[1]))
                    i += 1
                    continue
                if locations[(new_x, self.location[1])].color != self.color:
                    valid_moves.append((new_x, self.location[1]))
                    i += 1
                    break
                if locations[(new_x, self.location[1])].color == self.color:
                    break

        for ii in [1, -1]:
            i = 1
            while 0 <= self.location[1] + i*ii < 8:
                new_y = self.location[1] + i*ii
                if not locations[(self.location[0], new_y)]:
                    valid_moves.append((self.location[0], new_y))
                    i += 1
                    continue
                if locations[(self.location[0], new_y)].color != self.color:
                    valid_moves.append((self.location[0], new_y))
                    i += 1
                    break
                if locations[(self.location[0], new_y)].color == self.color:
                    break
        return valid_moves


class Bishop(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'bishop', color, location)

    def get_valid_moves(self):
        valid_moves = []
        locations = my_board.positions.copy()
        for ii in [1, -1]:
            for jj in [1, -1]:
                i = 1
                new_x = self.location[0] + i*ii
                new_y = self.location[1] + i*jj
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if not locations[(new_x, new_y)]:
                        valid_moves.append((new_x, new_y))
                        i += 1
                        new_x = self.location[0] + i * ii
                        new_y = self.location[1] + i * jj
                        continue
                    if locations[(new_x, new_y)].color != self.color:
                        valid_moves.append((new_x, new_y))
                        break
                    if locations[(new_x, new_y)].color == self.color:
                        break
        return valid_moves


class Knight(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'knight', color, location)

    def get_valid_moves(self):
        # split this into 2 over 1 up and the inverse
        locations = my_board.positions.copy()
        valid_moves = []
        for ii in [1, -1]:
            for jj in [1, -1]:
                new_x = self.location[0] + 2*ii
                new_y = self.location[1] + 1*jj
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if locations[(new_x, new_y)] is None or locations[(new_x, new_y)].color != self.color:
                        valid_moves.append((new_x, new_y))
        for ii in [1, -1]:
            for jj in [1, -1]:
                new_x = self.location[0] + 1*ii
                new_y = self.location[1] + 2*jj
                if 0 <= new_x < 8 and 0 <= new_y < 8:
                    if locations[(new_x, new_y)] is None or locations[(new_x, new_y)].color != self.color:
                        valid_moves.append((new_x, new_y))
        return valid_moves


class Queen(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'Queen', color, location)

    def get_valid_moves(self):
        # will borrow the code for rook + bishop
        locations = my_board.positions.copy()
        valid_moves = []
        # first, 'bishop' moves
        for ii in [1, -1]:
            for jj in [1, -1]:
                i = 1
                new_x = self.location[0] + i*ii
                new_y = self.location[1] + i*jj
                while 0 <= new_x < 8 and 0 <= new_y < 8:
                    if not locations[(new_x, new_y)]:
                        valid_moves.append((new_x, new_y))
                        i += 1
                        new_x = self.location[0] + i * ii
                        new_y = self.location[1] + i * jj
                        continue
                    if locations[(new_x, new_y)].color != self.color:
                        valid_moves.append((new_x, new_y))
                        break
                    if locations[(new_x, new_y)].color == self.color:
                        break
        # now, 'rook' moves
        for ii in [1, -1]:
            i = 1
            while 0 <= self.location[0] + i*ii < 8:
                new_x = self.location[0] + i*ii
                if not locations[(new_x, self.location[1])]:
                    valid_moves.append((new_x, self.location[1]))
                    i += 1
                    continue
                if locations[(new_x, self.location[1])].color != self.color:
                    valid_moves.append((new_x, self.location[1]))
                    i += 1
                    break
                if locations[(new_x, self.location[1])].color == self.color:
                    break

        for ii in [1, -1]:
            i = 1
            while 0 <= self.location[1] + i*ii < 8:
                new_y = self.location[1] + i*ii
                if not locations[(self.location[0], new_y)]:
                    valid_moves.append((self.location[0], new_y))
                    i += 1
                    continue
                if locations[(self.location[0], new_y)].color != self.color:
                    valid_moves.append((self.location[0], new_y))
                    i += 1
                    break
                if locations[(self.location[0], new_y)].color == self.color:
                    break
        return valid_moves


class Board:

    def __init__(self):
        self.board = np.empty((8, 8), dtype=object)

        for i in range(8):
            self.board[1][i] = Pawn('black', (1, i))
            self.board[6][i] = Pawn('white', (6, i))
        self.board[0][0] = Rook('black', (0, 0))
        self.board[0][7] = Rook('black', (0, 7))
        self.board[7][0] = Rook('white', (7, 0))
        self.board[7][7] = Rook('white', (7, 7))
        self.board[0][2] = Bishop('black', (0, 2))
        self.board[0][5] = Bishop('black', (0, 5))
        self.board[7][2] = Bishop('white', (7, 2))
        self.board[7][5] = Bishop('white', (7, 5))
        self.board[0][1] = Knight('black', (0, 1))
        self.board[0][6] = Knight('black', (0, 6))
        self.board[7][1] = Knight('white', (7, 1))
        self.board[7][6] = Knight('white', (7, 6))
        self.board[0][3] = Queen('black', (0, 3))
        self.board[7][3] = Queen('white', (7, 3))

        self.positions = dict()
        self.poll_board()

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

my_board.board[1][1].get_valid_moves()

# my_board.board[4][1] = Rook('white', (4, 1))
# my_board.board[4][1].get_valid_moves()

my_board.board[4][1] = Queen('white', (4, 1))
my_board.print()
my_board.board[4][1].get_valid_moves()