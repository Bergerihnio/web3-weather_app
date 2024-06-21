import sqlite3


# Connect to the DB
connect = sqlite3.connect('temperature.db')
# Create a cursor
cursor = connect.cursor()

'''
# Create table
cursor.execute("""CREATE TABLE temperature (
               today_temp REAL,
               next_day_temp REAL
               )""")
'''

cursor.execute("INSERT INTO temperature VALUES (12, 10)")

cursor.execute("SELECT * FROM temperature")

print(cursor.fetchall()[0])

# Commit our changes
connect.commit()

# Close database connection
connect.close()