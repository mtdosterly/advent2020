with open("1_1_input") as file:
    info = list(file.read().split("\n"))
    data = [int(x) for x in info if x != '']

def find2020(array):

    for x in range(0,len(array)):
        for y in range(x+1,len(array)):
            for z in range(y+1,len(array)):
                if array[x] + array[y] + array[z] == 2020:
                    return array[x]*array[y]*array[z]

find2020(data)
