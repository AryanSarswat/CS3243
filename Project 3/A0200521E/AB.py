import sys
from copy import deepcopy
from random import choice, shuffle, seed
import math



### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove

PIECE_VALUES = {
    "King" : 25,
    "Queen" : 9,
    "Rook" : 5,
    "Bishop" : 3,
    "Knight" : 3,
    "Pawn" : 1
}

def convert_to_index(string):
    col = string[0]
    row = string[1:]
    return (int(row), ord(col) - ord('a'))

def convert_to_notation(coord):
    row = coord[0]
    col = coord[1]
    return (chr(col + ord('a')), row)

class Piece:
    def __init__(self, current_position, opponent = 1):
        self.current_position = current_position
        self.color = opponent
        self.symbol = ""
        
    def updatePosition(self, position):
        self.current_position = position
        
        
    def __repr__(self):
        if self.color == -1:
            return "\033[1;31;40m" + self.symbol + "\033[0m"
        elif self.color == 1:
            return "\033[1;37;40m" + self.symbol + "\033[0m"

class Knight(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "Knight"
        self.symbol = "N"
    
    def possibleMoves(self, board):
        possible_actions = []
        pos_moves = [(self.current_position[0] - 2, self.current_position[1] + 1), (self.current_position[0] - 2, self.current_position[1] - 1), (self.current_position[0] + 2, self.current_position[1] + 1), (self.current_position[0] + 2, self.current_position[1] - 1),
                (self.current_position[0] - 1, self.current_position[1] + 2), (self.current_position[0] - 1, self.current_position[1] - 2), (self.current_position[0] + 1, self.current_position[1] + 2), (self.current_position[0] + 1, self.current_position[1] - 2)]
        for move in pos_moves:
            if board.isValidPos(move) and (board.isEmpty(move) or board.isOpponentPiece(move)):
                possible_actions.append(move)
        return possible_actions
        
class Rook(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "Rook"
        self.symbol = "R"

    
    def possibleMoves(self, board):
        possible_actions = []
        for x in range(self.current_position[1] - 1, -1, -1):
            pos = (self.current_position[0], x)
            if board.isEmpty(pos):
                possible_actions.append((self.current_position[0], x))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append((self.current_position[0], x))
                break
        #Right actions
        for x in range(self.current_position[1] + 1, board.columns):
            pos = (self.current_position[0], x)
            if board.isEmpty(pos):
                possible_actions.append((self.current_position[0], x))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append((self.current_position[0], x))
                break
        #Up actions
        for y in range(self.current_position[0] - 1, -1, -1):
            pos = (y, self.current_position[1])
            if board.isEmpty(pos):
                possible_actions.append((y, self.current_position[1]))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append((y, self.current_position[1]))
                break
        #Down actions
        for y in range(self.current_position[0] + 1, board.rows):
            pos = (y, self.current_position[1])
            if board.isEmpty(pos):
                possible_actions.append((y, self.current_position[1]))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append((y, self.current_position[1]))
                break
            
        return possible_actions
    
class Bishop(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "Bishop"
        self.symbol = "B"
        
    def possibleMoves(self, board):
        possible_actions = []
        max_iter = max(board.rows, board.columns)
        #Down_Right actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] + i, self.current_position[1] + i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Up_left actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] - i, self.current_position[1] - i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Up_right actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] - i, self.current_position[1] + i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Down_left actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] + i, self.current_position[1] - i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        
        return possible_actions     
        
class Queen(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "Queen"
        self.symbol = "Q"
    
    def possibleMoves(self, board):
        possible_actions = []
        #Left actions
        for x in range(self.current_position[1] - 1, -1, -1):
            pos = (self.current_position[0], x)
            if board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Right actions
        for x in range(self.current_position[1] + 1, board.columns):
            pos = (self.current_position[0], x)
            if board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Up actions
        for y in range(self.current_position[0] - 1, -1, -1):
            pos = (y, self.current_position[1])
            if board.isEmpty(pos):
                possible_actions.append((y, self.current_position[1]))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Down actions
        for y in range(self.current_position[0] + 1, board.rows):
            pos = (y, self.current_position[1])
            if board.isEmpty(pos):
                possible_actions.append((y, self.current_position[1]))
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Diagonals
        max_iter = max(board.rows, board.columns)
        #Down_Right actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] + i, self.current_position[1] + i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Up_left actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] - i, self.current_position[1] - i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Up_right actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] - i, self.current_position[1] + i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        #Down_left actions
        for i in range(1, max_iter):
            pos = (self.current_position[0] + i, self.current_position[1] - i)
            if board.isValidPos(pos) and board.isEmpty(pos):
                possible_actions.append(pos)
            else:
                if board.isOpponentPiece(pos):
                    possible_actions.append(pos)
                break
        
        return possible_actions
      
class King(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "King"
        self.symbol = "K"
        self.isCheck = False
    
    def possibleMoves(self, board):
        possible_actions = []
        
        pos_moves = [(self.current_position[0] + 1, self.current_position[1]), (self.current_position[0] - 1, self.current_position[1]), (self.current_position[0], self.current_position[1] + 1), (self.current_position[0], self.current_position[1] - 1),
                        (self.current_position[0] + 1, self.current_position[1] + 1), (self.current_position[0] - 1, self.current_position[1] - 1), (self.current_position[0] + 1, self.current_position[1] - 1), (self.current_position[0] - 1, self.current_position[1] + 1)]
        for move in pos_moves:
            if board.isValidPos(move) and (board.isEmpty(move) or board.isOpponentPiece(move)):
                possible_actions.append(move)
        
        return possible_actions
    
class Pawn(Piece):
    def __init__(self, current_position, opponent=1):
        super().__init__(current_position, opponent)
        self.name = "Pawn"
        self.symbol = "P"
        
    def possibleMoves(self, board):
        possible_actions = []
        if self.color == 1:
            down = (self.current_position[0] + 1, self.current_position[1])
            down_right = (self.current_position[0] + 1, self.current_position[1] + 1)
            down_left = (self.current_position[0] + 1, self.current_position[1] - 1)
            
            #down
            if board.isValidPos(down) and board.isEmpty(down):
                possible_actions.append(down)
            #down_left
            if board.isValidPos(down_left) and board.isOpponentPiece(down_left):
                possible_actions.append(down_left)
            #down_right
            if board.isValidPos(down_right) and board.isOpponentPiece(down_right):
                possible_actions.append(down_right)
        else:
            up = (self.current_position[0] - 1, self.current_position[1])
            up_right = (self.current_position[0] - 1, self.current_position[1] + 1)
            up_left = (self.current_position[0] - 1, self.current_position[1] - 1)
            
            #up
            if board.isValidPos(up) and board.isEmpty(up):
                possible_actions.append(up)
            #up_left
            if board.isValidPos(up_left) and board.isOpponentPiece(up_left):
                possible_actions.append(up_left)
            #up_right
            if board.isValidPos(up_right) and board.isOpponentPiece(up_right):
                possible_actions.append(up_right)
                
        return possible_actions
             
class Board:
    def __init__(self, rows, columns, white_pieces, black_pieces):
        #Create Board
        self.rows = rows
        self.columns = columns
        # 1 for white pieces, -1 for black pieces
        self.turn = 1
        self.white_king = None
        self.black_king = None
        self.white_pieces = dict()
        self.black_pieces = dict()
        self.num_moves_made = 0
        self.value = 0
        
        for piece in white_pieces:
            pos = piece.current_position
            self.value += PIECE_VALUES[piece.name]
            self.white_pieces[pos] = piece
            if type(piece) == King:
                self.white_king = piece
        
        for piece in black_pieces:
            pos = piece.current_position
            self.value += PIECE_VALUES[piece.name]
            self.black_pieces[pos] = piece
            if type(piece) == King:
                self.black_king = piece
            
    def isEmpty(self, coord):
        if not self.isValidPos(coord):
            return False
        if coord not in self.black_pieces and coord not in self.white_pieces:
            return True
        return False
    
    def isValidPos(self , coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            return True
        return False
    
    def isPiece(self, coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            if coord in self.black_pieces or coord in self.white_pieces:
                return True
        return False
    
    def isOpponentPiece(self, coord):
        if not self.isValidPos(coord):
            return False
        if self.turn == 1:
            if self.isPiece(coord) and coord in self.black_pieces:
                return True
        elif self.turn == -1:
            if self.isPiece(coord) and coord in self.white_pieces:
                return True
        return False
    
    def possibleMoves(self):
        pos_moves = []
        if self.turn == 1:
            for piece in self.white_pieces.values():
                pieceMoves = piece.possibleMoves(self)
                if len(pieceMoves) != 0:
                    for move in pieceMoves:
                        pos_moves.append([piece.current_position, move])
        else:
            for piece in self.black_pieces.values():
                pieceMoves = piece.possibleMoves(self)
                if len(pieceMoves) != 0:
                    for move in pieceMoves:
                        pos_moves.append([piece.current_position, move])
        return pos_moves
    
    def makeMove(self, prev_pos, new_pos):
        newBoard = deepcopy(self)
        pieceToMove = None
        if self.turn == 1:
            pieceToMove = newBoard.white_pieces[prev_pos]
            newBoard.white_pieces[new_pos] = pieceToMove
            del newBoard.white_pieces[prev_pos]
            
        else:
            pieceToMove = newBoard.black_pieces[prev_pos]
            newBoard.black_pieces[new_pos] = pieceToMove
            del newBoard.black_pieces[prev_pos]
            
        
        pieceToMove.updatePosition(new_pos)
        
        
        if self.turn == 1 and new_pos in newBoard.black_pieces:
            pieceToRemove = newBoard.black_pieces[new_pos]
            newBoard.value += PIECE_VALUES[pieceToMove.name]
            del newBoard.black_pieces[new_pos]
            if pieceToRemove.name == "King":
                newBoard.black_king = None
        elif self.turn == -1 and new_pos in newBoard.white_pieces:
            pieceToRemove = newBoard.black_pieces[new_pos]
            newBoard.value -= PIECE_VALUES[pieceToMove.name]
            del newBoard.white_pieces[new_pos]
            if pieceToRemove.name == "King":
                newBoard.white_king = None

        newBoard.turn *= -1
        newBoard.num_moves_made += 1
        return newBoard
    
    def isTerminal(self):
        if self.white_king == None or self.black_king == None:
            return True
        
        if self.num_moves_made >= 50:
            return True
        
        if len(self.possibleMoves()) == 0:
            return True

        return False
    
    def __repr__(self):
        printGrid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for coord, piece in self.white_pieces.items():
            printGrid[coord[0]][coord[1]] = piece
        for coord, piece in self.black_pieces.items():
            printGrid[coord[0]][coord[1]] = piece
            
        for row in range(self.rows):
            printGrid[row] = [row] + printGrid[row]
            
        printGrid.append(['', 0, 1, 2, 3, 4])
            
        grid = '\n'.join(['\t'.join(['|' + str(cell) + '|' for cell in row]) for row in printGrid])
        
        grid += "\n \n"
        
        return grid 
    
def parse_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        
    rows = int(lines[0][5:-1])
    columns = int(lines[1][5:-1])
    
    
    #Get enemy pieces
    black_pieces = []
    index_black = 2
    requirements = sum(list(map(int,lines[index_black].split(":")[1][:-1].split())))
    start = index_black + 2
    for i in range(requirements):
        piece_name, piece_position = lines[start + i].split(",")
        piece_name = piece_name[1:]
        piece_position = piece_position[:-2]
        if piece_name == "King":
            black_pieces.append(King(convert_to_index(piece_position), opponent = -1))
        elif piece_name == "Queen":
            black_pieces.append(Queen(convert_to_index(piece_position), opponent = -1))
        elif piece_name == "Bishop":
            black_pieces.append(Bishop(convert_to_index(piece_position), opponent = -1))
        elif piece_name == "Rook":
            black_pieces.append(Rook(convert_to_index(piece_position), opponent = -1))
        elif piece_name == "Knight":
            black_pieces.append(Knight(convert_to_index(piece_position), opponent = -1))
        elif piece_name == "Pawn":
            black_pieces.append(Pawn(convert_to_index(piece_position), opponent = -1))   
    
    
    white_pieces = []
    index_white = 14
    requirements = sum(list(map(int,lines[index_white].split(":")[1][:-1].split())))
    start = index_white + 2
    for i in range(requirements):
        piece_name, piece_position = lines[start + i].split(",")
        piece_name = piece_name[1:]
        piece_position = piece_position[:-2]
        if piece_name == "King":
            white_pieces.append(King(convert_to_index(piece_position)))
        elif piece_name == "Queen":
            white_pieces.append(Queen(convert_to_index(piece_position)))
        elif piece_name == "Bishop":
            white_pieces.append(Bishop(convert_to_index(piece_position)))
        elif piece_name == "Rook":
            white_pieces.append(Rook(convert_to_index(piece_position)))
        elif piece_name == "Knight":
            white_pieces.append(Knight(convert_to_index(piece_position)))
        elif piece_name == "Pawn":
            white_pieces.append(Pawn(convert_to_index(piece_position)))    
            
    return rows, columns, black_pieces, white_pieces

def random_agent(board):
    p_moves = board.possibleMoves()
    prev_pos, new_pos = choice(p_moves)
    move = (prev_pos, new_pos)
    return move

def manual_agent(board):
    i, j = input("Enter piece and move: ").split()
    prev = i.split(",")
    next = j.split(",")
    return ((int(prev[0]), int(prev[1])), (int(next[0]), int(next[1])))
        
def heuristic(board):
    
    max_value = sum([PIECE_VALUES[piece.name] for piece in board.white_pieces.values()])
    min_value = sum([PIECE_VALUES[piece.name] for piece in board.black_pieces.values()])
    
    return max_value - min_value
        


#Implement your minimax with alpha-beta pruning algorithm here.
def ab(board):
    DEPTH = 2
    if board.turn == 1:
        value, move = max_value(DEPTH, board, -math.inf, math.inf)
    else:
        value , move = min_value(DEPTH, board, -math.inf, math.inf)
    return value, move
    
def max_value(depth, board, alpha, beta):
    if board.isTerminal() or depth == 0:
        return heuristic(board), None
    
    v = -math.inf
    best_move = None
    pos_moves = board.possibleMoves()
    shuffle(pos_moves)
    for moves in pos_moves:
        v2, a2 = min_value(depth - 1, board.makeMove(moves[0], moves[1]), alpha, beta)
        if v2 > v:
            v , best_move = v2, (moves[0], moves[1])
            alpha = max(alpha, v)
        if v >= beta:
            return v, best_move
    return v, best_move

def min_value(depth, board, alpha ,beta):
    if board.isTerminal() or depth == 0:
        return heuristic(board), None
    
    v = math.inf
    best_move = None
    pos_moves = board.possibleMoves()
    shuffle(pos_moves)
    for moves in pos_moves:
        v2, a2 = max_value(depth - 1, board.makeMove(moves[0], moves[1]), alpha, beta)
        if v2 < v:
            v , best_move = v2, (moves[0], moves[1])
            beta = min(beta, v)
        if v <= alpha:
            return v, best_move
    return v, best_move



### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    #config = sys.argv[1] #Takes in config.txt Optional
    seed(6)
    
    rows = 5
    columns = 5
    whitepieces = []
    blackpieces = []
    
    for pos, piece in gameboard.items():
        if piece[0] == "King":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(King(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(King(convert_to_index(temp), opponent = -1))
        elif piece[0] == "Queen":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(Queen(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(Queen(convert_to_index(temp), opponent= -1))
        elif piece[0] == "Bishop":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(Bishop(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(Bishop(convert_to_index(temp), opponent= -1))
        elif piece[0] == "Rook":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(Rook(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(Rook(convert_to_index(temp), opponent= -1))
        elif piece[0] == "Knight":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(Knight(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(Knight(convert_to_index(temp), opponent= -1))
        elif piece[0] == "Pawn":
            if piece[1] == "White":
                temp = pos[0] + str(pos[1])
                whitepieces.append(Pawn(convert_to_index(temp)))
            else:
                temp = pos[0] + str(pos[1])
                blackpieces.append(Pawn(convert_to_index(temp), opponent= -1))
        
    board = Board(rows, columns, whitepieces, blackpieces)
    
    value, move = ab(board)
    
    move = [convert_to_notation(move[0]), convert_to_notation(move[1])]
    
    return move #Format to be returned (('a', 0), ('b', 3))

# import time
# def instantiate_board():
#     config = sys.argv[1]
#     rows, columns, black_pieces, white_pieces = parse_input(config)
#     board = Board(rows, columns, white_pieces, black_pieces)
    
#     print(board)
    
#     while not board.isTerminal():
#         if board.turn == 1:
#             start = time.time()
#             value , move = ab(board)
#             end = time.time()
#             print(f"Minimax move (Time taken {end - start}")
#         else:

#             print("Opponent Move")
#             move = manual_agent(board)
        
#         board = board.makeMove(move[0], move[1])
#         print(move)
#         print(board)

# if __name__ == '__main__':
#     instantiate_board()


# if __name__ == '__main__':
#     gameboard = {
#         ('a', 0) : ('Queen','White'
# ), 
#         ('a', 1) : ('King','White'),
#         ('b', 4) : ('Rook','White'),
#         ('d', 2) : ('Knight','Black'), 
#         ('c', 3) : ("King", "Black"),
#         ('c', 2) : ("Pawn", "Black")
#     }
#     print(studentAgent(gameboard))