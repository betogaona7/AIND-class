"""
	Here we are implement the minimax algorithm to solve the isolation game.
"""
from copy import deepcopy

xlimit, ylimit = 3, 2 # Board dimensions

class GameState:

    def __init__(self):
    	self.board = [[0] * ylimit for _ in range(xlimit)] # Create the board 2*3  [0 0 0]
    													   #					   [0 0 0]
    	self.board[2][1] = 1 # Block the lower rigth corner [0 0 0]
    						 #                              [0 0 1]
    	self.player = 0 # Active player; 0 indicates that player one has initiative and 1 indicates player 2
    	self.player_locations = [None, None] # Keep track of the current location of each player on the board
    	
    
    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if move not in self.get_legal_moves():
        	return "Attempted forecast of illegal move"
        newBoard = deepcopy(self)
        newBoard.board[move[0]][move[1]] = 1
        newBoard.player_locations[self.player] = move
        newBoard.player ^= 1
        return newBoard
    
    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        location = self.player_locations[self.player]
        if not location:
        	return self.get_blank_spaces()

       	moves = []
       	rays = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

       	for dx, dy in rays:
       		_x, _y = location
       		while 0 <= _x + dx < xlimit and 0 <= _y + dy < ylimit:
       			_x, _y = _x +dx, _y + dy
       			if self.board[_x][_y]:
       				break
       			moves.append((_x,_y))
       	return moves



    def get_blank_spaces(self):
    	""" Return a list of blank spaces on the board. """
    	return [(x,y) for y in range(ylimit) for x in range(xlimit) if self.board[x][y] == 0]


def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    return not bool(gameState.get_legal_moves()) # No more moves

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
    	return 1
    v = float("inf")
    for m in gameState.get_legal_moves():
    	v = min(v, max_value(gameState.forecast_move(m)))
    return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
    	return -1 
    v = float("-inf")
    for m in gameState.get_legal_moves():
    	v = max(v, min_value(gameState.forecast_move(m)))
    return v

def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    return  max(gameState.get_legal_moves(), key=lambda m: min_value(gameState.forecast_move(m)))
    

""" Test GameState
print("Creating empty game board...")
g = GameState()

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))

print(g1.board)

print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()
if (0, 0) in set(p2_empty_moves):
    print("Failed\n  Uh oh! (0, 0) was not blocked properly when " +
          "player 1 moved there.")
else:
    print("Everything looks good!") """


""" Test minimax_helper
g = GameState()
print("Calling min_value on an empty board...")
v = min_value(g)
if v == -1:
    print("min_value() returned the expected score!")
else:
    print("Uh oh! min_value() did not return the expected score.") """

# Test minimax
best_moves = set([(0, 0), (2, 0), (0, 1)])
rootNode = GameState()
minimax_move = minimax_decision(rootNode)

print("Best move choices: {}".format(list(best_moves)))
print("Your code chose: {}".format(minimax_move))

if minimax_move in best_moves:
    print("That's one of the best move choices. Looks like your minimax-decision function worked!")
else:
    print("Uh oh...looks like there may be a problem.")