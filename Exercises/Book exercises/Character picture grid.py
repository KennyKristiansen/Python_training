spam = ['apples', 'bananas', 'tofu', 'cats']
list = ['john', 'elsa', 'pig', 'sofa', 'calculator']


def text(list_name):
    string = ''

    for i in range(0, (len(list_name))):
        if i < (len(list_name) - 1):
            string += list_name[i] + ', '
        else:
            string += 'and ' + list_name[i]
    print(string)


#####################################################

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def grid_rotate(grid_name):
    y = len(grid_name)
    x = len(grid_name[1])
    for i in range(0, x):
        x_grid = i
        print()
        for a in range(0, y):
            y_grid = a
            print(grid_name[y_grid][x_grid], end='')


grid_rotate(grid)
