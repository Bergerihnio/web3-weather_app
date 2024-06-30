import sqlite3

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
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


def get_data_sql(offset):
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, humidity, time FROM temperatures ORDER BY date DESC, time DESC LIMIT 1 OFFSET (?)", (offset,))
    data = c.fetchone()
    
    temperature, humidity, time = data

    return temperature, humidity, time
    
print(get_data_sql(1))

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


