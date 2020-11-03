#! python3
#Project - Password locker.py
import pyperclip
print(pyperclip.paste())

password = {'email':'Piksvin09','blog':'1234','youtube':'nein'}

import sys
if len(sys.argv) < 2:
    print('Usage: python password.py [Account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in password:
    pyperclip.copy(password[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)