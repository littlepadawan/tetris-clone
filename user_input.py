from random import randint

def random_user_input():
    inp = randint(0, 3)
    if inp is 0:
        return 'left'
    elif inp is 1:
        return 'right'
    else:
        return 'down'



def move_block(rand, block, grid):
    if rand == 'left' or a == 'right':
        move_sideways(rand, block, grid)
    else:
        move_down(block, grid)