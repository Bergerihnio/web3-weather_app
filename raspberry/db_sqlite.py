import sqlite3
from datetime import date

# # Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
c = conn.cursor()

# # Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS weather
            (temperature REAL,
            humidity INTEGER,
            pressure INTEGER,
            wind INTEGER,
            rain INTEGER,
            emoji INTEGER,
            cloudy INTEGER,   
            sunrise  TEXT DATETIME,
            sunset TEXT DATETIME,       
            time TEXT DEFAULT (time('now', 'localtime')),
            date TEXT DEFAULT (date('now')))''')

# # Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close()


def get_stats_emoji():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()

    data =  f'{date.today()}'
    time_start = '10:00:00'
    time_end = '20:00:00'

    c.execute("SELECT emoji FROM temperatures WHERE date= (?) AND time BETWEEN ? AND ?",
              (data, time_start, time_end))
    rows = c.fetchall()

    rows_list = []
    for row in rows:
        rows_list.append(row[0])
    
    conn.close()

    average_emoji = the_most_occurate(rows_list)
    
    return average_emoji

def the_most_occurate(emoji_list):
    counter = 0
    for element in emoji_list:
        current = emoji_list.count(element)
        if (current > counter):
            counter = current
            the_most_occ = [element]

        elif current == counter:
            if element not in the_most_occ:
                the_most_occ.append(element)
    return the_most_occ

# print(the_most_occurate(emoji_list))

print(get_stats_emoji())

