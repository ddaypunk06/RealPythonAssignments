import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	try:
		c.execute("INSERT INTO populations VALUES('New York City','NY', 8200000)")
		c.execute("INSERT INTO populations VALUES('San Fransisco','CA', 800000)")

#		conn.commit()

	except sqlite3.OperationalError:
		print "Oops! Something went wrong. Try again..."