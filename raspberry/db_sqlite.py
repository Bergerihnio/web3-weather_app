import sqlite3

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('weather.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS weather
             (temperature REAL,
              humidity INTEGER,
              pressure INTEGER,
              sunrise  TEXT DATETIME,
              sunset TEXT DATETIME,
              wind INTEGER,
              rain INTEGER,        
              time TEXT DEFAULT (time('now', 'localtime')),
              date TEXT DEFAULT (date('now')))''')


# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


