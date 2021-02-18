with open("3_1_input") as file:
    info = list(file.read().split("\n"))
    info.pop()

def treecount(array):

    x = trees = 0

    for y in array:
        if x <= len(y)-1:
            if y[x] == '#':
                trees += 1
                x += 3
            else:
                x += 3
        else:
            x -= len(y)
            if y[x] == '#':
                trees += 1
                x += 3
            else:
                x += 3

    return trees
