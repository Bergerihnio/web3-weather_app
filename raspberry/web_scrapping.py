import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')


def scrap_soup():
    r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
    if r.status_code != 200:
        print("DUPA")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    find_temp = soup.find('div', class_='weather-currently-temp-strict')
    find_wind_pres = soup.find_all('span', class_='weather-currently-details-value')
    find_sunrise = soup.find('span', class_='weather-currently-info-sunrise')
    find_sunset = soup.find('span', class_='weather-currently-info-sunset')

    interia_temp = temp(find_temp)
    interia_sunrise, interia_sunset = sun(find_sunrise, find_sunset)
    interia_pressure, interia_wind = find(find_wind_pres)

    humidity = scrap_weather_com()
    

    return interia_temp, interia_pressure, interia_wind, interia_sunrise, interia_sunset, humidity

def temp(find_temp):
    interia_temp = find_temp.get_text(strip=True)
    return interia_temp

def find(find_wind_pres):
    interia_wind = find_wind_pres[2].get_text(strip=True)
    interia_wind = f'{interia_wind[:2]}'
    
    interia_pressure = find_wind_pres[1].get_text(strip=True)
    interia_pressure = f'{interia_pressure[:4]}'

    return interia_pressure, interia_wind


def sun(find_sunrise, find_sunset):
    interia_sunrise = find_sunrise.get_text(strip=True)
    interia_sunset = find_sunset.get_text(strip=True)

    return interia_sunrise, interia_sunset

def scrap_weather_com():
    r = requests.get('https://weather.com/weather/today/l/070de30acaa6420327d5cecbb61fb43b720bb86826506460b7a73d09ab0096aa')
    
    if r.status_code != 200:
        print("DUPA")
        return
    
    soup = BeautifulSoup(r.content, 'html.parser')
    find_humidity = soup.find('span', {'data-testid': 'PercentageValue'})
    humidity = find_humidity.get_text(strip=True)

    # find_chance_of_precipitation = soup.find('span', class_='Column--precip--3JCDO')
    # chance_of_precipitation = find_chance_of_precipitation.get_text(strip=True)
    # print(chance_of_precipitation)

    return humidity
    

if __name__ == '__main__':
    scrap_soup()

