import sqlite3
from datetime import date, datetime, time

conn = sqlite3.connect("test.db")
# Create Cursor
cur = conn.cursor()

comm = "SELECT emp_id, name, age FROM employees WHERE age >= '2019-12-04'"
tabl = """SELECT name FROM sqlite_schema
WHERE type='table'
ORDER BY name"""
desc = "PRAGMA table_info(employees)"
emp_epp = "SELECT employees.emp_id, employees.name, epp.epp, ROUND(epp.strike_price,2), ROUND(epp.epp * epp.strike_price,2) as Val FROM employees INNER JOIN epp ON employees.emp_id = epp.emp_id"
group = "SELECT age, COUNT(age) from employees GROUP BY age HAVING COUNT(age)>2"
time_t = """
    SELECT strftime('%Y', age) as birth_year, COUNT(strftime('%Y', age)) as count FROM employees GROUP BY birth_year HAVING count > 28 ORDER BY count
"""


# cur.execute(desc)
cur.execute(time_t)
print(cur.fetchall())

conn.close()

# print(datetime.strptime("2018-09-10", "%Y-%m-%d"))
