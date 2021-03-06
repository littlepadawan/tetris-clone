import time
from pynput import keyboard

global direction

starttime = time.time() # Time in seconds since 'epoch'
tick_rate = 0.5 # Frequency of refreshing grid (in seconds)

game = 'on' # Game state
block_list = [] # Containing all created blocks
block_origin = {'x': 4, 'y': 0, 'state': 'active'} # Block template
direction = '' 

def start_splash():
#Startscreen splash
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n       Block som rör sig nedåt\n')
    print(' the groundbreaking tetris-like game\n\n')
    print('   Use the Left and Right arrow keys')
    print('          to move the blocks')
    print('\n     Press Enter to start the game')
    print('      Press Esc to quit the game')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    user_input = input('')
    if user_input == '':
        start_game()

def end_splash():
#Endscreen splash
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n       Thank you for playing!')
    print('\n     If you\'ve enjoyed the game,')
    print('  please be on the lookout for more')
    print('      games from Idgurd studios')
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def new_grid():
    # Creates a grid containing 10 rows and 10 columns
    grid = []
    for x in range(10):
        grid.append([])
        for y in range(10):    
            grid[x].append(0)
    return grid

def new_block(grid):
    # Creates a block and puts it on the grid
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

def move_block(dirr, block, grid):
    # Moves block
    # Always moves block one step down if possible
    # Moves block sideways depending on user input
    global direction
    if dirr == 'left' or dirr == 'right':
        block = move_sideways(dirr, block, grid)
        direction = ''
    block = move_down(block, grid)
    
def refresh_grid(grid, block): 
    # If block is active, move it and print updated grid
    # If block is not active, create a new block
    if block['state'] == 'active':
        global direction
        move_block(direction, block, grid)
        view_grid(grid)
    else:
        global game
        if grid[0][4] == empty():
            new_block(grid)
        else:
            game = 'over'

def on_press(key):
    # If user presses left arrow key or right arrow key,
    # set direction to left respective right
    global direction
    global game
    if key == keyboard.Key.left:
        direction = 'left'
    if key == keyboard.Key.right:
        direction = 'right'
    if key == keyboard.Key.esc:
        game = 'over'
        
def play(grid, block): 
    # While game is on, keep updating grid and creating new blocks
    global game
    while game == 'on':
        refresh_grid(grid, block_list[-1])
        time.sleep(tick_rate - ((time.time() - starttime) % tick_rate))
    end_splash()
        
def start_game():
    matrix = new_grid()
    first_block = new_block(matrix)
    play(matrix, first_block)
    
listener = keyboard.Listener(on_press = on_press) # Event listener for keyboard
listener.start()

start_splash()