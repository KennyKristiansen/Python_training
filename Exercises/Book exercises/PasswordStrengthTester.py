#! python3
# PasswordStrengthTester.py - Tests how strong the password is

import re

print('What is your password?')
password = str(input())

smallletterregex = re.compile(r"[a-z]+")
bigletterregex = re.compile(r"[A-Z]+")
numberregex = re.compile(r"[0-9]+")
signregex = re.compile(r"\W+")

def tester(password):
    points = len(password)*0.25
    small = ((smallletterregex.findall(password)))
    big = (bigletterregex.findall(password))
    number = (numberregex.findall(password))
    sign = (signregex.findall(password))
    for i in range(0,len(small)):
        points += (len(small[i]) * 0.15)
    for i in range(0,len(big)):
        points += (len(big[i]) * 0.20)
    for i in range(0, len(number)):
        points += (len(number[i]) * 0.5)
    for i in range(0,len(sign)):
        points += (len(sign[i]) * 1.5)
    print(points)
    if points < 5:
        print('Weak password')
    elif points < 8:
        print('Okay password')
    elif points < 12:
        print('Strong password')





tester(password)
