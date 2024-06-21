import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
import thermometer
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
CORS(app)

# Konfiguracja harmonogramu zadań
scheduler = BackgroundScheduler()
scheduler.start()

# Funkcja do zapisywania temperatury do bazy danych
def save_to_db(temperature): 
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO temperatures (temperature) VALUES (?)", (temperature,))
    conn.commit()
    conn.close()

# Zadanie do pobierania i zapisywania temperatury co minute
@scheduler.scheduled_job('interval', seconds=10)
def save_schedule_job():
    temperature = thermometer.get_temperature()
    save_to_db(temperature)

@app.route('/data', methods=['GET'])
def get_data():
    temperature = thermometer.get_temperature()
    return jsonify({'temperature': f'{temperature:.2f}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
