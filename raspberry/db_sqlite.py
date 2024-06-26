import sqlite3

# Tworzenie połączenia z bazą danych
conn = sqlite3.connect('temperatures.db')
c = conn.cursor()

# Tworzenie tabeli
c.execute('''CREATE TABLE IF NOT EXISTS temperatures
             (temperature REAL,
              time TEXT DEFAULT (time('now', 'localtime')),
              date TEXT DEFAULT (date('now')))''')


# c.execute("SELECT temperature FROM temperatures ORDER BY date DESC")

c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC")

last_hour_temp = c.fetchone()


print(last_hour_temp[0], last_hour_temp[1])

# rows = c.fetchall()


# for row in rows:
#     print(row[0])

# c.execute("SELECT * FROM temperatures")
# print(c.fetchall())

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


