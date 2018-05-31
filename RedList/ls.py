import sqlite3
import category as ctg
import inquirer

conn = sqlite3.connect("task.db")
cur = conn.cursor()
# table col : id, what, due, importance, category, finished

def list_todo_due():
	slct_data = "select * from todo where finished = ? order by due asc, what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

	print("")

def list_todo_importance():
	slct_data = "select * from todo where finished = ? order by importance asc, what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

	print("")

def list_todo_what():
	slct_data = "select * from todo where finished = ? order by what asc"
	cur.execute(slct_data,['n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2], row[4])

	print("")

def list_todo_category(category):	# 가나다순
	slct_data = "select * from todo where category = ? and finished = ? order by category asc"
	cur.execute(slct_data, [category,'n'])
	records = cur.fetchall()
	for row in records:
		print(row[5], row[3], row[1], row[2])

	print("")

def list_main():
	opt = [
			inquirer.List('opt',
				message="Choose list option",
				choices=['due', 'what', 'importance', 'category'],
			),
		]
	answers = inquirer.prompt(opt)
	
	if answers['opt'] == 'due':
		list_todo_due()
	elif answers['opt'] == 'what':
		list_todo_what()
	elif answers['opt'] == 'importance':
		list_todo_importance()
	elif answers['opt'] == 'category':
		ctg.show_category()
		c = str(input("What cateogry do you want to list? "))

		list_todo_category(c)
