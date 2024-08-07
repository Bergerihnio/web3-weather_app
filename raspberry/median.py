import statistics
import sqlite3
from datetime import date
import median_emoji


def get_stats():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()

    data = f'{date.today()}'
    time_start = '10:00:00'
    time_end = '20:00:00'

    c.execute("SELECT temperature FROM temperatures WHERE date= (?) AND time BETWEEN ? AND ?",
              (data, time_start, time_end))
    rows = c.fetchall()

    rows_list = []
    for row in rows:
        rows_list.append(row[0])

    median_temp = statistics.median(rows_list)

    conn.close()

    return median_temp


def insert_median():
    conn = sqlite3.connect('statistics.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS statistics
                (median_temp REAL,
                weather TEXT,    
                date TEXT DEFAULT (date('now')))''')

    median_temp = get_stats()

    emoji_string = median_emoji.get_stats_emoji()

    c.execute("INSERT INTO statistics (median_temp, weather) VALUES (?, ?)", (median_temp, emoji_string))

    conn.commit()
    conn.close()


def get_stats_sql(offset):
    conn = sqlite3.connect('statistics.db')
    c = conn.cursor()
    c.execute(
        "SELECT median_temp, date, weather FROM statistics ORDER BY DATE DESC LIMIT 1 OFFSET (?)", (offset,))

    data = c.fetchone()

    median_temp, date, weather = data
    conn.commit()
    conn.close()

    return median_temp, date, weather


if __name__ == '__main__':
    insert_median()