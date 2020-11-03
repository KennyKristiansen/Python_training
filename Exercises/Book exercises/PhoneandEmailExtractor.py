#! python3
#PhoneandEmailExtractor.py - Finds phone numbers and email addresses

import re, pyperclip
phoneregex = re.compile(r'''(
(\+\d\d)?  #finder +45 hvis tilstede
((\d{2})
\s?
(\d{2})
\s?
(\d{2})
\s?
(\d{2})
\s?
(\d{2})?)
)''',re.VERBOSE)

emailregex = re.compile(r'''(
[a-zA-Z0-9.\-_+\-æøå]+  #finder email
@       #finder @
[a-zA-Z\.æøå]+    #finder domænet
)''',re.VERBOSE)

phonenumber = phoneregex.findall((pyperclip.paste()))
emailadress = emailregex.findall((pyperclip.paste()))
###Samling af numre




#text = ('phonenumber: ' + str(phonenumber.groups[1]) + '\n''Emailadress: ' + str(emailadress.groups[1]))
#print(text)
#print('Phonenumber and Emailadress are copied to clipboard.')
#pyperclip.copy(text)
match = []
match.append('Following phone numbers were found:')
for i in phonenumber:
    if i[7] != '':
        numbers = ''.join(['+',i[1],i[3],' ', i[4], i[5], i[6],i[7]])
        match.append(numbers)
    else:
        numbers =''.join([i[1],i[3],i[4],i[5],i[6]])
        match.append(numbers)

match.append('\n''Following email adresses were found:')
for i in emailadress:
    match.append(i)

for i in range(0,len(match)):
    print(match[i])

###Want to save output?
print('Want to save list to clipboard? (Y/N)')
answer = input()
if answer == 'Y':
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard')
else:
    print('Nothing saved to clipboard')

