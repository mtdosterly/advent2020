with open("2_1_input") as file:
    pwds = list(file.read().split("\n"))
    pwds.pop()

def pwdcheck(array):

    counter = 0

    for x in array:
        tocheck = list(x.split(' '))
        pos = list(tocheck[0].split('-'))
        tosearch = tocheck[1][0]
        string = tocheck[2]
        p1 = int(pos[0])-1
        p2 = int(pos[1])-1

        if string[p1] == tosearch:
            if string[p2] == tosearch:
                continue
            else:
                counter += 1
        elif string[p2] == tosearch:
            counter += 1
        else:
            continue

    return counter

pwdcheck(pwds)
