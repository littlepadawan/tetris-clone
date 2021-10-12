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