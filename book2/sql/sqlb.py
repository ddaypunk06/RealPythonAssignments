import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()
	
	c.execute("INSERT INTO population VALUES('New York City','NY', 8200000)")
	c.execute("INSERT INTO population VALUES('San Fransisco','CA', 800000)")