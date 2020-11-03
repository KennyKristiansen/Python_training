import random #Side 74
secretnumber = random.randint(1,20)
guess = 0
print('I am thinking of a number between 1 and 20.')

for tries in range(1,7):
    print('Take a guess')
    guess =int(input())
    if guess<secretnumber:
        print('Your guess is too low.')
    elif guess>secretnumber:
        print('Your guess is to high')
    else:
        print('You guessed it, my number was ' + str(secretnumber))
        print('You used ' + str(tries) + ' tries')
        break
print('You lost, the number was ' + str(tries))