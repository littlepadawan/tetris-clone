grid = []

def create_lists():
    a = []
    for x in range(10):
        a.append(0)
    for x in range(10):    
        grid.append(a)
    return grid

def print_lists(a):
    
    for element in a:
        print(element)

create_lists()

print(grid)
grid[3][4] = 1
print(grid)

# grid_list = grid



# def new_grid():
#     print('2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2')
#     for n in range(11):
#         print('2', grid_list, '2')
#     print('2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2')

#        print('2', a, '2')

# grid_list2 = ['%' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '%']
# 
# def end_grid(l):
#     print('%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%', '%')
#     for a in l:
#         print (l[a])
#         
#     print('%','%','%','%','%','%','%','%','%','%','%','%',)
