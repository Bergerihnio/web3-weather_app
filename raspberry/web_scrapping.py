import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')


def scrap_soup():
    r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
    if r.status_code != 200:
        print("DUPA")
        return
    
    r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')

    soup = BeautifulSoup(r.content, 'html.parser')
    find_temp = soup.find('div', class_='weather-currently-temp-strict')
    find_wind_pres = soup.find_all('span', class_='weather-currently-details-value')
    find_sunrise = soup.find('span', class_='weather-currently-info-sunrise')
    find_sunset = soup.find('span', class_='weather-currently-info-sunset')

    interia_temp = temp(find_temp)
    interia_sunrise, interia_sunset = sun(find_sunrise, find_sunset)
    interia_pressure, interia_wind = find(find_wind_pres)

    return interia_temp, interia_pressure, interia_wind, interia_sunrise, interia_sunset

def temp(find_temp):
    interia_temp = find_temp.get_text(strip=True)
    return interia_temp

def find(find_wind_pres):
    interia_wind = find_wind_pres[2].get_text(strip=True)
    interia_wind = f'{interia_wind[0] + interia_wind[1]}'
    
    interia_pressure = find_wind_pres[1].get_text(strip=True)
    interia_pressure = f'{interia_pressure[:4]}'

    return interia_pressure, interia_wind


def sun(find_sunrise, find_sunset):
    interia_sunrise = find_sunrise.get_text(strip=True)
    interia_sunset = find_sunset.get_text(strip=True)

    return interia_sunrise, interia_sunset

if __name__ == '__main__':
    scrap_soup()

