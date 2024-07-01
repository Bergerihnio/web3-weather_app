import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')


def scrap_soup():
    r = requests.get(
        'https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
    if r.status_code != 200:
        print("DUPA")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    find_temp = soup.find('div', class_='weather-currently-temp-strict')
    find_wind_pres = soup.find_all(
        'span', class_='weather-currently-details-value')
    find_sunrise = soup.find('span', class_='weather-currently-info-sunrise')
    find_sunset = soup.find('span', class_='weather-currently-info-sunset')

    interia_temp = temp(find_temp)
    interia_sunrise, interia_sunset = sun(find_sunrise, find_sunset)
    interia_pressure, interia_wind = find(find_wind_pres)

    humidity = scrap_weather_com()

    rain_precipitation = scrap_rain()

    cloudy = scrap_soup_details()

    return interia_temp, interia_pressure, interia_wind, interia_sunrise, interia_sunset, humidity, rain_precipitation, cloudy


def scrap_soup_details():
    r = requests.get(
        'https://pogoda.interia.pl/prognoza-szczegolowa-blonie,cId,1689')
    if r.status_code != 200:
        print("DUPA")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    find_cloudy = soup.find(
        'span', class_='entry-precipitation-value cloud-cover')
    cloudy = find_cloudy.get_text(strip=True)

    cloudy = cloudy.replace("%", "")

    return cloudy


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
    r = requests.get(
        'https://weather.com/weather/today/l/070de30acaa6420327d5cecbb61fb43b720bb86826506460b7a73d09ab0096aa')

    if r.status_code != 200:
        print("DUPA")
        return

    soup = BeautifulSoup(r.content, 'html.parser')
    find_humidity = soup.find('span', {'data-testid': 'PercentageValue'})
    humidity = find_humidity.get_text(strip=True)
    humidity = humidity.replace("%", "")

    return humidity


def scrap_rain():
    r = requests.get(
        'https://weather.com/weather/today/l/070de30acaa6420327d5cecbb61fb43b720bb86826506460b7a73d09ab0096aa')

    if r.status_code != 200:
        print("Błąd przy pobieraniu strony")
        return

    soup = BeautifulSoup(r.content, 'html.parser')

    all_spans = soup.find_all(
        'span', class_='Accessibility--visuallyHidden--H7O4p')

    for span in all_spans:
        if span.get_text(strip=True) == "Chance of Rain":
            # Pobierz tekst rodzica tego elementu (który zawiera '1%')
            rain_precipitation = span.parent.get_text(strip=True)
            rain_precipitation = rain_precipitation.replace(
                "Chance of Rain", "")
            rain_precipitation = rain_precipitation.replace("%", "")

        return rain_precipitation


if __name__ == '__main__':
    scrap_soup()
