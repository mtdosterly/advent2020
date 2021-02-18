with open("3_1_input") as file:
    info = list(file.read().split("\n"))
    info.pop()

def treecount_all(array,var):
    
    x = trees = 0
    
    for y in array:
        if x <= len(y)-1:
            if y[x] == '#':
                trees += 1
                x += var
            else:
                x += var
        else:
            x -= len(y)
            if y[x] == '#':
                trees += 1
                x += var
            else:
                x += var
        
    return trees

def treecount_skip(array,var):
    
    x = trees = 0
    
    for z in range(0,len(array)):
        if z == 0 or z%2 == 0:
            if x <= len(array[z])-1:
                if array[z][x] == '#':
                    trees += 1
                    x += var
                else:
                    x += var
            else:
                x -= len(array[z])
                if array[z][x] == '#':
                    trees += 1
                    x += var
                else:
                    x += var
        else:
            continue
        
    return trees

treecount_all(info,1) * treecount_all(info,3) * treecount_all(info,5) * treecount_all(info,7) * treecount_skip(info,1)
