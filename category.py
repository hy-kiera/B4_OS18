import sqlite3

def show_category():
	conn = sqlite3.connect("task.db")
	cur = conn.cursor()

	slct_data = "select distinct category from todo where 1 order by category asc"
	cur.execute(slct_data)
	records = cur.fetchall()
	for row in records:
		print(row[0])

	print("")