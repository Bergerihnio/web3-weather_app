import requests, sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

def scrap_behavior():
    r = requests.get('https://pogoda.interia.pl/prognoza-dlugoterminowa-blonie,cId,1689')
    if r.status_code != 200:
        return("DUPA")
        return
    
    soup = BeautifulSoup(r.content, 'html.parser')
    find_behave = soup.find_all('div', class_='weather-currently-icon ico-6')

    #Find title ind find_behave
    for title in find_behave:
        title_text = title.get('title')

    match title_text:
        case 'Słonecznie':
            return('☀️')
        case 'Przeważnie słonecznie':
            return('🌤️')
        case 'Częściowo słonecznie':
            return('⛅')
        case 'Przejściowe zachmurzenie':
            return('🌥️')
        case 'Zachmurzenie duże':
            return('☁️')
        case 'Pochmurno':
            return('🌫️')
        case 'Deszcz':
            return('🌧️')
        case 'Przelotne opady':
            return('🌦️')
        case 'Burze z piorunami':
            return('⛈️')
        case 'Częściowo słonecznie i burze z piorunami':
            return('🌦️⛈️')
        case _:
            return('Nieznany opis pogody')



if __name__ == '__main__':
    scrap_behavior()