import sqlite3
from random import randint, uniform
from pprint import pprint

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


search = """SELECT epp.emp_id,employees.name,sum(epp.epp) AS total_epp, sum(round((4.3 - epp.strike_price) * epp.epp,2)) as value_today, sum(round((20 - epp.strike_price) * epp.epp,2)) as value_2024
FROM epp
INNER JOIN employees
ON epp.emp_id = employees.emp_id
GROUP BY epp.emp_id
ORDER BY epp.emp_id"""

cur.execute(search)
data = cur.fetchall()[0]

pprint(f"{data[0]} - {data[1]} - {data[2]}")
