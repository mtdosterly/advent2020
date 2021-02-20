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
    colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    counter = 0
    
    def byrcheck(x):
        if 1920 <= int(x) <= 2002:
            return True
        else:
            return False
        
    def iyrcheck(x):
        if 2010 <= int(x) <= 2020:
            return True
        else:
            return False
        
    def eyrcheck(x):
        if 2020 <= int(x) <= 2030:
            return True
        else:
            return False
        
    def hgtcheck(x):
        if x[-2] == "c":
            if 150 <= int(x[:-2]) <= 193:
                return True
            else:
                return False
        elif x[-2] == "i":
            if 59 <= int(x[:-2]) <= 76:
                return True
            else:
                return False
        else:
            return False
    
    def hclcheck(x):
        if len(x) != 7:
            return False
        elif x[0] != "#":
            return False
        elif re.search("[^a-z|A-Z|0-9]",x[1:7]) == True:
            return False
        else:
            return True
    
    def eclcheck(x):
        if x in colors:
            return True
        else:
            return False
    
    def pidcheck(x):
        if len(x) != 9:
            return False
        elif re.search("[\D]",x[0:9]) == True:
            return False
        else:
            return True
    
    for x in array:
        checksout = True
        for y in check_fields:
            if y not in x.keys():
                checksout = False
        if checksout == True:
            if not byrcheck(x["byr"]):
                checksout = False
            elif not iyrcheck(x["iyr"]):
                checksout = False
            elif not eyrcheck(x["eyr"]):
                checksout = False
            elif not hgtcheck(x["hgt"]):
                checksout = False
            elif not hclcheck(x["hcl"]):
                checksout = False
            elif not eclcheck(x["ecl"]):
                checksout = False
            elif not pidcheck(x["pid"]):
                checksout = False
            
        if checksout == True:
            counter += 1

    return counter

passport_check(data)
