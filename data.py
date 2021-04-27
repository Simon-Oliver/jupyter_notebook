import sqlite3

connection = sqlite3.connect("test.db")

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)
"""

cursor.execute(command1)
