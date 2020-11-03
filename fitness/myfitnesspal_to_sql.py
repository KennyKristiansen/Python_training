import sqlite3
import os
import csv
import re

database_name = 'fitness.sqlite'

try:
    connection = sqlite3.connect(database=database_name, isolation_level=None)
    print(f'connected to {database_name}')
except sqlite3.Error as e:
    print(f'Could not connect to database. Error: {e}')

dir_of_mfp_files = r'C:\Users\kenny\Desktop\Fitness\Myfitnesspal files'
os.chdir(dir_of_mfp_files)
myfitnesspal_files_folder = os.listdir(dir_of_mfp_files)


for file in myfitnesspal_files_folder:
    with open(file, newline='', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quoting=0)
        first_line = True
        for row in reader:
            filename = str(file.split('-')[0])
            if str(file).startswith('Motionsoversigt'):
                if first_line:
                    # noinspection PyUnboundLocalVariable
                    categories = ['Dato', 'Dyrk motion', 'Type', 'Øvelseskalorier', 'Minutters motion', 'Indstillinger', 'Antal gentagelser pr. sæt', 'Kilogram', 'Skridt', 'export_headers.note']
                    print(filename + '(%s)' % ', '.join(categories))
                    connection.execute('CREATE TABLE IF NOT EXISTS ' + filename + '(%s)' % ', '.join(categories))
                    print(row)
                else:
                    pass
            if str(file).startswith('Næringsoversigt'):
                if first_line:
                    print(row)
                else:
                    pass
            if str(file).startswith('Oversigt'):
                if first_line:
                    print(row)
                else:
                    pass
            first_line = False
