#! python3
# QuizGenerator.py Creates quizzes with questions and answers in
# a random order

import random, pprint

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

statelist = list(capitals.keys())
capitallist = list(capitals.values())
right_answers = []
for i in range(35):
    wrong = []
    wrongs = []
    question = statelist[random.randrange(50-i)]
    print(str(i+1) + '. What is capital of ' + question)
    right = capitals[question]
    capitallist.remove(right)
    for a in range(3):
        wrong = capitallist[random.randrange(49-i)]
        if wrong not in wrongs:
            wrongs.append(wrong)
        else:
            continue
    wrongs.append(right)
    for b in range(len(wrongs)):
       answers = wrongs[random.randrange(len(wrongs))]
       print('ABCD'[b] + '. '  + answers)
       wrongs.remove(answers)
       if answers == right:
           right_answers.append(str(i + 1) + ': ' + 'ABCD'[b])

    statelist.remove(question)
pprint.pprint(right_answers)
