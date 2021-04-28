import sqlite3

from faker import Faker
fake = Faker()


conn = sqlite3.connect("test.db")

# Create Cursor
cur = conn.cursor()

for _ in range(5):
    user = fake.profile()
    addUser = "INSERT INTO customers VALUES(NULL, ?, ?, ?)"
    cur.execute(addUser, (user["name"], user["birthdate"], user["sex"]))

# comm = """CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, sex TEXT)"""

# cur.execute(comm)
