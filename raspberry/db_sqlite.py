import sqlite3

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS temperatures
             (temperature REAL,
              humidity INTEGER,
              pressure INTEGER,
              sunrise  TEXT DATETIME,
              sunset TEXT DATETIME,
              wind INTEGER,
              rain INTEGER,        
              time TEXT DEFAULT (time('now', 'localtime')),
              date TEXT DEFAULT (date('now')))''')


# c.execute("SELECT temperature FROM temperatures ORDER BY date DESC")

# c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC")

# last_hour_temp = c.fetchone()


# print(last_hour_temp[0], last_hour_temp[1])

def get_data_sql(offset):
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC LIMIT 1 OFFSET (?)", (offset,))
    data = c.fetchone()
    
    temperature, time = data

    return temperature, time


first_temp, first_time = get_data_sql(1)

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


