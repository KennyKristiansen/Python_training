tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(liste):
    #### Find the longest line ####
    longestlenght = 0
    for i in range(0,len(liste)):
        tablelenght = 0
        table = liste[i]
        for i in range(0,len(table)):
            tablelenght = len(table[i])
            if longestlenght < tablelenght:
                longestlenght = tablelenght
                print('longest word so far is ' + str(longestlenght) + ' characters long.')
    #### PRINTING TIME ####
    for x in range(len(liste[0])):


        for x in range(len(liste[0])):
            for y in range(len(liste)):
                print(tableData[y][x].rjust(longestlenght).center(), end = '')
            print('')

printTable(tableData)
