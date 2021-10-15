import grid
import time

def occupied():
    # Represents an occupied cell
    return 1

def empty():
    # Represents an empty cell
    return 0

def is_empty(cell_coordinates):
    # Checks if a cell is empty
    # cell_coordinates is a list index
    if cell_coordinates == empty():
        return True
    else:
        return False

def empty_cell(list_index, cell_index):
    # Empties a cell
    # list_num is the list to change
    # cell_num is the list index to change
    list_index[cell_index] = empty()
    return list_index

def occupy_cell(list_index, cell_index):
    # Occupies a cell
    # list_num is the list to change
    # cell_num is the list index to change
    list_index[cell_index] = occupied()
    return list_index

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
    s = ''
    for row in grid:
        print(row_to_string(row))
        
test_grid = [[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
test_list = [0,0,0,0,0,0]
test_block = {'x': 2, 'y':0}

print(cell_to_string(test_grid[0][3]))
print(row_to_string(test_grid[0]))