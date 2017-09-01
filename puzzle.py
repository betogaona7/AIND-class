# We'll record the puzzle in two ways  - string and as a dictionary

# The string will consist of a concatenation of all the readings of the digits in the rows, taking the rows 
# to top from bottom. If the puzzle is not solved we can use a . as a placeholder for an empty box
# For example, the unsolved puzzle at the above left will be written as:
# ..3.2.6..9..3.5..1..1..18.64 ... 
# And the solved puzzle at the above right will be recorded as:
# 4839214633231123412341234132 ...

# We'll implement the dictionary as follows. The keys will be string corresponding to the boxes - namely, 'A1'
# 'A2',.., 'I9'. The values will either be the digit in each box (if there is one) or a '.' (if not)


# Display function shows a nice vuisual representation of the dictionary
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

# Turn te string reprentation of a sudoku intro a dictionary representation

# A function to convert the string representation of a puzzle into a dictionary form 
def grid_values(values):
	return dict([box, value] for box, value in zip(boxes, values))

test = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'

display(grid_values(test))



	