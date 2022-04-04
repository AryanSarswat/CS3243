import nntplib
import sys
from copy import deepcopy
from random import choice
import math
import time


### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove

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
        self.attack = dict()
        
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
        self.white_pieces = white_pieces
        self.black_pieces = black_pieces
        self.num_moves_made = 0
        
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]
        
        for piece in white_pieces:
            self.grid[piece.current_position[0]][piece.current_position[1]] = piece
            if type(piece) == King:
                self.white_king = piece
        
        for piece in black_pieces:
            self.grid[piece.current_position[0]][piece.current_position[1]] = piece
            if type(piece) == King:
                self.black_king = piece
            
    def isEmpty(self, coord):
        if self.grid[coord[0]][coord[1]] == 0:
            return True
        return False
    
    def isValidPos(self , coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            return True
        return False
    
    def isPiece(self, coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            if type(self.grid[coord[0]][coord[1]]) in [King, Queen, Rook, Bishop, Knight, Pawn]:
                return True
        return False
    
    def isOpponentPiece(self, coord):
        if not self.isValidPos(coord):
            return False
        if self.turn == 1:
            if self.isPiece(coord) and self.grid[coord[0]][coord[1]] in self.black_pieces:
                return True
        elif self.turn == -1:
            if self.isPiece(coord) and self.grid[coord[0]][coord[1]] in self.white_pieces:
                return True
        return False
    
    def possibleMoves(self):
        pos_moves = []
        if self.turn == 1:
            for piece in self.white_pieces:
                pieceMoves = piece.possibleMoves(self)
                if len(pieceMoves) != 0:
                    pos_moves.append([piece, piece.possibleMoves(self)])
        else:
            for piece in self.black_pieces:
                pieceMoves = piece.possibleMoves(self)
                if len(pieceMoves) != 0:
                    pos_moves.append([piece, piece.possibleMoves(self)])
                
        return pos_moves
    
    def makeMove(self, piece, move):
        newBoard = deepcopy(self)
        pieceToMove = newBoard.grid[piece.current_position[0]][piece.current_position[1]]
        newBoard.grid[piece.current_position[0]][piece.current_position[1]] = 0
        pieceToMove.updatePosition(move)
        
        
        if newBoard.grid[move[0]][move[1]] != 0:
            if newBoard.grid[move[0]][move[1]].color == -1:
                newBoard.black_pieces.remove(newBoard.grid[move[0]][move[1]])
                newBoard.num_moves_made = 0
            else:
                newBoard.white_pieces.remove(newBoard.grid[move[0]][move[1]])
                newBoard.num_moves_made = 0
                
                
        newBoard.grid[move[0]][move[1]] = pieceToMove
        newBoard.turn *= -1
        newBoard.num_moves_made += 1
        return newBoard
    
    def isTerminal(self):
        if self.white_king not in self.white_pieces or self.black_king not in self.black_pieces:
            return True
        
        if self.num_moves_made >= 50:
            return True
        
        if len(self.possibleMoves()) == 0:
            return True

        return False
    
    def __repr__(self):
        grid = '\n'.join(['\t'.join(['|' + str(cell) + '|' for cell in row]) for row in self.grid])
        
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

def instantiate_board():
    config = sys.argv[1]
    rows, columns, black_pieces, white_pieces = parse_input(config)
    board = Board(rows, columns, white_pieces, black_pieces)
    
    print(board)
    
    while not board.isTerminal():
        if board.turn == 1:
            start = time.time()
            value , move = ab(board)
            end = time.time()
            print(f"Minimax move (Time taken {end - start}")
        else:
            print("Opponent Move")
            move = manual_agent(board)
        
        board = board.makeMove(move[0], move[1])
        print(move)
        print(board)

def random_agent(board):
    p_moves = board.possibleMoves()
    piece , moves = choice(p_moves)
    move = (piece, choice(moves))
    return move

def manual_agent(board):
    p_moves = board.possibleMoves()
    print(p_moves)
    i, j = input("Enter piece and move: ").split()
    return (p_moves[int(i)][0], p_moves[int(i)][1][int(j)])
        
def heuristic(board):
    PIECE_VALUES = {
        "King" : 100,
        "Queen" : 9,
        "Rook" : 5,
        "Bishop" : 3,
        "Knight" : 3,
        "Pawn" : 1
    }
    
    score = sum([PIECE_VALUES[piece.name] for piece in board.white_pieces]) - sum([PIECE_VALUES[piece.name] for piece in board.black_pieces])
    
    return score
        


#Implement your minimax with alpha-beta pruning algorithm here.
def ab(board):
    DEPTH = 4
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
    for piece_move in pos_moves:
        for move in piece_move[1]:
            v2, a2 = min_value(depth - 1, board.makeMove(piece_move[0], move), alpha, beta)
            if v2 > v:
                v , best_move = v2, [piece_move[0], move]
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
    for piece_move in pos_moves:
        for move in piece_move[1]:
            v2, a2 = max_value(depth - 1, board.makeMove(piece_move[0], move), alpha, beta)
            if v2 < v:
                v , best_move = v2, [piece_move[0], move]
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
    config = sys.argv[1] #Takes in config.txt Optional

    rows = 5
    columns = 5
    whitepieces = []
    blackpieces = []
    
    for pos, piece in gameboard.items():
        if piece[0] == "King":
            if piece[1] == "White":
                whitepieces.append(King(pos))
            else:
                blackpieces.append(King(pos))
        elif piece[0] == "Queen":
            if piece[1] == "White":
                whitepieces.append(Queen(pos))
            else:
                blackpieces.append(Queen(pos))
        elif piece[0] == "Bishop":
            if piece[1] == "White":
                whitepieces.append(Bishop(pos))
            else:
                blackpieces.append(Bishop(pos))
        elif piece[0] == "Rook":
            if piece[1] == "White":
                whitepieces.append(Rook(pos))
            else:
                blackpieces.append(Rook(pos))
        elif piece[0] == "Knight":
            if piece[1] == "White":
                whitepieces.append(Knight(pos))
            else:
                blackpieces.append(Knight(pos))
        elif piece[0] == "Pawn":
            if piece[1] == "White":
                whitepieces.append(Pawn(pos))
            else:
                blackpieces.append(Pawn(pos))
        
    board = Board(rows, columns, whitepieces, blackpieces)
    
    move = ab(board)
    return move #Format to be returned (('a', 0), ('b', 3))


if __name__ == '__main__':
    instantiate_board()