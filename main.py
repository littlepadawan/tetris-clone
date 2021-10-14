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
        

test_grid = [[0,0,0,1,0],[0,0,0,1,0],[0,0,0,0,0]]
test_list = [0,0,0,0,0,0]
test_block = {'x': 2, 'y':0}

#print(is_empty(test_list[1]))
#print(occupy_cell(test_list, 2))
#print(empty_cell(test_list, 2))            

print(move_down(test_block, test_grid))
print(move_left(test_block, test_grid))
print(move_right(test_block, test_grid)) 

#move_sideways('left', test_block, test_grid)


