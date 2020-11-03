import openpyxl
import os
import re
import requests
import sqlite3

movie_regex = re.compile(r'(.+)\((\d{4})\)')
series_regex = re.compile(r'(^.+?(?=\(\d{4}\)$|$))')

connection = sqlite3.connect(database='server_database.db', isolation_level=None)
connection.execute('''CREATE TABLE IF NOT EXISTS movies(title text)''')
connection.execute('''CREATE TABLE IF NOT EXISTS series(title text)''')

cursor = connection.cursor()

drive = r'D:\Movies'

try:
    movies_list = os.listdir(drive)
    series_list = os.listdir(drive)
except FileNotFoundError:
    raise Exception(f'Location ({drive}) not found.')

class Omdb:
    def __init__(self):
        self.api_key = 'a86a0ee2'
        self.title = ''
        self.year = ''
        self.type = ''

    def request(self):
        omdb_request_link = f'http://www.omdbapi.com/?t={self.title}&y={self.year}&type={self.type}&apikey={self.api_key}'
        request = requests.get(str(omdb_request_link)).json()
        return request


class Progress:

    def __init__(self):
        self.min = 0
        self.max = 0
        self.current = 0
        self.progress = 1

    def update(self):

        increments = float(int(self.max) - int(self.min)) / 100
        compare = self.progress * increments
        while self.current > compare:
            self.progress += 1
            compare = self.progress * increments
            percentage = compare / self.max * 100
            print(str(round(percentage, 2)) + ' %', end="\r")

        else:
            pass


try:
    os.chdir(r'D:/')
    wb = openpyxl.load_workbook('databases.xlsx')
except FileNotFoundError:
    wb = openpyxl.Workbook()


def database_update():
    progress = Progress()
    total_requests = 0
    updated = 0
    added = 0
    file_list = len(movies_list)
    progress.min = 0
    progress.max = file_list

    for i in range(file_list):
        progress.current += 1
        total_requests += 1
        req = Omdb()  # start instance of class omdb
        movie_information_regex = movie_regex.findall(movies_list[i])
        req.title = movie_information_regex[0][0]
        req.year = movie_information_regex[0][1]
        req.type = 'movie'
        request_json = req.request()
        v_list = []
        for k, v in request_json.items():
            k = str(k)
            v_list.append(str(v))

            try:
                connection.execute('ALTER TABLE movies ADD COLUMN %s TEXT' % k)
            except sqlite3.OperationalError:
                pass
        columns = len(tuple(connection.execute('PRAGMA table_info(series)')))
        while columns > len(v_list):
            v_list.append('N/A')  # list not long enough, is 25 should be 26
        v_list_title = (v_list[0],)

        # Check if title exists, else add it
        file = connection.execute('SELECT * FROM movies WHERE title=(?)', v_list_title)  # find rows containing title
        title_exists = False
        for row in file:
            title_exists = True
        if title_exists is True:
            title = request_json.get('Title')
            connection.execute('DELETE FROM movies WHERE title=(?)', v_list_title)
            connection.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                               ' ?, ?, ?, ?)', v_list)
            updated += 1

        elif title_exists is False:
            connection.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                               ' ?, ?, ?, ?)', v_list)
            added += 1

        progress.update()
    print(f'Requested files: {total_requests}')
    print(f'Movies updated: {updated}')
    print(f'Movies added: {added}')
    print(f'Not parsed: {total_requests - (added + updated)}')


def database_update_series():
    progress = Progress()
    total_requests = 0
    updated = 0
    added = 0
    file_list = len(series_list)
    progress.min = 0
    progress.max = file_list

    for i in range(file_list):
        progress.current += 1
        total_requests += 1
        req = Omdb()  # start instance of class omdb
        movie_information_regex = series_regex.findall(series_list[i])
        req.title = movie_information_regex[0]
        req.year = movie_information_regex[0]
        req.type = 'series'
        request_json = req.request()
        v_list = []
        for k, v in request_json.items():
            k = str(k)
            v_list.append(str(v))

            try:
                connection.execute('ALTER TABLE series ADD COLUMN %s TEXT' % k)
            except sqlite3.OperationalError:
                pass

        columns = len(tuple(connection.execute('PRAGMA table_info(series)')))
        while columns > len(v_list):
            v_list.append('N/A')  # list not long enough, is 25 should be 26
        v_list_title = (v_list[0],)

        # Check if title exists, else add it
        file = connection.execute('SELECT * FROM series WHERE title=(?)', v_list_title)  # find rows containing title
        title_exists = False
        for row in file:
            title_exists = True
        if title_exists is True:
            title = request_json.get('Title')
            connection.execute('DELETE FROM series WHERE title=(?)', v_list_title)
            connection.execute('INSERT INTO series VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                               ' ?)', v_list)
            updated += 1

        elif title_exists is False:
            connection.execute('INSERT INTO series VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                               ' ?)', v_list)
            added += 1

        progress.update()
    print(f'Requested files: {total_requests}')
    print(f'Series updated: {updated}')
    print(f'Series added: {added}')
    print(f'Not parsed: {total_requests - (added + updated)}')


database_update()
database_update_series()
wb.save('database.xlsx')






