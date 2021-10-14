test_list = [0,1,0,1,0,0]

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

def empty_cell(list_num, cell_num):
    # Empties a cell
    # list_num is the list to change
    # cell_num is the list index to change
    list_num[cell_num] = empty()
    return list_num

def occupy_cell(list_num, cell_num):
    # Occupies a cell
    # list_num is the list to change
    # cell_num is the list index to change
    list_num[cell_num] = occupied()
    return list_num

#print(is_empty(test_list[1]))
#print(occupy_cell(test_list, 2))
#print(empty_cell(test_list, 2))

block = {'coordinates': [0,0]}

def move_down(block):
    block['coordinates'][1] = block['coordinates'][1] + 1
    return(block)
    

