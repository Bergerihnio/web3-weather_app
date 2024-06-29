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

def get_data_sql(offset):
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, time FROM temperatures ORDER BY date DESC, time DESC LIMIT 1 OFFSET (?)", (offset,))
    data = c.fetchone()
    
    temperature, time = data

    return temperature, time
    

@app.route('/data', methods=['GET'])
def get_data():
    temperature = thermometer.get_temperature()

    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation = web_scrapping.scrap_soup()

    last_hour_temp, last_hour_time = get_data_sql(0)

    last_second_hour_temp, last_second_hour_time = get_data_sql(1)

    last_fourth_hour_temp, last_fourth_hour_time = get_data_sql(3)

    last_seventh_hour_temp, last_seventh_hour_time = get_data_sql(6)

    last_10th_hour_temp, last_10th_hour_time = get_data_sql(9)

    # last_13th_hour_temp, last_13th_hour_time = get_data_sql(12)

    data = {
        'temperature': f'{temperature}',
        'interia_temperature': f'{interia_temperature[:2]}',
        'interia_pressure_hPa': pressure,
        'interia_wind_speed_km_h': wind,
        'interia_sunrise_time': sunrise,
        'interia_sunset_time': sunset,
        'humidity_in_percentage': humidity, 
        'rain_precipitation_percentage': rain_precipitation,
        'last_hour_data': {'time': f'{last_hour_time}', 'temp': f'{last_hour_temp}'},
        'last_second_hour_data': {'time': f'{last_second_hour_time}', 'temp': f'{last_second_hour_temp}'},
        'last_fourth_hour_data': {'time': f'{last_fourth_hour_temp}', 'temp': f'{last_fourth_hour_time}'},
        'last_seventh_hour_data': {'time': f'{last_seventh_hour_temp}', 'temp': f'{last_seventh_hour_time}'},
        # 'last_10th_hour_data': {'time': f'{last_10th_hour_temp}', 'temp': f'{last_10th_hour_time}'},
        # 'last_13th_hour_data': {'time': f'{last_13th_hour_temp}', 'temp': f'{last_13th_hour_time}'}
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    