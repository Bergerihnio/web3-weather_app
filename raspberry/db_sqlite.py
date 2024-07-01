import sqlite3
import weather_behavior

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
c = conn.cursor()

# Tworzenie tabeli
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

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close()


