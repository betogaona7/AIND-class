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

class testcode:

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
	    print("Everything looks good!")