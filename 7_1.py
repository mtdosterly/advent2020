import re

with open("7_input") as file:
    info = file.read().strip().split('\n')
    
replace_dict = {" bags":""," bag":""," contain":":", "no other": "0", ".":''}
data = []

for x in info:
    for a,b in replace_dict.items():
        x = x.replace(a,b)
        y = x.split(": ")
    data.append(y)

for x in data:
    x[1] = x[1].split(", ")

def bag(array):

    baglist = []
    templist = []
    searchlist = []
    
    for x in array: # initial set of results
        for y in x[1]:
            if re.search(r"shiny gold",y):
                templist.append(x)
    
    searchover = False
    
    while searchover == False: #keep adding to list while search comes up with new bags
        for x in templist:
            baglist.append(x)
        
        array = [x for x in array if x not in baglist]
        
        for x in templist:
            searchlist.append(x[0])
            
        if templist == []:
            searchover = True
            break
        
        templist = []

        for x in searchlist:
            for y in array:
                for z in y[1]:
                    if re.search(fr"{x}",z):
                        templist.append(y)
    
    final = set()
    
    for x in baglist:
        final.add(x[0])
        
    return len(final)

bag(data)
