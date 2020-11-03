#! python3
# Price_scraper.py - Scrape desired sites for prices of wanted items

import bs4
import datetime
import re
import requests
import sqlite3

# example                {results: {"Amazon_1" : ["Printer ink", "5 $", "4,2 of 5 stars", "WWW.Amazon.Com/Printer]}}
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


def site_links(complete_search_link):
    site_regex = re.compile(r'^(www\.|http:\/\/www\.|https:\/\/www\.|https:\/\/)(\w+)(\.\w+)(.*)')
    # Example: http://www.searchsite.de/s?k=
    # Full match    = http://www.search_site.de/s?k=
    # Group 1       = http://www.
    # Group 2       = search_site
    # Group 3       = .de
    # Group 4       = /s?k=
    link_regex = site_regex.search(complete_search_link)
    site_link = str(''.join(link_regex.group(1, 2, 3)))
    search_link = str(link_regex.group(0))
    service_name = str(link_regex.group(2))
    return site_link, search_link, service_name

connection = sqlite3.connect(database='item_database.db', isolation_level=None)
connection.execute('''CREATE TABLE IF NOT EXISTS items(item_name text, price real, rating real, link text, time_stamp text, site)''')
cursor = connection.cursor()


class Item:
    def __init__(self):         # initiation set values
        self.name = ''          # text
        self.price = 0          # float
        self.rating = 0         # float
        self.link = ''          # text
        self.timestamp = ''     # text
        self.site = ''          # text

    def print_item(self):
        print('---------------------------------')
        print(f'Name: {self.name}')
        print(f'Price: {self.price}')
        print(f'Rating: {self.rating}')
        print(f'Link: {self.link}')
        print(f'Timestamp: {self.timestamp}')
        print('---------------------------------')
        print('')

    def update_database(self):
        values = (self.name, self.price, self.rating, self.link, self.timestamp, self.site)  # values to add to database
        cursor.execute('insert into items values (?, ?, ?, ?, ?, ?)', values)                # adding to database


def currency_convert(price):
    price = str(price).replace('\n', '')    # replaces newline with empty space, for correct regex
    price_regex = re.compile(r'([a-zA-Z0-9,.]*)(?=(([,.])\d+))|(^\d*\d)')  # regex to identify numbers
    # example price = 10.000,95
    # full match will match until . or , = 10.000
    # group 2 will match everything after the last . or , if followed by 2 digits = ,95
    # group 3 will match the delimiter = , or .
    price_reg = price_regex.search(price)  # regex compiles the price
    first_price = price_reg.group(0).replace(',', '').replace('.', '')  # removes redundant . and ,     10.000 -> 10000
    last_price = price_reg.group(2).replace(',', '').replace('.', '')   # removes redundant . and ,         .95 -> 95
    total_price = float(first_price + '.' + last_price)                 # combines prices

    # Converts from given currency to DKK
    # TODO convert if's to a dictionary
    # TODO automatic update of currency value
    if price.endswith('€') is True:
        total_price = round(float(first_price + '.' + last_price) * float('7.46565'), 0)
    if price.endswith('$') is True:
        total_price = round(float(first_price + '.' + last_price) * float('6.83'), 0)
    if price.endswith('£') is True:
        total_price = round(float(first_price + '.' + last_price) * float('8.5'), 0)
    if price.startswith('£') is True:
        total_price = round(float(first_price + '.' + last_price) * float('8.5'), 0)
    return total_price


# Extracts and converts the rating string to a single value
def rating_converter(rating):
    rating_regex = re.compile('[0-9.,/]+')
    rating_regex = rating_regex.search(rating)
    rating = rating_regex.group(0)
    return rating


# Returns the wanted page as a bs4 type parsed with lxml
def page_get(search, page_link):
    page_link = str(page_link)
    search = str(search)
    combine_link = page_link + search
    page_request = requests.get(combine_link, headers=header)
    page_content = page_request.content
    soup = bs4.BeautifulSoup(page_content, features="lxml")
    return soup


# header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'}
header = []


def amazon_price_get(search):
    page = site_links('http://www.amazon.de/s?k=')
    soup = page_get(search, page[1])
    results = 0
    bot_check = soup.find_all('title', attrs={'dir': 'ltr'})
    if len(bot_check) == 1:
        print(bot_check)
        print('bot detection active')
    for container in soup.find_all(class_="s-include-content-margin s-border-bottom s-latency-cf-section"):
        item = Item()
        item.site = page[2]
        # Try to find wanted information in all containers (items)
        try:
            item.name = (container.find('span', attrs={'class': 'a-size-medium a-color-base a-text-normal'})).text
            item.price = (container.find('span', attrs={'class': 'a-offscreen'})).text
            item.price = currency_convert(item.price)
            try:
                item.rating = (container.find('span', attrs={'class': 'a-icon-alt'})).text
                item.rating = rating_converter(item.rating)
            except AttributeError:
                # print('No rating available')
                pass
            item.link = page[1] + str(container.find('a', attrs={'a-link-normal a-text-normal'}).get('href'))
            item.timestamp = datetime.datetime.now()
            results += 1
            item.update_database()
        except AttributeError:
            pass

    print(f'{results} results found at {page[2]}')


def newegg_price_get(search):
    page = site_links('https://www.newegg.com/global/uk-en/p/pl?d=')
    soup = page_get(search, page[1])
    result = 0
    for container in soup.find_all(class_='item-container'):
        item = Item()
        item.site = page[2]
        try:
            item.name = (container.find('a', attrs={'class': 'item-title'})).text
            item.price = currency_convert((container.find('li', attrs={'class': 'price-current'})).text)
            item.price = item.price * 1.20
            item.rating = rating_converter(str(container.find('a', attrs={'class': 'item-rating'}).get('title')))
            item.link = container.find('a', attrs={'item-img'}).get('href')
            item.timestamp = datetime.datetime.now()
            result += 1
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')


def compumail_price_get(search):
    page = site_links('https://compumail.dk/da/search?q=')
    soup = page_get(search, page[1])
    result = 0

    for container in soup.find_all(class_='product-grid-item-content'):
        item = Item()
        item.site = page[2]
        try:
            item.name = (container.find('a', attrs={'class': 'product-link'})).get('data-product-name')
            item.price = currency_convert((container.find('span', attrs={'class': 'price'})).text)
            item.link = page[1] + str(container.find('a', attrs={'product-link'}).get('href'))
            # item.rating = Site has no rating system
            item.timestamp = datetime.datetime.now()
            result += 1
            # item.print_item()
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')



def proshop_price_get(search):
    page = site_links('https://www.proshop.dk/?s=')
    soup = page_get(search, page[1])
    result = 0

    for container in soup.find_all(class_='product-grid-item-content'):
        item = Item()
        item.site = page[2]
        try:
            item.name = (container.find('a', attrs={'class': 'product-link'})).get('data-product-name')
            item.price = currency_convert((container.find('span', attrs={'class': 'price'})).text)
            item.link = page[1] + str(container.find('a', attrs={'product-link'}).get('href'))
            # item.rating = Site has no rating system
            item.timestamp = datetime.datetime.now()
            result += 1
            # item.print_item()
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')


def elgiganten_price_get(search):
    page = site_links('https://www.elgiganten.dk/search?SearchTerm=')
    soup = page_get(search, page[1])
    result = 0

    for container in soup.find_all(class_='mini-product-content'):
        item = Item()
        item.site = page[2]
        try:
            item.name = (container.find('a', attrs={'class': 'product-image-link'})).get('title')
            item.price = str((container.find('div', attrs={'class': 'product-price'})).text).replace(' ', '')
            item.link = str(container.find('a', attrs={'product-image-link'}).get('href'))
            # item.rating = Site has no rating system
            item.timestamp = datetime.datetime.now()
            result += 1
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')


def happii_price_get(search):
    page = site_links('https://www.happii.dk/?s=')
    soup = page_get(search, page[1])
    result = 0

    for container in soup.find_all(class_='row toggle'):
        item = Item()
        item.site = page[2]
        try:
            item.name = container.find('h2', attrs={'product-display-name': ''}).text
            item.price = currency_convert(container.find('span', attrs={'class': 'site-currency-lg'}).text)
            item.link = page[1] + str(container.find('a', attrs={'site-product-link'}).get('href'))
            item.timestamp = datetime.datetime.now()
            result += 1
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')


def foeniks_price_get(search):
    page = site_links('https://www.fcomputer.dk/search?q=')
    soup = page_get(search, page[1])
    result = 0

    for container in soup.find_all(class_='inner-query-product-wrapper'):
        item = Item()
        item.site = page[2]
        try:
            item.name = container.find('span', attrs={'class': 'title'}).text
            item.price = currency_convert(str((container.find('div', attrs={'class': 'product-price'})).text).replace('	', '').replace(',-', '.00'))
            item.link = page[1] + str(container.find('a').get('href'))
            # print(item.name, item.price, item.link)
            item.timestamp = datetime.datetime.now()
            result += 1
            item.update_database()

        except AttributeError:
            continue

    print(f'{result} results found at {page[2]}')

# Used for parsing the search input, into searchable format.
# Defined for ability to easily edibility


def search_string_parser(search_string):
    search = str(search_string).replace(' ', '+')
    return search


# Runs the search on all available sites

def return_best_price(search_string):
    search_string_parsed = str(search_string).replace(' ', '%')  # seperates string into seperate searchable words for SQLite3
    for row in cursor.execute('SELECT "item_name", "price", "link", "site", item_name FROM items WHERE item_name Like ? ORDER BY price LIMIT 1', ('%'+search_string_parsed+'%',)):
        print(f'Item {search_string} found at {row[3]} for {int(row[1])} DKK - LINK: {row[2]}')


def service_run(search_string):
    search_string_parsed = search_string_parser(search_string)
    if True:
        compumail_price_get(search_string_parsed)
        amazon_price_get(search_string_parsed)
        newegg_price_get(search_string_parsed)
        elgiganten_price_get(search_string_parsed)
        happii_price_get(search_string_parsed)
        foeniks_price_get(search_string_parsed)
    return_best_price(search_string)


search_name = "nzxt h510"
service_run(search_name)
connection.close()
