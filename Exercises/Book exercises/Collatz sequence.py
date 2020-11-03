print('Enter a number:')
inputnumber = int(input())
tries = 0

def collatz(number):
    if ((number%2) == 0):
        return(number // 2)
    else:
        return(3 * number + 1)


while inputnumber != 1:
    print(collatz(inputnumber))
    inputnumber = collatz(inputnumber)
    tries = tries + 1
print('The sequence ended after ' + str(tries) + ' loops')
