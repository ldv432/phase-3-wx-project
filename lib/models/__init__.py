import sqlite3

CONN = sqlite3.connect('lib/weather_data.db')
CURSOR = CONN.cursor()