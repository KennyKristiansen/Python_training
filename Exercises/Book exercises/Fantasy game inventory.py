inventory = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
Alarm = {'rope':12,'gold coin':420,'arrow':12,'bottle':10}

def displayinventory(player):
    liste = list(player)
    print(liste)
    total = 0
    for i in range(len(player)):
        print(str(player[liste[i]]) + ' ' + str(liste[i]))
        total += player[liste[i]]
    print('Total number of items: ' + str(total))

#displayinventory(inventory)
print()
#displayinventory(Alarm)

def displayInventory(player):
    total = 0
    for k, v in player.items():
        print(str(v) + ' ' + str(k))
        total += v
    print('Total number of items: ' + str(total))

#displayInventory(inventory)
print()
#displayInventory(Alarm)

def addtoinventory(player,addeditems):
    newInventory = {}
    for k, v in player.items():
        v += addeditems.get(k,0)
        newInventory[k] = v
    player = newInventory
    print(player)


addtoinventory(inventory,Alarm)