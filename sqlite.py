import sqlite3

conn = sqlite3.connect("test.db")
# Create Cursor
cur = conn.cursor()

comm = "SELECT emp_id, name FROM employees"
tabl = """SELECT name FROM sqlite_schema
WHERE type='table'
ORDER BY name"""
desc = "PRAGMA table_info(employees)"
emp_epp = "SELECT employees.emp_id, employees.name, epp.epp, ROUND(epp.strike_price,2), ROUND(epp.epp * epp.strike_price,2) as Val FROM employees INNER JOIN epp ON employees.emp_id = epp.emp_id"
# cur.execute(desc)
cur.execute(emp_epp)
print(cur.fetchall())

conn.close()
