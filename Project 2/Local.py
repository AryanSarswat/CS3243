# Helper functions to aid in your implementation. Can edit/remove
# Helper functions to aid in your implementation. Can edit/remove
import random
from sys import argv

class Piece:
    
    def __init__(self, piece_name, current_position, opponent = True):
        self.name = piece_name
        self.current_position = current_position
        self.opponent = opponent
        
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
    
    def __hash__(self):
        return hash(self.current_position)*2 + hash(self.name)*4

    @staticmethod
    def possibleAttacks(board, piece_name, current_position):
        """
        Returns a list of possible actions for the piece.
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
            return "\033[1;35;40m" + self.symbol + "\033[0m"
        else:
            return "\033[1;34;40m" + self.symbol + "\033[0m"
        
    def __hash__(self):
        return hash(self.symbol + self.current_position.__str__())

class Obstacle:
    def __init__(self, current_position):
        self.current_position = current_position
    
    def __repr__(self):
        return "\033[1;33;40mX\033[0m"
       
class Board:
    def __init__(self, rows, columns, obstacles_locations, pieces):
        #Create Board
        self.rows = rows
        self.columns = columns
        
        self.grid = [['0' for _ in range(columns)] for _ in range(rows)]
        
        #Mark obstacles
        for loc in obstacles_locations:
            self.grid[loc[0]][loc[1]] = Obstacle(loc)
            
        #Mark pieces and the squares they attack
        for piece in pieces:
            #Occupy position by enemy piece
            self.grid[piece.current_position[0]][piece.current_position[1]] = piece
        self.pieces = pieces
    
    def addPiece(self, piece):
        self.grid[piece.current_position[0]][piece.current_position[1]] = piece
        self.pieces.append(piece)
        
    def removePiece(self, piece):
        coord = piece.current_position
        self.grid[coord[0]][coord[1]] = '0'
        self.pieces.remove(piece)
    
    def heuristic(self):
        attacked = 0
        for piece in self.pieces:
            attacked += Piece.possibleAttacks(self, piece.name, piece.current_position)
        return attacked
    
    def isEmpty(self, coord):
        if self.grid[coord[0]][coord[1]] == '0':
            return True
        return False
    
    def isPiece(self, coord):
        if 0 <= coord[0] < self.rows and 0 <= coord[1] < self.columns:
            if type(self.grid[coord[0]][coord[1]]) == Piece:
                return True
        return False
    
    def isGoal(self):
        for piece in self.pieces:
            if Piece.possibleAttacks(self, piece.name, piece.current_position) > 0:
                return False
        return True

    def numPieces(self):
        return len(self.pieces)
    
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
    #Get cost to move to selected grids
    K = int(lines[4][42:-1])
    
    #Get enemy pieces
    index = 5
    pieces = []
    num_pieces = sum(map(int,lines[index].split(":")[1][:-1].split()))
    start =  index + 2
    for i in range(num_pieces):
        index = start + i
        piece_name, curr_pos = lines[index].split(",")
        pieces.append(Piece(piece_name[1:], convert_to_index(curr_pos[:-2])))
    
    return rows, columns, obstacle_locations, pieces, K

def search(rows, columns, obstacle_locations, pieces, K):
    goal_state = None
    subset = random.sample(pieces, k = K)
    board = Board(rows, columns, obstacle_locations, subset)
        

    while goal_state == None:
        if board.isGoal():
            goal_state = board
        else:
            pieces_left = [piece for piece in pieces if piece not in board.pieces]
            curr_eval = board.heuristic()
            piece2Remove = None
            piece2Add = None
            for pieceToRemove in board.pieces:
                stopCond = False
                board.removePiece(pieceToRemove)
                for pieceToAdd in pieces_left:
                    board.addPiece(pieceToAdd)
                    new_eval = board.heuristic()
                    if new_eval <= curr_eval:
                        piece2Remove = pieceToRemove
                        piece2Add = pieceToAdd
                        curr_eval = new_eval
                        if new_eval == 0:
                            goal_state = board
                            stopCond = True
                            break
                    board.removePiece(pieceToAdd)
                board.addPiece(pieceToRemove)
                if stopCond:
                    break
            
            if piece2Remove != None:
                board.removePiece(piece2Remove)
                board.addPiece(piece2Add)
                
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
def run_local():
    # You can code in here but you cannot remove this function or change the return type
    testfile = argv[1] #Do not remove. This is your input testfile.
    rows, columns, obstacle_locations, pieces, K = parse_input(testfile)
    
    goalState = search(rows, columns, obstacle_locations, pieces, K)
    return goalState #Format to be returned

# if __name__ == '__main__':
#     print(run_local())
    