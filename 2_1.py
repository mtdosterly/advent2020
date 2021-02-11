with open("2_1_input") as file:
    pwds = list(file.read().split("\n"))
    pwds.pop()

def pwdcheck(array):

    counter = 0

    for x in array: #split into range(rng), letter searched for (tosearch), and search string (tocheck[2])
        tocheck = list(x.split(' '))
        rng = list(tocheck[0].split('-'))
        tosearch = tocheck[1][0]
        hits = tocheck[2].count(tosearch)
        if hits >= int(rng[0]) and hits <= int(rng[1]):
            counter +=1

    return counter

pwdcheck(pwds)
