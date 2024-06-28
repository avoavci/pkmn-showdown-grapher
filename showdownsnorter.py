import re
import numpy as np
# pokemon showdown graph creator by Avo

# creates pokemon list for each trainer
def trainer(i):
    pokelist = []
    st = nameTable["trainer{0}".format(i)] + ' sent out'
    p = len(st) +1
    # checks every 
    for item in listStr:
        t1 = re.findall(st + r'.+', item)
        # creates a slice from the match object that just gives the pkmn name
        t1p = [match[p:] for match in t1]
        # removes any brackets, spaces or special characters from pkmn name
        if len(t1p) > 0:
             t1p[0] = t1p[0].replace("!", "")
             t1p[0] = re.sub(r'\([^)]*\)', "", t1p[0])
             t1p[0] = re.sub(r'\s+$', "", t1p[0])
             pokelist.append(t1p)
    # using numpy unique() to get rid of dupes (from switching pkmn)
    pokelist = np.unique(pokelist)
    pokelist = pokelist.tolist()
    # if the list is empty after checking every line for trainer name
    # then the program assumes that it is the host machine's pkmn and searches
    # again for them with the string "Go!" instead
    if len(pokelist) == 0:
        st = 'Go!'
        p = len(st) +1
        for item in listStr:
            t1 = re.findall(st + r'.+', item)
            t1p = [match[p:] for match in t1]
            if len(t1p) > 0:
                 t1p[0] = t1p[0].replace("!", "")
                 t1p[0] = re.sub(r'\([^)]*\)', "", t1p[0])
                 t1p[0] = re.sub(r'\s+$', "", t1p[0])
                 pokelist.append(t1p)
        pokelist = np.unique(pokelist)
        pokelist = pokelist.tolist()
    return(pokelist)
# trainer 1's hits, requiring the pokemon's name. This code is messy i hate it
def t1hits(currentMon):
    # searches each line for the pokemon using an ability
    for i in range(len(listStr)):
         if re.search(currentMon, listStr[i]) != None:
         # if it is found, then checks subsequent lines to see who is hit
            for j in range(20):
                i += 1
                # searching for brackets since any damage instances leads with
                # brackets
                if re.search(r'\([^)]*\)', listStr[i]) != None:
                    listStr[i] = re.sub('[(]', "", listStr[i])
                    # checks each trainers pokemon list to see who was hit
                    for k in range(len(trainer1["pokemon"])):
                        t2hit = trainer1["pokemon"][k] + " lost"
                        if re.search(t2hit, listStr[i]) != None:
                            trainer0["hit1"] += 1
                    for k in range(len(trainer2["pokemon"])):
                        t3hit = trainer2["pokemon"][k] + " lost"
                        if re.search(t3hit, listStr[i]) != None:
                            trainer0["hit2"] += 1
                    for k in range(len(trainer3["pokemon"])):
                        t4hit = trainer3["pokemon"][k] + " lost"
                        if re.search(t4hit, listStr[i]) != None:
                            trainer0["hit3"] += 1
                # if there is a blank line, it means the next move is happening
                # so it breaks the loop
                if listStr[i] == "":
                    break
# one of these functions for each trainer, functionally identical
def t2hits(currentMon):
    for i in range(len(listStr)):
         if re.search(currentMon, listStr[i]) != None:
            for j in range(20):
                i += 1
                if re.search(r'\([^)]*\)', listStr[i]) != None:
                    listStr[i] = re.sub('[(]', "", listStr[i])
                    for k in range(len(trainer0["pokemon"])):
                        t1hit = trainer0["pokemon"][k] + " lost"
                        if re.search(t1hit, listStr[i]) != None:
                            trainer1["hit0"] += 1
                    for k in range(len(trainer2["pokemon"])):
                        t3hit = trainer2["pokemon"][k] + " lost"
                        if re.search(t3hit, listStr[i]) != None:
                            trainer1["hit2"] += 1
                    for k in range(len(trainer3["pokemon"])):
                        t4hit = trainer3["pokemon"][k] + " lost"
                        if re.search(t4hit, listStr[i]) != None:
                            trainer1["hit3"] += 1
                if listStr[i] == "":
                    break

def t3hits(currentMon):
    for i in range(len(listStr)):
         if re.search(currentMon, listStr[i]) != None:
            for j in range(20):
                i += 1
                if re.search(r'\([^)]*\)', listStr[i]) != None:
                    listStr[i] = re.sub('[(]', "", listStr[i])
                    for k in range(len(trainer0["pokemon"])):
                        t1hit = trainer0["pokemon"][k] + " lost"
                        if re.search(t1hit, listStr[i]) != None:
                            trainer2["hit0"] += 1
                    for k in range(len(trainer1["pokemon"])):
                        t2hit = trainer1["pokemon"][k] + " lost"
                        if re.search(t2hit, listStr[i]) != None:
                            trainer2["hit1"] += 1
                    for k in range(len(trainer3["pokemon"])):
                        t4hit = trainer3["pokemon"][k] + " lost"
                        if re.search(t4hit, listStr[i]) != None:
                            trainer2["hit3"] += 1
                if listStr[i] == "":
                    break

def t4hits(currentMon):
    for i in range(len(listStr)):
         if re.search(currentMon, listStr[i]) != None:
            for j in range(20):
                i += 1
                if re.search(r'\([^)]*\)', listStr[i]) != None:
                    listStr[i] = re.sub('[(]', "", listStr[i])
                    for k in range(len(trainer1["pokemon"])):
                        t2hit = trainer1["pokemon"][k] + " lost"
                        if re.search(t2hit, listStr[i]) != None:
                            trainer3["hit1"] += 1
                    for k in range(len(trainer2["pokemon"])):
                        t3hit = trainer2["pokemon"][k] + " lost"
                        if re.search(t3hit, listStr[i]) != None:
                            trainer3["hit2"] += 1
                    for k in range(len(trainer0["pokemon"])):
                        t1hit = trainer0["pokemon"][k] + " lost"
                        if re.search(t1hit, listStr[i]) != None:
                            trainer3["hit0"] += 1
                if listStr[i] == "":
                    break
                
    
rawStr = input("Enter the battle log here ty: ")
listStr = list(rawStr.split("\n"))
# certain special characters give regex a hard time. forgive me
for i in range(len(listStr)):
    listStr[i] = re.sub("/", "", listStr[i])


nameTable = {}
names = listStr[0]

# I will eventually implement a way to see how many protects are used by
# each trainer, stored in "pt" integer variable
trainer0 = dict(name = "", pokemon = "", hit1 = int(0),
                hit2 = int(0), hit3 = int(0), pt = int(0))
trainer1 = dict(name = "", pokemon = "", hit0 = int(0),
                hit2 = int(0), hit3 = int(0), pt = int(0))
trainer2 = dict(name = "", pokemon = "", hit0 = int(0),
                hit1 = int(0), hit3 = int(0), pt = int(0))
trainer3 = dict(name = "", pokemon = "", hit0 = int(0),
                hit1 = int(0), hit2 = int(0), pt = int(0))

name1 = re.findall("☆\w*", names)

for i in range(len(name1)):
    cName = re.sub("☆", "",name1[i], 1)
    nameTable["trainer{0}".format(i)] = cName
    
# constructing each trainer dictionary values
i = 0
trainer0["name"] = nameTable["trainer{0}".format(i)]
trainer0["pokemon"] = trainer(i)
i = 1
trainer1["name"] = nameTable["trainer{0}".format(i)]
trainer1["pokemon"] = trainer(i)
i = 2
trainer2["name"] = nameTable["trainer{0}".format(i)]
trainer2["pokemon"] = trainer(i)
i = 3
trainer3["name"] = nameTable["trainer{0}".format(i)]
trainer3["pokemon"] = trainer(i)

for i in range(len(trainer0["pokemon"])):
    currentMon = trainer0["pokemon"][i] + " used "
    t1hits(currentMon)

for i in range(len(trainer1["pokemon"])):
    currentMon = trainer1["pokemon"][i] + " used "
    t2hits(currentMon)
    
for i in range(len(trainer2["pokemon"])):
    currentMon = trainer2["pokemon"][i] + " used "
    t3hits(currentMon)

for i in range(len(trainer3["pokemon"])):
    currentMon = trainer3["pokemon"][i] + " used "
    t4hits(currentMon)



            
       
    