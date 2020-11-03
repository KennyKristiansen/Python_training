#! python3




#Site crawler
import requests, bs4
rec = requests.get('https://www.dk-kogebogen.dk/opskrifter/132/')
try:
    rec.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % exc)
souprec = bs4.BeautifulSoup(rec.text, features="html.parser")


#Informationfinder
titles = souprec.select('span')
dish = titles[0].getText()







