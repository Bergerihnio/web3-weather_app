import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')

def good_soup(r):
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_='weather-currently-temp-strict')
    print(s.get_text(strip=True))


if r.status_code == 200:
    good_soup(r)
else:
    print('dupa')
