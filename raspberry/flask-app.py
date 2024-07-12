import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS
import datetime, web_scrapping, median, thermometer, weather_behavior, median_emoji
from apscheduler.schedulers.background import BackgroundScheduler
from colorama import Fore

app = Flask(__name__)
CORS(app)

# Konfiguracja harmonogramu zadań
scheduler = BackgroundScheduler()
scheduler.start()

i = 0

# Zadanie do pobierania i zapisywania temperatury o równej godzinie np. 17:00
@scheduler.scheduled_job('cron', minute='0')
def save_schedule_job():
    global i
    temperature = thermometer.get_temperature()
    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation, cloudy = web_scrapping.scrap_soup()

    emoji = weather_behavior.scrap_behavior()

    save_to_db(interia_temperature, humidity, pressure, sunrise,
               sunset, wind, rain_precipitation, cloudy, emoji)
    i += 1

    print(Fore.GREEN + f'Zapisano pomyślnie po raz {i}')


@scheduler.scheduled_job('cron', minute='1', hour='20')
def insert_schedule_job():
    median.insert_median()
    print(Fore.GREEN + 'Weather conditions successfully recorded')


# Funkcja do zapisywania temperatury do bazy danych
def save_to_db(interia_temperature, humidity, pressure, sunrise, sunset, wind, rain_precipitation, cloudy, emoji):
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("INSERT INTO temperatures (temperature, humidity, pressure, sunrise, sunset, wind, rain, cloudy, emoji) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (interia_temperature[:2], humidity, pressure, sunrise, sunset, wind, rain_precipitation, cloudy, emoji))

    conn.commit()
    conn.close()


def get_data_sql(offset):
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()
    c.execute("SELECT temperature, rain, time, emoji FROM temperatures ORDER BY date DESC, time DESC LIMIT 1 OFFSET (?)", (offset,))
    data = c.fetchone()

    temperature, rain, time, emoji = data

    conn.commit()
    conn.close()

    return temperature, rain, time, emoji


def get_stats_sql(offset):
    median_temp = median.get_stats_sql(offset)
    median_temp, date, weather = median_temp

    unmutable_date = date  # -> 2024-06-26
    date = date[5:10]  # -> 06-26
    month = date[:2]  # -> 06
    day = date[3:5]  # -> 26

    if month.startswith('0'):
        month = month[1:]

    month = int(month)

    list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month_word = list[month-1]

    date_obj = datetime.datetime.strptime(unmutable_date, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%A')

    return median_temp, day_of_week, month_word, unmutable_date, weather


@app.route('/data', methods=['GET'])
def get_data():
    temperature = thermometer.get_temperature()

    emoji = weather_behavior.scrap_behavior()

    interia_temperature, pressure, wind, sunrise, sunset, humidity, rain_precipitation, cloudy = web_scrapping.scrap_soup()

    last_hour_temp, last_hour_rain, last_hour_time, last_hour_emoji = get_data_sql(0)

    last_second_hour_temp, last_second_hour_rain, last_second_hour_time, last_second_hour_emoji = get_data_sql(1)

    last_fourth_hour_temp, last_fourth_hour_rain, last_fourth_hour_time, last_fourth_hour_emoji = get_data_sql(3)

    last_seventh_hour_temp, last_seventh_hour_rain, last_seventh_hour_time, last_seventh_hour_emoji = get_data_sql(6)

    last_10th_hour_temp, last_10th_hour_rain, last_10th_hour_time, last_10th_hour_emoji = get_data_sql(9)

    last_13th_hour_temp, last_13th_hour_rain, last_13th_hour_time, last_13th_hour_emoji = get_data_sql(12)

    last_median_temp, last_median_day_of_week, last_median_month_word, last_median_unmutable_date, last_median_weather_emoji = get_stats_sql(0)

    last_second_median_temp, last_second_median_day_of_week, last_second_median_month_word, last_second_median_unmutable_date, last_second_median_weather_emoji = get_stats_sql(1)

    last_third_median_temp, last_third_median_day_of_week, last_third_median_month_word, last_third_median_unmutable_date, last_third_median_weather_emoji = get_stats_sql(2)

    last_fourth_median_temp, last_fourth_median_day_of_week, last_fourth_median_month_word, last_fourth_median_unmutable_date, last_fourth_median_weather_emoji = get_stats_sql(3)

    last_fifth_median_temp, last_fifth_median_day_of_week, last_fifth_median_month_word, last_fifth_median_unmutable_date, last_fifth_median_weather_emoji = get_stats_sql(4)


    data = {
        'temperature': f'{temperature}',
        'interia_temperature': f'{interia_temperature[:2]}',
        'interia_pressure_hPa': pressure,
        'interia_wind_speed_km_h': wind,
        'interia_sunrise_time': sunrise,
        'interia_sunset_time': sunset,
        'humidity_in_percentage': humidity,
        'rain_precipitation_percentage': rain_precipitation,

        'last_hour_data': {'time': f'{last_hour_time}', 'temp': f'{last_hour_temp}', 'rain': f'{last_hour_rain}', 'emoji': last_hour_emoji},
        'last_second_hour_data': {'time': f'{last_second_hour_time}', 'temp': f'{last_second_hour_temp}', 'rain': f'{last_second_hour_rain}', 'emoji': last_second_hour_emoji},
        'last_fourth_hour_data': {'time': f'{last_fourth_hour_time}', 'temp': f'{last_fourth_hour_temp}', 'rain': f'{last_fourth_hour_rain}', 'emoji': last_fourth_hour_emoji},
        'last_seventh_hour_data': {'time': f'{last_seventh_hour_time}', 'temp': f'{last_seventh_hour_temp}', 'rain': f'{last_seventh_hour_rain}', 'emoji': last_seventh_hour_emoji},
        'last_10th_hour_data': {'time': f'{last_10th_hour_time}', 'temp': f'{last_10th_hour_temp}', 'rain': f'{last_10th_hour_rain}', 'emoji': last_10th_hour_emoji},
        'last_13th_hour_data': {'time': f'{last_13th_hour_time}', 'temp': f'{last_13th_hour_temp}', 'rain': f'{last_13th_hour_rain}', 'emoji': last_13th_hour_emoji},

        'last_median_temp': {'median_temp': f'{last_median_temp}', 'date': f'{last_median_unmutable_date}', 'day': f'{last_median_day_of_week}', 'month': f'{last_median_month_word}', 'median_emoji': f'{last_median_weather_emoji}'},
        'last_second_median_temp': {'median_temp': f'{last_second_median_temp}', 'date': f'{last_second_median_unmutable_date}', 'day': f'{last_second_median_day_of_week}', 'month': f'{last_second_median_month_word}', 'median_emoji': f'{last_second_median_weather_emoji}'},
        'last_third_median_temp': {'median_temp': f'{last_third_median_temp}', 'date': f'{last_third_median_unmutable_date}', 'day': f'{last_third_median_day_of_week}', 'month': f'{last_third_median_month_word}', 'median_emoji': f'{last_third_median_weather_emoji}'},
        'last_fourth_median_temp': {'median_temp': f'{last_fourth_median_temp}', 'date': f'{last_fourth_median_unmutable_date}', 'day': f'{last_fourth_median_day_of_week}', 'month': f'{last_fourth_median_month_word}', 'median_emoji': f'{last_fourth_median_weather_emoji}'},
        'last_fifth_median_temp': {'median_temp': f'{last_fifth_median_temp}', 'date': f'{last_fifth_median_unmutable_date}', 'day': f'{last_fifth_median_day_of_week}', 'month': f'{last_fifth_median_month_word}', 'median_emoji': f'{last_fifth_median_weather_emoji}'},
        'cloudy': cloudy,
        'emoji': emoji
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
