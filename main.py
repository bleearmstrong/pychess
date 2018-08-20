import numpy as np
import uuid


class Piece:

    def __init__(self, piece, color, location):
        self.piece = piece
        self.color = color
        self.location = location
        self.multiplier = 1 if color == 'white' else -1
        self.id = str(uuid.uuid4())
        self.move_count = 0


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
        if self.move_count == 0:
            possible_positions.append((self.location[0] - (2 * self.multiplier), self.location[1]))
        valid_moves_0 = []
        for position in possible_positions:
            if not (position[0] < 0 or position[0] > 7 or position[1] < 0 or position[1] > 7):
                valid_moves_0.append(position)
        locations = my_board.positions.copy() # get positions of all pieces
        relevant_squares = {key: locations[key] for key in valid_moves_0} # filter above list to only look at squares this pawn can move to
        valid_moves_1 = []
        # print('relevant squares = {}'.format(relevant_squares))
        for square in relevant_squares: # for each square this pawn can move to...
            if relevant_squares[square] and relevant_squares[square].location[1] != self.location[1] and relevant_squares[square].color != self.color:
                valid_moves_1.append(square)
            if square[1] == self.location[1] and not relevant_squares[square]:
                valid_moves_1.append(square)
        #     if not relevant_squares[square] or relevant_squares[square].color != self.color: # if it's empty OR the piece is a different color, it passes the first test
        #         valid_moves_1.append(square)
        # if relevant_squares[(self.location[0] - (1 * self.multiplier), self.location[1])] is not None and relevant_squares[(self.location[0] - (1 * self.multiplier), self.location[1])].color != self.color:
        #     valid_moves_1.append((self.location[0] - (1 * self.multiplier), self.location[1]))
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


class King(Piece):

    def __init__(self, color, location):
        Piece.__init__(self, 'King', color, location)

    def get_valid_moves(self):
        # will borrow the code for rook + bishop
        locations = my_board.positions.copy()
        valid_moves = []
        for ii in [-1, 0, 1]:
            for jj in [-1, 0, 1]:
                if (ii, jj) != (0, 0):
                    new_x = self.location[0] + ii
                    new_y = self.location[1] + jj
                    if 0 <= new_x < 8 and 0 <= new_y < 8 and (locations[(new_x, new_y)] is None or locations[(new_x, new_y)].color != self.color):
                        valid_moves.append((new_x, new_y))
        return valid_moves


class Board:

    def __init__(self):
        self.board = np.empty((8, 8), dtype=object)
        self.game_status = 'active'
        self.points = {'p': 1
                       , 'k': 3
                       , 'b': 3
                       , 'r': 5
                       , 'Q': 9
                       , 'K': 1000}

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
        self.board[0][4] = King('black', (0, 4))
        self.board[7][4] = King('white', (7, 4))

        self.positions = dict()
        self.poll_board()

    def poll_board(self):
        for i in range(8):
            for j in range(8):
                self.positions[(i, j)] = self.board[i][j]
        x = 1

    def print(self):
        print('     a  b  c  d  e  f  g  h')
        print('     0  1  2  3  4  5  6  7')
        for i, row in enumerate(self.board):
            print_row = str(i) + ': |' + '|'.join([item.__repr__() if item is not None else '  ' for item in row]) + '|'
            print(print_row)

    def play(self):
        counter = 0
        while counter < 5:
            self.turn('white')
            # self.check()
            self.turn('black')
            # self.check()
            counter += 1
            print(counter)

    def get_value(self, key):
        destination = self.positions[key]
        if destination:
            return self.points[str(destination)[0]]
        else:
            return 0

    def max_points(self, group):
        return group[1]

    def get_available_moves(self, color):
        self.poll_board()
        pieces_in_play = {key: self.positions[key] for key in self.positions if
                          self.positions[key] and self.positions[key].color == color}
        available_moves = {}
        for piece in pieces_in_play:
            pieces_moves = my_board.board[piece].get_valid_moves()
            available_moves[(str(my_board.board[piece]), my_board.board[piece].id)] = pieces_moves
        # print(available_moves)
        flattened_list = []
        for i, piece in enumerate(available_moves):
            for move in available_moves[piece]:
                flattened_list.append(((piece, move), self.get_value(move)))
        # print('flattened_list = {}'.format(flattened_list))
        return flattened_list

    def make_move(self, move, color):
        print('{} making move'.format(color))
        # print('move[0][0][1] = {}'.format(move[0][0][1]))
        # print('move[0][1] = {}'.format(move[0][1]))
        # print('move[1] = {}'.format(move[1]))
        original_location = self.find_piece(move[0][0][1])
        print('original_location {}'.format(original_location))
        print('new location {}'.format(move[0][1]))
        self.board[move[0][1]] = self.board[original_location]
        self.board[original_location] = None
        self.board[move[0][1]].location = move[0][1]
        self.board[move[0][1]].move_count += 1
        self.poll_board()

    def find_piece(self, id):
        for index, i in np.ndenumerate(self.board):
            if self.board[index] and self.board[index].id == id:
                return index

    def rebuild_board(self, positions_copy):
        for key in positions_copy:
            self.board[key] = positions_copy[key]
            self.board[key].location = key
            self.board[key] -= 1

    def find_king(self, color):
        for index, i in np.ndenumerate(self.board):
            if self.board[index] and str(self.board[index])[0] + color[0] == 'K' + color[0]:
                return index

    def move_safe(self, color):
        opp_color = 'black' if color == 'white' else 'white'
        opp_available_moves = [x[0][1] for x in self.get_available_moves(opp_color)]
        king = self.find_king(color)
        return king not in opp_available_moves

    def turn(self, color):
        available_moves = self.get_available_moves(color)
        selected_move = False
        while not selected_move:
            this_move = max(available_moves, key=self.max_points)
            # print('max points: {} '.format(this_move))
            # now we need to make sure the move is legal (at the moment, just to make sure we're not putting the king in check)
            positions_copy = self.positions.copy()
            self.make_move(this_move, color)
            self.print()
            selected_move = self.move_safe(color)
            if not selected_move:
                available_moves.remove(this_move)
                self.rebuild_board(positions_copy)
            if len(available_moves) == 0:
                self.game_status = 'Stalemate'






my_board = Board()
my_board.print()
my_board.play()
# my_board.print()
# my_board.positions
# my_board.board[1][1].get_valid_moves()
#
# # my_board.board[4][1] = Rook('white', (4, 1))
# # my_board.board[4][1].get_valid_moves()
#
# my_board.board[(5, 2)] = Knight('white', (5, 2))
# my_board.print()
# my_board.board[(5, 2)].get_valid_moves()
# my_board.board[(1, 2)]
#
# my_board.board[(1, 1)].id
#
# def find_piece(id):
#     for index, i in np.ndenumerate(my_board.board):
#         if my_board.board[index] and my_board.board[index].id == id:
#             return index
# id = 'bc389ad0-c4bd-4a90-abc6-6f2983c89c74'
# find_piece(id)
# blah = my_board.positions[(6, 5)]