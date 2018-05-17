import sqlite3

conn = sqlite3.connect("task.db")
cur = conn.cursor()
# table col : id, what, due, importance, category, finished

def list_todo_due():
	slct_data = "select * from todo order by due asc where finished = 1"
	cur.execute(slct_data)
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

def list_todo_importance():
#	slct_data = "select * from todo where finished = 1"
#	cur.execute(slct_data)
	slct_data = "select * from todo order by importance asc, what asc where finished = 1"
	cur.execute(slct_data)
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

def list_todo_input():
	slct_data = "select * from todo where finished = 1"
	cur.execute(slct_data)
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

def list_todo_category(category):	# 가나다순
	slct_data = "select * from todo order by due asc where category = ?, finished = 1"
	cur.execute(slct_data, [category])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2])
