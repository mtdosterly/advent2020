with open("6_input") as file:
    info = file.read().strip().split('\n\n')

def count(array):
    counter = 0

    for x in info:
        y = set(str(x).replace('\n', ''))
        counter += len(y)

    return counter

count(info)
