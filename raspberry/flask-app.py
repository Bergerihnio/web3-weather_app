import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
import thermometer
import web_scrapping
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# Konfiguracja harmonogramu zadań
scheduler = BackgroundScheduler()
scheduler.start()


# Zadanie do pobierania i zapisywania temperatury co minute
@scheduler.scheduled_job('cron', minute='0')
def save_schedule_job():
    temperature = thermometer.get_temperature()
    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation = web_scrapping.scrap_soup()

    save_to_db(interia_temperature, humidity, pressure, sunrise, sunset, wind, rain_precipitation)


# Funkcja do zapisywania temperatury do bazy danych
def save_to_db(interia_temperature, humidity, pressure, sunrise, sunset, wind, rain_precipitation): 
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO temperatures (temperature, humidity, pressure, sunrise, sunset, wind, rain) VALUES (?, ?, ?, ?, ?, ?, ?)", (interia_temperature[:2], humidity, pressure, sunrise, sunset, wind, rain_precipitation))

    conn.commit()
    conn.close()

def last_hour():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC")
    last_hour_data = c.fetchone()

    last_hour_temp = last_hour_data[0]
    last_hour_time = last_hour_data[1]

    conn.commit()
    conn.close()

    return last_hour_temp, last_hour_time

def last_second_hour():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC LIMIT 1 OFFSET 1")
    last_second_hour_data = c.fetchone()

    last_second_hour_temp = last_second_hour_data[0]
    last_second_hour_time = last_second_hour_data[1]

    conn.commit()
    conn.close()

    return last_second_hour_temp, last_second_hour_time
    

@app.route('/data', methods=['GET'])
def get_data():
    temperature = thermometer.get_temperature()

    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation = web_scrapping.scrap_soup()

    last_hour_temp, last_hour_time = last_hour()

    last_second_hour_temp, last_second_hour_time = last_second_hour()

    data = {
        'temperature': f'{temperature}',
        'interia_temperature': f'{interia_temperature[:2]}',
        'interia_pressure_hPa': pressure,
        'interia_wind_speed_km_h': wind,
        'interia_sunrise_time': sunrise,
        'interia_sunset_time': sunset,
        'humidity_in_percentage': humidity, #'humidity_in_perentage': humidity,
        'rain_precipitation_percentage': rain_precipitation,
        'last_hour_data': {'time': f'{last_hour_time}', 'temp': f'{last_hour_temp}'},
        'last_second_hour_data': {'time': f'{last_second_hour_time}', 'temp': f'{last_second_hour_temp}'}
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    