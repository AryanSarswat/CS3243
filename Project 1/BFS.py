# Helper functions to aid in your implementation. Can edit/remove
from sys import argv
from timeit import timeit

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
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isAttackable(move):
                    possible_actions.append(move)
            
        elif piece_name == "Queen":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isAttackable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isAttackable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Diagonals
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break      
        elif piece_name == "Rook":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isAttackable(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isAttackable(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isAttackable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isAttackable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
        elif piece_name == "Bishop":
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isAttackable(pos):
                    possible_actions.append(pos)
                else:
                    break                
        elif piece_name == "Knight":
            pos_moves = [(current_position[0] - 2, current_position[1] + 1), (current_position[0] - 2, current_position[1] - 1), (current_position[0] + 2, current_position[1] + 1), (current_position[0] + 2, current_position[1] - 1),
                         (current_position[0] - 1, current_position[1] + 2), (current_position[0] - 1, current_position[1] - 2), (current_position[0] + 1, current_position[1] + 2), (current_position[0] + 1, current_position[1] - 2)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isAttackable(move):
                    possible_actions.append(move)
        else:
            raise Exception("Invalid piece name")
        return possible_actions
    
    
    @staticmethod
    def possibleMoves(board, piece_name, current_position):
        """
        Returns a list of possible actions for the piece.
        """
        possible_actions = []
        
        if piece_name == "King":
            pos_moves = [(current_position[0] + 1, current_position[1]), (current_position[0] - 1, current_position[1]), (current_position[0], current_position[1] + 1), (current_position[0], current_position[1] - 1),
                         (current_position[0] + 1, current_position[1] + 1), (current_position[0] - 1, current_position[1] - 1), (current_position[0] + 1, current_position[1] - 1), (current_position[0] - 1, current_position[1] + 1)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isMovable(move):
                    possible_actions.append(move)
            
        elif piece_name == "Queen":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isMovable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isMovable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Diagonals
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break      
        elif piece_name == "Rook":
            #Left actions
            for x in range(current_position[1] - 1, -1, -1):
                pos = (current_position[0], x)
                if board.isMovable(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    break
            #Right actions
            for x in range(current_position[1] + 1, board.columns):
                pos = (current_position[0], x)
                if board.isMovable(pos):
                    possible_actions.append((current_position[0], x))
                else:
                    break
            #Up actions
            for y in range(current_position[0] - 1, -1, -1):
                pos = (y, current_position[1])
                if board.isMovable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
            #Down actions
            for y in range(current_position[0] + 1, board.rows):
                pos = (y, current_position[1])
                if board.isMovable(pos):
                    possible_actions.append((y, current_position[1]))
                else:
                    break
        elif piece_name == "Bishop":
            max_iter = max(board.rows, board.columns)
            #Down_Right actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] + i)
                if pos[0] < board.rows and pos[1] < board.columns and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] - i)
                if pos[0] >= 0 and pos[1] >= 0 and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Up_right actions
            for i in range(1, max_iter):
                pos = (current_position[0] - i, current_position[1] + i)
                if pos[0] >= 0 and pos[1] < board.columns and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break
            #Down_left actions
            for i in range(1, max_iter):
                pos = (current_position[0] + i, current_position[1] - i)
                if pos[0] < board.rows and pos[1] >= 0 and board.isMovable(pos):
                    possible_actions.append(pos)
                else:
                    break                
        elif piece_name == "Knight":
            pos_moves = [(current_position[0] - 2, current_position[1] + 1), (current_position[0] - 2, current_position[1] - 1), (current_position[0] + 2, current_position[1] + 1), (current_position[0] + 2, current_position[1] - 1),
                         (current_position[0] - 1, current_position[1] + 2), (current_position[0] - 1, current_position[1] - 2), (current_position[0] + 1, current_position[1] + 2), (current_position[0] + 1, current_position[1] - 2)]
            for move in pos_moves:
                if 0 <= move[0] < board.rows and 0 <= move[1] < board.columns and board.isMovable(move):
                    possible_actions.append(move)
        else:
            raise Exception("Invalid piece name")
        return possible_actions
    
    def __repr__(self):
        if self.opponent:
            return "\033[1;35;40m" + self.symbol + "\033[0m"
        else:
            return "\033[1;34;40m" + self.symbol + "\033[0m"

class Obstacle:
    def __init__(self, current_position):
        self.current_position = current_position
    
    def __repr__(self):
        return "\033[1;33;40mX\033[0m"
    
class AttackedPosition:
    def __init__(self, current_position):
        self.current_position = current_position
    
    def __repr__(self):
        return "\033[1;31;40mA\033[0m"

class Goal:
    def __init__(self, position):
        self.position = position

    def checkGoal(self, coord):
        return coord[0] == self.position[0] and coord[1] == self.position[1]
    
    def __repr__(self):
        return "\033[1;32;40mG\033[0m"
    

class Board:
    def __init__(self, rows, columns, costs, obstacles_locations, enemy_pieces, friendly_pieces, goal_positions):
        #Create Board
        self.rows = rows
        self.columns = columns
        
        self.grid = [['0' for _ in range(columns)] for _ in range(rows)]
        
        #Matrix to store cost to move to each square
        self.costs = [[1 for _ in range(columns)] for _ in range(rows)]
        for cost in costs:
            self.costs[cost[0][0]][cost[0][1]] = cost[1]
            
        #Mark obstacles
        for loc in obstacles_locations:
            self.grid[loc[0]][loc[1]] = Obstacle(loc)
            
        #Mark goal positions
        self.goal_positions = set(goal_positions)
        for pos in self.goal_positions:
            self.grid[pos[0]][pos[1]] =  Goal(pos)
        
        #Mark pieces and the squares they attack
        for piece in enemy_pieces:
            attacked_positions = piece.possibleAttacks(self, piece.name, piece.current_position)
            #Attacked position is denoted by a Attacked Position clas
            for pos in attacked_positions:
                self.grid[pos[0]][pos[1]] = AttackedPosition(pos)
            #Occupy position by enemy piece
            self.grid[piece.current_position[0]][piece.current_position[1]] = piece
        
        for piece in friendly_pieces:
            #Occupy position by Friendly piece
            self.grid[piece.current_position[0]][piece.current_position[1]] = piece
        

        
    def updatePosition(self, piece, new_position):
        self.grid[piece.current_position[0]][piece.current_position[1]] = '0'
        piece.current_position = new_position
        self.grid[new_position[0]][new_position[1]] = piece
    
    def isGoal(self, coord):
        return coord in self.goal_positions
    
    def isAttackable(self, coord):
        if self.grid[coord[0]][coord[1]] == '0' or type(self.grid[coord[0]][coord[1]]) == AttackedPosition or type(self.grid[coord[0]][coord[1]]) == Goal:
            return True
        return False
    
    def isMovable(self, coord):
        if self.grid[coord[0]][coord[1]] == '0' or type(self.grid[coord[0]][coord[1]]) == Goal:
            return True
        return False
    
        
        
    def __repr__(self):
        grid = '\n'.join(['\t'.join(['|' + str(cell) + '|' for cell in row]) for row in self.grid])
        
        grid += "\n \n"
        
        
        #grid += '\n'.join(['\t'.join(['|' + str(cell) + '|' for cell in row]) for row in self.costs])
        
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
    selected_costs = []
    start = 5
    for i in range(rows * columns):
        index = start + i
        if lines[index][0] != '[':
            break
        else:
            loc, cost = lines[index].split(",")
            selected_costs.append((convert_to_index(loc[1:]), int(cost[:-2])))
    
    #Get enemy pieces
    enemy_pieces = []
    num_enemy_pieces = sum(map(int,lines[index].split(":")[1][:-1].split()))
    start =  index + 2
    for i in range(num_enemy_pieces):
        index = start + i
        piece_name, curr_pos = lines[index].split(",")
        enemy_pieces.append(Piece(piece_name[1:], convert_to_index(curr_pos[:-2])))
    
    #Get friendly pieces
    index = index + 1 if num_enemy_pieces != 0 else start
    friendly_pieces = []
    num_friendly_pieces = sum(map(int,lines[index].split(":")[1][:-1].split()))
    start = index + 2
    for i in range(num_friendly_pieces):
        index = start + i
        if lines[index][0] != '[':
            break
        else:
            piece_name, curr_pos = lines[index].split(",")
            friendly_pieces.append(Piece(piece_name[1:], convert_to_index(curr_pos[:-2]), opponent=False))
            
    #Get goal positions
    goal_positions = list(map(convert_to_index ,lines[-1].split(":")[1][:-1].split(" ")))
    
    return rows, columns, obstacle_locations, selected_costs, enemy_pieces, friendly_pieces, goal_positions


class Path:
    def __init__(self, current_coord):
        self.current_position = current_coord
        self.path = [current_coord]
    
    def add(self, coord):
        new_path = Path(coord)
        new_path.path = self.path + [coord]
        return new_path
    
    def __repr__(self):
        return " -> ".join(map(str,self.path))
        
    
        
def search(board, piece):
    frontier = [[piece.current_position]]
    nodesExplored = set()
    numNodesExplored = 0
    while frontier:
        current_path = frontier.pop(0)
        numNodesExplored += 1
        current_position = current_path[-1]
        nodesExplored.add(current_position)
        pos_moves = Piece.possibleMoves(board, piece.name, current_position)
        test = None
        for coord in pos_moves:
            if coord not in nodesExplored:
                if board.isGoal(coord):
                    current_path.append(coord)
                    return current_path, numNodesExplored
                else:
                    new_path = current_path.copy()
                    new_path.append(coord)
                    nodesExplored.add(coord)
                    frontier.append(new_path)
    return [], numNodesExplored
       

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# To return: List of moves and nodes explored
def run_BFS():
    # You can code in here but you cannot remove this function or change the return type
    file_path = argv[1]
    rows, columns, obstacle_locations, selected_costs, enemy_pieces, friendly_pieces, goal_positions = parse_input(file_path)
    board = Board(rows, columns, selected_costs, obstacle_locations, enemy_pieces, friendly_pieces, goal_positions)
    
    indMoves, numNodesExplored = search(board, friendly_pieces[0]) #For reference
    temp_moves = [convert_to_notation(move) for move in indMoves]
    moves = []
    for i in range(len(temp_moves) - 1):
        moves.append([temp_moves[i], temp_moves[i+1]])
    
    return moves, numNodesExplored #Format to be returned

if __name__ == '__main__':
    print(run_BFS())


