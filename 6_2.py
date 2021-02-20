with open("6_input") as file:
    info = file.read().strip().split('\n\n')

def count(array):

    from functools import reduce

    counter = 0

    def intersect(list1,list2):
        return [x for x in list1 if x in list2]

    for x in info:
        y = x.split('\n')
        yeslist = reduce(intersect,y)
        counter += len(yeslist)

    return counter

count(info)
