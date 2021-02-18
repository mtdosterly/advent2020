import re

with open("4_input") as file:
    data = []
    info = file.read().strip().split("\n\n")
    for x in info:
        x = list(re.split("\s|\n",x))
        x = dict((a,b) for a,b in (y.split(':') for y in x))
        data.append(x)

def passport_check(array):

    check_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    counter = 0

    for x in array:
        checksout = True
        for y in check_fields:
            if y not in x.keys():
                checksout = False
        if checksout == True:
            counter += 1

    return counter
