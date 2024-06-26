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
@scheduler.scheduled_job('interval', minutes=10)
def save_schedule_job():
    temperature = thermometer.get_temperature()
    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation = web_scrapping.scrap_soup()

    save_to_db(interia_temperature)


# Funkcja do zapisywania temperatury do bazy danych
def save_to_db(interia_temperature): 
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO temperatures (temperature) VALUES (?)", (interia_temperature[:2],))

    conn.commit()
    conn.close()

def last_hour():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature FROM temperatures ORDER BY date DESC")
    rows = c.fetchall()

    last_hour_temp = rows[0][0]

    conn.commit()
    conn.close()

    return last_hour_temp
    

@app.route('/data', methods=['GET'])
def get_data():
    temperature = thermometer.get_temperature()

    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation = web_scrapping.scrap_soup()

    last_hour_temp = last_hour()

    return jsonify({
        'temperature': f'{temperature:.2f}',
        'interia_temperature': f'{interia_temperature[:2]}',
        'interia_pressure_hPa': pressure,
        'interia_wind_speed_km_h': wind,
        'interia_sunrise_time': sunrise,
        'interia_sunset_time': sunset,
        'humidity': humidity,
        'rain_precipitation': rain_precipitation,
        'Last_hour_temperature': last_hour_temp
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)