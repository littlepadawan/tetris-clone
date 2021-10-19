import time
from random import randint
from pynput import keyboard

starttime = time.time()

tick_rate = 2

game = 'on'
global direction
direction = ''
block_origin = {'x': 4, 'y': 0, 'state': 'active'}
block_list=[]

def new_grid():
    grid = []
    for x in range(10):
        grid.append([])
        for y in range(10):    
            grid[x].append(0)
    return grid

def new_block(grid):
    new_block = block_origin.copy()
    block_list.append(new_block)
    occupy_cell(grid[new_block['y']], new_block['x'])
    return(new_block)

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
            empty_cell(grid[block['y']], block['x'])
            block['y'] = block['y']+1
            occupy_cell(grid[block['y']], block['x'])
            return(block)
        else:
            block['state'] = 'passive'
            return(block)
    except IndexError:
        block['state'] = 'passive'
        return(block)

def move_left(block, grid):
    # Move block one step left if cell to the left is empty
    next_x = grid[block['y']][block['x']-1]
    if block['x'] > 0 and is_empty(next_x) == True:
        empty_cell(grid[block['y']], block['x'])
        block['x'] = block['x']-1
        occupy_cell(grid[block['y']], block['x'])
        return(block)
    else:
        return(block)
    
def move_right(block, grid):
    # Move block one step right if cell to the right is empty
    try:
        next_x = grid[block['y']][block['x']+1]
        if block['x'] < len(grid[block['y']]) and is_empty(next_x) == True:
            empty_cell(grid[block['y']], block['x'])
            block['x'] = block['x']+1
            occupy_cell(grid[block['y']], block['x'])
            return(block)
        else:
            return(block)
    except IndexError:
        return(block)
        
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

# def random_user_input():
#     inp = randint(0, 3)
#     if inp is 0:
#         return 'left'
#     elif inp is 1:
#         return 'right'
#     else:
#         return 'down'

def move_block(dirr, block, grid):
    global direction
    if dirr == 'left' or dirr == 'right':
        block = move_down(block, grid)
        block = move_sideways(dirr, block, grid)
        direction = ''
    else:
        block = move_down(block, grid)
    

def tick(grid, block):
    if block['state'] == 'active':
        global direction
        move_block(direction, block, grid)
        view_grid(grid)
    else:
        new_block(grid)

#         global game
#         game = 'over'

def on_press(key):
    global direction
    if key == keyboard.Key.left:
        direction = 'left'
    elif key == keyboard.Key.right:
        direction = 'right'
   
        
def refresh_grid(grid, block):
    global game
    while game == 'on':
        tick(grid, block_list[-1])
        time.sleep(tick_rate - ((time.time() - starttime) % tick_rate))

listener = keyboard.Listener(on_press=on_press)
listener.start()

test_grid = new_grid()
test_block = new_block(test_grid)

refresh_grid(test_grid, test_block)

