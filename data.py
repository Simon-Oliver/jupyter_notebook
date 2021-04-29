import sqlite3
from random import randint, uniform

from faker import Faker
fake = Faker()


conn = sqlite3.connect("test.db")
# Create Cursor
cur = conn.cursor()


def create_table():
    comm = """CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, sex TEXT)"""
    cur.execute(comm)


def create_users():
    for _ in range(1000):
        user = fake.profile()
        addUser = "INSERT INTO employees VALUES(NULL, ?, ?, ?)"
        cur.execute(addUser, (user["name"], user["birthdate"], user["sex"]))

    conn.commit()


def create_epp_table():
    comm1 = """CREATE TABLE epp (epp_id INTEGER PRIMARY KEY, epp INTEGER, strike_price FLOAT, emp_id INTEGER, FOREIGN KEY (emp_id) REFERENCES employees(emp_id))"""
    cur.execute(comm1)


def dummy_epp_data():
    cur.execute("SELECT COUNT(emp_id) FROM employees")
    user_range = cur.fetchone()[0]
    for _ in range(5000):
        addEpp = "INSERT INTO epp VALUES(NULL, ?, ?, ?)"
        cur.execute(addEpp, (randint(0, 100000), uniform(
            0.36, 1.40), randint(1, user_range)))

    conn.commit()


cur.execute(
    "SELECT epp_id, SUM(epp) FROM epp LEFT OUTER JOIN employees ON epp.emp_id = employees.emp_id")
print(cur.fetchall())
