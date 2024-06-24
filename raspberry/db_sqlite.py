import sqlite3

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS temperatures
             (temperature REAL,
              time TEXT DEFAULT (time('now', 'localtime')),
              date TEXT DEFAULT (date('now')))''')

c.execute("SELECT temperature FROM temperatures ORDER BY date DESC")

rows = c.fetchall()

for row in rows:
    print(row[0])

# c.execute("SELECT * FROM temperatures")
# print(c.fetchall())

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


