#Kapitel 1
print('Hvad er dit navn?')
varName = input() #Sætter variabel vha. input
len(varName) #antal tegn
str() #string
int()  #hele tal
float() #komma-tal

#Boolean kapitel 2
bool(1==1) # True or false
1 == 2 #lig med
1 != 1 #Not equal to
1 < 1
1 > 1
1 <= 1
1 >= 1
and # Begge skal være True
or # Den ene skal være True
not # not true == False
if condition == True:
    clause #kaldet "if clause"
else:
    clause #kaldet "else clause"
elif:
    clause #kaldet "elif clause"
while True #kaldet loop
    continue #går direkte hen og tjekker condition
    break #stopper while loopet
for variable in range(5) #range er antal gange, variable starter som 0
range(10,20,2) #10 =start og 20 = stop 2 = step/stigning pr. gang

import
sys.exit() #afslutter programmet, kræver import af sys

#kapitel 3
def function(argument)
    print('hello'+argument)

return  # f.eks. hvis svar er 1 == 'femten'
None    #null eller undefined

#Kapitel 4 lists
listeA = ['item1','item2','item3']
listeA[1] = items2
listeA[0:1] = item1 og item2
len(listeA) = antal items
del listeA[2] = fjerner item3 #bruges til at fjerne vha. placering
listeA.index('Word to find in list')
listeA.append('item4') #indsætter item til sidst i liste
listeA.insert(1,'item1A') #indsætter item i liste, på givet sted
listeA.remove('item1A') #bruges til at fjerne vha. navn
listeA.sort() #sorterer liste ASCII-alfabetisk
listeA.sort(reverse=true) #Sorterer liste omvendt ASCII-alfabetisk
listeA.sort(key=str.lower) #sorterer efter normal alfabetisk orden

#Kapitel 5 Dictionary
dict = {'size':'big','color':'red','type':'toy'}
dict.keys()
dict.values()
dict.items()
item = key,value
for k in dict() # keys
for v in dict() # dictionary
for i in dict() # items
dict.get(value_to_get,Fall_back_value)
dict.setdefault()
pprint.pprint() #printer dictionaries ud formateret
pprint.format() #printer ikke, men kan bruges til at gemme værdier

#Kapitel 6 Manipulating strings
'\' text' eller "\" text" #escape character, gør det muligt at bruge alle tegn
\t # tab
\n # New line (linebreak)
\\ #backslash
r'' # Raw string, ignorerer alle escape tegn
'''text
tex''' #multiline string, over flere linjer, i stedet for \n
text[0:9] #finder de første 10 bogstaver af en string

text.upper() # laver alt til uppercase
text.lower() #laver alt til lowercase
text.isupper() # True or false
text.islower() # True or false
isalpha() # true hvis kun kun tekst
isalnum() # true hvis kun tal og tekst
usdecimal() #true hvis kun tal
isspace() # true hvis space, tabs eller newline
istitle() # true hvis ord starter med stort
startswith('tekst') #true or false
endswith('tekst') #true or false

', '.join() #sammensætter strings
# ', ' betyder at alt skal sammensættes med et komma og et mellemrum
'text text text'.split(argument) # argument kan f.eks. være '\n'
#splitter en text til en liste-form

'tekst'.rjust(10,'filler')
'tekst'.ljust(10,'filler')
'tekst'.center(20,'filler')

'tekst'.strip() #Removes whitespace
'tekst'.lstrip() #Remove whitespace left
'tekst'.rstrip() #Remove whitespace right
'tekst'.strip('ekst') # = 't'

import pyperclip #kan bruges til at copy paste fra clipboard
pyperclip.copy('tekst')
pyperclip.paste()

# Kapitel 7 Pattern matching with regular expressions
#regres functions hentes vha.
import re #bruges f.eks. til at søge
phonenumber =re.compile(r'\+45\d{8}') #finder alle danske telefonnumre
# r'' betyder raw, derved undgås escape characters
# herved bliver det ikke \\d men bare \d
mo = phonenumber.search('text') # søger efter numre i en given tekst
print(mo.group()) # udprinter det fundne nummer
mo = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') #her bruges () til at inddele i grupper
# herved kan de enkelte grupper kaldes frem vha.
mo.group(1) #viser den første gruppe
mo.group(2) #anden gruppe
mo.group(0) #alle grupper
mo.groups() #henter alle grupper men inddelt i tuple
areacode, mainnumber = mo.groups()
#herved blive gruppe 1 = areacode og gruppe 2 = mainnumber
| #kaldes pipe, fungerer som "or", men returnerer den første sande værdi
re.compile(r'Bat(man|mobile|copter|bat)') #søger på ordene batman, batmobile osv.
batRegex = re.compile(r'Bat(wo)?man') # ? indikerer at wo ikke er nødvendigt, kun måske tilstede
re.compile(r'Bat(wo)*man') #match wo nul eller flere gange
#matcher f.eks. batwowowowoman
batRegex = re.compile(r'Bat(wo)+man') # match en eller flere
re.compile(r'(Ha){1,3}') #matcher med ha, haha eller hahaha
re.compile(r'(Ha){1,3}?') #nongreedy, finder den mindste mulighed
batRegex.findall('text') #finder alle kombinationer, kommer ud som liste
#hvis regex finder grupper, kommer det ud som en tuple
#### andre forkortelser til regex side 158.
re.compile(r'.at') # . fungerer som wildcard, så f.eks. cat, hat, sat er ok
re.compile(r'first name: (.*)') #finder så meget som muligt efter first name:, everything
re.IGNORECASE #eller re.I #ignorerer forskel i små og store bogstaver
batRegex.sub(r'superman','batman is strongest') #substituerer batman med superman

#Kapitel 8 reading and writing files
import os
os.path.join('usr','bin','spam') # usr\\bin\\spam
os.getcwd() #current working directory
os.chdir('C:\\Winsows\\System32') #new working directory
os.makedirs('C:\\folder1\\folder2')
filedir = open('C:\\folder1')
filedir.read(argument) #argument kan være r,w og a
#Read, Write eller append
filedir.write('filename.txt')
import shelve #muliggør save and open funktion for et program
file = shelve.open('filename') #ligesom en dictionary
file.keys() #ligsom med en dictionary
file.values()

#Kapitel 9 Organizing files
import shutil #Copy, move, delete and rename files
shutil.copy(source, destination) #kopier en fil
shutil.copytree(source, destination) #kopier hele mappe med undermapper
shutil.move(source, destination)

#Kapitel 10 Debugging
raise Exception('Error message')
import traceback
traceback.format_exc() #Gemmer traceback
assert name == 'value','Returntext if false'

#kapitel 11 Web scraping
import webbrowser # muliggør at åbne links med specifike browsers
webbrowser.open('google.dk')
import requests