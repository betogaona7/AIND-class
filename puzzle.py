# We'll record the puzzle in two ways  - string and as a dictionary

# The string will consist of a concatenation of all the readings of the digits in the rows, taking the rows 
# to top from bottom. If the puzzle is not solved we can use a . as a placeholder for an empty box
# For example, an unsolved puzzle will be written as:
# ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
# And the solved puzzle will be recorded as:
# 483921657967345821251876493548132976729564138136798245372689514814253769695417382

# We'll implement the dictionary as follows. The keys will be string corresponding to the boxes - namely, 'A1'
# 'A2',.., 'I9'. The values will either be the digit in each box (if there is one) or a '.' (if not)

# Display function shows a nice visual representation of the dictionary
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# We'll record rows and columns as strings.
rows = 'ABCDEFGHI'
cols = '123456789'

# helper function which, given two strings - a and b - will return the list formed by all possibles concatenations
# of a letter s in string a tirh a letter t in string b
def cross(a, b):
	return [s+t for s in a for t in b]

# Create labels of the boxes
boxes = cross(rows, cols)

# Create labels of the units
row_units = [cross(r, cols) for r in rows] # row units 
col_units = [cross(rows, c) for c in cols] # col units
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123','456','789')] # square 3x3 units 

unitlist = row_units + col_units + square_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

#---------------------------------------------------------------------------------------
# Turn te string reprentation of a sudoku intro a dictionary representation

# A function to convert the string representation of a puzzle into a dictionary form 
""" - Encoding board 
def grid_values(values):
	return dict([box, value] for box, value in zip(boxes, values))"""

""" Udacity solution 
def grid_values(values):
    assert len(values) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, values)) """
#----------------------------------------------------------------------------------------

# Strategy 1 - Elimination - If a box has a value addigned, then none of the peers of this box can have this value


# As of now, we are recording the puzzles in dictonary form, where the keys are the boxes ('A1', 'A2', ..., 'I9') and 
# the values are either the value for each box (if a value exists) or '.' (if the box has no value assigned yet). What
# we really wantis for each value to represent all the avalaible values for that box. 


""" - Improved grid_values fuction to return '123456789' instead of '.' for empty boxes """
def grid_values(values):
    dictionary = {}
    for box, value in zip(boxes, values):
        if value == '.':
            value = '123456789'
        dictionary[box] = value
    return dictionary

""" Udacity solution 
def grid_values(grid):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values)) """

# Function eliminate take as input a puzzle in dictionary form. The function will iterate over all the boxes in the puzzle
# that only have one value assigned to them, and it will remove this value from every one of its peers

""" - Implement eliminate() """
def eliminate(values):
    for box, value in values.items():
        if len(value) == 1:
            for peer in peers[box]:
                values[peer] = values[peer].replace(value,"")
    return values

test = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

display(eliminate(grid_values(test)))
#display(grid_values(test))



	