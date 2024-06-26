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

c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC")

last_hour_temp = c.fetchone()


print(last_hour_temp[0], last_hour_temp[1])


{
  "humidity_in_percentage": "50",
  "interia_pressure_hPa": "1014",
  "interia_sunrise_time": "04:18",
  "interia_sunset_time": "21:02",
  "interia_temperature": "26",
  "interia_wind_speed_km_h": "9 ",
  "last_hour_data": {
    "temp": "29.0",
    "time": "19:30:00"
  },
  "last_second_hour_data": {
    "temp": "29.0",
    "time": "18:30:00"
  },
  "rain_precipitation_percentage": "0",
  "temperature": "21.00"
}

# rows = c.fetchall()


# for row in rows:
#     print(row[0])

# c.execute("SELECT * FROM temperatures")
# print(c.fetchall())

# Zapisanie zmian
conn.commit()

# Zamknięcie połączenia
conn.close() 


