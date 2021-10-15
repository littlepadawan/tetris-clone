import grid
import time

def occupied():
    # Represents an occupied cell
    return 1

def empty():
    # Represents an empty cell
    return 0

def is_empty(x_coordinate):
    # Checks if a cell is empty
    # x_coordinate - index of the cell to check
    if x_coordinate == empty():
        return True
    else:
        return False

def empty_cell(row, x_coordinate):
    # Empties a cell
    # row - list containing the cell to change
    # x_coordinate - the cell to change
    row[x_coordinate] = empty()
    return row

def occupy_cell(row, x_coordinate):
    # Occupies a cell
    # row - list containing the cell to change
    # x_coordinate - the cell to change
    row[x_coordinate] = occupied()
    return row

def move_down(block, grid):
    # Move block one step down if cell under is empty
    try:
        next_y = grid[block['y']+1][block['x']]
        if is_empty(next_y) == True:
            block['y'] = block['y']+1
            return(block, 'Its empty!')
        else:
            return(block, 'Its not empty!')
    except IndexError:
        return(block, 'Hit ground')

def move_left(block, grid):
    # Move block one step left if cell to the left is empty
    next_x = grid[block['y']][block['x']-1]
    if block['x'] > 0 and is_empty(next_x) == True:
        print('Its empty')
        block['x'] = block['x']-1
        return(block, 'Block x-coordinate updated!')
    else:
        return(block, 'Collision')
    
def move_right(block, grid):
    # Move block one step right if cell to the right is empty
    try:
        next_x = grid[block['y']][block['x']+1]
        if block['x'] < len(grid[block['y']]) and is_empty(next_x) == True:
            print('Its empty')
            block['x'] = block['x']+1
            return(block, 'Block x-coordinate updated!')
        else:
            return(block, 'Collision')
    except IndexError:
        return(block, 'You are at the border')
        
def move_sideways(direction, block, grid):
    # Move block sideways depending on input
    if direction == 'left':
        return move_left(block, grid)
    if direction == 'right':
        return move_right(block, grid)
        
def cell_to_string(cell):
    # Converts a cell to a string
    # cell - list index of the cell to convert
    if is_empty(cell) == True:
        return(' ')
    elif is_empty(cell) == False:
        return('*')

def row_to_string(row):
    # Converts a row of cells to a string
    # row - list representing a row on the grid
    s = ''
    for cell in row:
        s = s + cell_to_string(cell)
    return s

def view_grid(grid):
    # Prints grid
    # grid - list of rows
    top_line = ' '
    bottom_line = ' '
    for x in range(len(grid[0])):
        top_line = top_line + '_'
        bottom_line = bottom_line + '_'
    print(top_line)
    for row in grid:
        print(f'|{row_to_string(row)}|')
    print(bottom_line)
    
test_grid = grid.new_grid()
test_block = {'x': 2, 'y':0}

#print(cell_to_string(test_grid[0][3]))
#print(row_to_string(test_grid[0]))
view_grid(test_grid)