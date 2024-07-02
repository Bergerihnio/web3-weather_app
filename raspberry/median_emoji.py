import sqlite3
from datetime import date


def get_stats_emoji():
    conn = sqlite3.connect('temperatures.db')
    c = conn.cursor()

    data = f'{date.today()}'
    time_start = '10:00:00'
    time_end = '20:00:00'

    c.execute("SELECT emoji FROM temperatures WHERE date= (?) AND time BETWEEN ? AND ?",
              (data, time_start, time_end))
    rows = c.fetchall()

    rows_list = []
    for row in rows:
        rows_list.append(row[0])
    conn.close()

    emoji_string = the_most_occurate(rows_list)

    return emoji_string


def the_most_occurate(emoji_list):
    counter = 0
    for element in emoji_list:
        current = emoji_list.count(element)
        if (current > counter):
            counter = current
            the_most_occ = [element]

        elif current == counter:
            if element not in the_most_occ:
                the_most_occ.append(element)
    emoji_string = ''.join(the_most_occ)
    return emoji_string


if __name__ == '__main__':
    get_stats_emoji()
