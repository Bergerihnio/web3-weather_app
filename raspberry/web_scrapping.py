import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')


def good_soup():
    r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
    if r.status_code == 200:
        r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find('div', class_='weather-currently-temp-strict')
        interia_temp = s.get_text(strip=True)
        # print(s.get_text(strip=True))
        return interia_temp
    else:
        print("DUPA")

if __name__ == '__main__':
    good_soup()