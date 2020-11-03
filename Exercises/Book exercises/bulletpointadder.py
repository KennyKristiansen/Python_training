import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
# print(len(lines))
linedel = []
for i in range(len(lines)):
    if str(lines[i]).startswith('1') is True:
        lines[i] = str(lines[i]).replace('1 ', '')
        lines[i] = ('Respondent: ' + str(lines[i]))
    if str(lines[i]).startswith('Respondent: ') is False:
        lines[i] = ('Kenny: ' + str(lines[i]))
for a in range(0, len(linedel)):

    b = linedel[a]
    del lines[b-a]



text = '\n'.join(lines)

pyperclip.copy(text)
print(text)


