import json
import requests
import sqlite3
from random import randint, uniform
from pprint import pprint
from faker import Faker

fake = Faker()


conn = sqlite3.connect("test.db")
# Create Cursor
cur = conn.cursor()


def send_event(event_data):
    webhook_url = "https://webhook.site/cdeb7ea5-22c8-4459-8b43-7b9389241638"

    r = requests.post(webhook_url, data=json.dumps(event_data), headers={
        "Content-Type": "application/json"})


def create_table():
    comm = """CREATE TABLE employees (emp_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, sex TEXT)"""
    cur.execute(comm)


def create_users():
    for _ in range(10):
        user = fake.profile()
        addUser = "INSERT INTO employees VALUES(NULL, ?, ?, ?)"
        cur.execute(addUser, (user["name"], user["birthdate"], user["sex"]))
        send_event(
            {"user": user["name"], "sex": user["sex"]})
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


def create_image_data():
    comm = """CREATE TABLE files (file_id INTEGER PRIMARY KEY, file BLOB, image BLOB, emp_id INTEGER,FOREIGN KEY (emp_id) REFERENCES employees(emp_id))"""
    cur.execute(comm)


def dummy_file_data():
    with open("./images/austin-wade-X6Uj51n5CE8-unsplash.jpg", "rb") as binIMG:
        addFile = "INSERT INTO files VALUES(?, NULL, ?,?)"
        cur.execute(addFile, (randint(0, 100000),
                              binIMG.read(), randint(1, 5000)))
    conn.commit()


search = """SELECT epp.emp_id,employees.name,sum(epp.epp) AS total_epp, sum(round((4.3 - epp.strike_price) * epp.epp,2)) as value_today, sum(round((20 - epp.strike_price) * epp.epp,2)) as value_2024
FROM epp
INNER JOIN employees
ON epp.emp_id = employees.emp_id
GROUP BY epp.emp_id
ORDER BY epp.emp_id"""

cur.execute(search)
data = cur.fetchall()[0]
# create_users()
create_image_data()
dummy_file_data()

pprint(f"{data[0]} - {data[1]} - {data[2]}")
