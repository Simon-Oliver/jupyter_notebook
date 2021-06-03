import sqlite3

conn = sqlite3.connect("test.db")
# Create Cursor
cur = conn.cursor()

comm = "SELECT emp_id FROM employees"
desc = "PRAGMA table_info(employees)"
# cur.execute(desc)
cur.execute(comm)
print(cur.fetchall())
