import sys

### IMPORTANT: Remove any print() functions or rename any print functions/variables/string when submitting on CodePost
### The autograder will not run if it detects any print function.

# Helper functions to aid in your implementation. Can edit/remove
from sys import argv
import random


class Piece:
    def __init__(self, piece_name, current_position, opponent = True):
        self.name = piece_name
        self.current_position = current_position
        self.opponent = opponent
        self.attack = dict()
        
        if self.name == "King":
            self.symbol = "K"
        elif self.name == "Queen":
            self.symbol = "Q"
        elif self.name == "Rook":
            self.symbol = "R"
        elif self.name == "Bishop":
            self.symbol = "B"
        elif self.name == "Knight":
            self.symbol = "N"

    @staticmethod
    def possibleAttacks(board, piece_name, current_position):
        """
        Returns a list of possible actions for the piece.
        """
        possible_actions = []
        
        if piece_name == "King":
            pos_moves = [(current_position[0] + 1, current_position[1]), (current_position[0] - 1, current_position[1]), (current_position[0], current_position[1] + 1), (current_position[0], current_position[1] - 1),
                         (current_position[0] + 1, current_position[1] + 1), (current_position[0] - 1, current_position[1] - 1), (current_position[0] + 1, current_position[1] - 1), (current_position[0] - 1, current_position[1] + 1)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and (board.isEmpty(move) or board.isPiece(move)):
                    possible_actions.append(move)
            
        elif piece_name == "Queen":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Diagonals
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break 
        elif piece_name == "Rook":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    if board.isPiece(pos):
                        possible_actions.append((current_position[0], x))
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    if board.isPiece(pos):
                        possible_actions.append((current_position[0], x))
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    if board.isPiece(pos):
                        possible_actions.append((y, current_position[1]))
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    if board.isPiece(pos):
                        possible_actions.append((y, current_position[1]))
                    break
        elif piece_name == "Bishop":
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isEmpty(pos):
                    possible_actions.append(pos)
                else:
                    if board.isPiece(pos):
                        possible_actions.append(pos)
                    break            
        elif piece_name == "Knight":
            pos_moves = [(current_position[0] - 2, current_position[1] + 1), (current_position[0] - 2, current_position[1] - 1), (current_position[0] + 2, current_position[1] + 1), (current_position[0] + 2, current_position[1] - 1),
                         (current_position[0] - 1, current_position[1] + 2), (current_position[0] - 1, current_position[1] - 2), (current_position[0] + 1, current_position[1] + 2), (current_position[0] + 1, current_position[1] - 2)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and (board.isEmpty(move) or board.isPiece(move)):
                    possible_actions.append(move)
        else:
            pass
        return possible_actions
    
    
    @staticmethod
    def attackedPieces(board, piece_name, current_position):
        """
        Returns the number of attacked pieces.
        """
        num_attacked_pieces = 0
        
        if piece_name == "King":
            pos_moves = [(current_position[0] + 1, current_position[1]), (current_position[0] - 1, current_position[1]), (current_position[0], current_position[1] + 1), (current_position[0], current_position[1] - 1),
                         (current_position[0] + 1, current_position[1] + 1), (current_position[0] - 1, current_position[1] - 1), (current_position[0] + 1, current_position[1] - 1), (current_position[0] - 1, current_position[1] + 1)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isEmpty(move):
                    continue
                else:
                    if board.isPiece(move):
                        num_attacked_pieces += 1        
        elif piece_name == "Queen":
            #Diagonals
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break     
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
 
        elif piece_name == "Rook":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
        elif piece_name == "Bishop":
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isEmpty(pos):
                    continue
                else:
                    if board.isPiece(pos):
                        num_attacked_pieces += 1
                        continue
                    break                
        elif piece_name == "Knight":
            pos_moves = [(current_position[0] - 2, current_position[1] + 1), (current_position[0] - 2, current_position[1] - 1), (current_position[0] + 2, current_position[1] + 1), (current_position[0] + 2, current_position[1] - 1),
                         (current_position[0] - 1, current_position[1] + 2), (current_position[0] - 1, current_position[1] - 2), (current_position[0] + 1, current_position[1] + 2), (current_position[0] + 1, current_position[1] - 2)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isEmpty(move):
                    continue
                else:
                    if board.isPiece(move):
                        num_attacked_pieces += 1
        return num_attacked_pieces
    
    def __repr__(self):
        if self.opponent:
            return self.symbol
            return "\033[1;35;40m" + self.symbol + "\033[0m"
        else:
            return "\033[1;34;40m" + self.symbol + "\033[0m"
    

class Obstacle:
    def __init__(self, current_position):
        self.current_position = current_position
    
    def __repr__(self):
        return "O"
        return "\033[1;33;40mX\033[0m"
    
class AttackedPosition:
    def __init__(self, current_position):
        self.current_position = current_position
        self.num = 1
    
    def __repr__(self):
        return "A"
        return "\033[1;31;40mA\033[0m"
       
class Board:
    def __init__(self, rows, columns, obstacles_locations, pieces):
        #Create Board
        self.rows = rows
        self.columns = columns
        
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]
        
        #Mark obstacles
        for loc in obstacles_locations:
            self.grid[loc[0]][loc[1]] = Obstacle(loc)
            
        #Mark pieces and the squares they attack
        self.pieces = set(pieces)

    def isEmpty(self, coord):
        if self.grid[coord[0]][coord[1]] == 0 or type(self.grid[coord[0]][coord[1]]) == AttackedPosition:
            return True
        return False
    
    def isPiece(self, coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            if type(self.grid[coord[0]][coord[1]]) == Piece:
                return True
        return False
    
    def isGoal(self, numPieces):
        ans = False
        if len(self.pieces) == numPieces:
            for piece in self.pieces:
                numattackedpieces = Piece.attackedPieces(self, piece.name, piece.current_position)
                if numattackedpieces != 0:
                    return False
            ans = True
        return ans
    
    def addPiece(self, piece, position):
        if self.grid[position[0]][position[1]] != 0:
            pass
        else:
            piece.current_position = position
            self.grid[position[0]][position[1]] = piece
            self.pieces.add(piece)
            
            attackedPositions = piece.attack[position]
            for attack in attackedPositions:
                check = self.grid[attack[0]][attack[1]]
                if type(check) == AttackedPosition:
                    self.grid[attack[0]][attack[1]].num += 1
                elif check == 0:
                    self.grid[attack[0]][attack[1]] = AttackedPosition(attack)
            
    def removePiece(self, piece, position):
        if self.grid[position[0]][position[1]] != piece:
            pass
        else:
            self.pieces.remove(piece)
            piece.current_position = None
            self.grid[position[0]][position[1]] = 0
            
            attackedPositions = piece.attack[position]
            for attack in attackedPositions:
                if type(self.grid[attack[0]][attack[1]]) == AttackedPosition:
                    check = self.grid[attack[0]][attack[1]].num
                    if check == 1:
                        self.grid[attack[0]][attack[1]] = 0
                    else:
                        self.grid[attack[0]][attack[1]].num -= 1
                    
    def validPlacements(self):
        empty = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.grid[i][j] == 0:
                    empty.append((i, j))
        return empty
    
    def infer(self, pos, piece):
        if pos in piece.attack:
            attacks = piece.attack[pos]
        else:
            attacks = Piece.possibleAttacks(self, piece.name, pos)
        add = True
        piece.attack[pos] = attacks
        for attack in attacks:
            if self.isPiece(attack):
                add = False
                break
        return add
    
    def __repr__(self):
        grid = '\n'.join(['\t'.join(['|' + str(cell) + '|' for cell in row]) for row in self.grid])
        
        grid += "\n \n"
        
        return grid

def convert_to_index(string):
    col = string[0]
    row = string[1:]
    return (int(row), ord(col) - ord('a'))

def convert_to_notation(coord):
    row = coord[0]
    col = coord[1]
    return (chr(col + ord('a')), row)

def parse_input(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        
    rows = int(lines[0][5:-1])
    columns = int(lines[1][5:-1])
    
    #Get obstacle locations
    num_obstacles = int(lines[2][20:])
    if num_obstacles > 0:
        obstacle_locations = list(map(convert_to_index,lines[3].split(":")[1][:-1].split(" ")))
    else:
        obstacle_locations = []
    
    #Get enemy pieces
    index = 4
    requirements = list(map(int,lines[index].split(":")[1][:-1].split()))
    numKings = requirements[0]
    numQueens = requirements[1]
    numBishops = requirements[2]
    numRook = requirements[3]
    numKnights = requirements[4]
    
    return rows, columns, obstacle_locations, numKings, numQueens, numBishops, numRook, numKnights

def backtrack(board, constraints, numPieces):
    if board.isGoal(numPieces):
        return board
    elif len(constraints) == 0:
        return None
    
    piece = constraints[0]
    
    validPlacements = board.validPlacements()
    
    if len(validPlacements) < len(constraints):
        return None
    else:
        random.shuffle(validPlacements)
    
    for position in validPlacements:
        if board.infer(position, piece):
            board.addPiece(piece, position)
            
            goal = backtrack(board, constraints[1:], numPieces)
            
            if goal != None:
                return goal
            else:
                board.removePiece(piece, position)
        
    
    return None


def search(rows, columns, obstacle_locations, numKings, numQueens, numBishops, numRook, numKnights):
    random.seed(1)
    board = Board(rows, columns, obstacle_locations, [])
    constraints = []
    #Create pieces
    for _ in range(numQueens):
        constraints.append(Piece("Queen", None))
    
    for _ in range(numRook):
        constraints.append(Piece("Rook", None))
    
    for _ in range(numBishops):
        constraints.append(Piece("Bishop", None))
    
    for _ in range(numKnights):
        constraints.append(Piece("Knight", None))
    
    for _ in range(numKings):
        constraints.append(Piece("King", None))   

    
    goal_state = backtrack(board, constraints, numQueens + numRook + numBishops + numKnights + numKings)

    ret = dict()


    for piece in goal_state.pieces:
        coord = piece.current_position
        coord = convert_to_notation(coord)
        ret[coord] = piece.name

    return ret


### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: Goal State which is a dictionary containing a mapping of the position of the grid to the chess piece type.
# Chess Pieces: King, Queen, Knight, Bishop, Rook (First letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Goal State to return example: {('a', 0) : Queen, ('d', 10) : Knight, ('g', 25) : Rook}
def run_CSP():
    # You can code in here but you cannot remove this function or change the return type
    testfile = sys.argv[1] #Do not remove. This is your input testfile.
    rows, columns, obstacle_locations, numKings, numQueens, numBishops, numRook, numKnights = parse_input(testfile)
    
    goalState = search(rows, columns, obstacle_locations, numKings, numQueens, numBishops, numRook, numKnights)
    return goalState #Format to be returned

from time import time

if __name__ == '__main__':
    start = time()
    run_CSP()
    end = time()
    print("Time taken: ", end - start)