import sqlite3
import logo as lg
import add_todo as at
import list as li
import create_table as ct
import modify as md
import del_todo as dl

def run_program():
	while True:
		i = input("choose what to do\n(a: Add todo, l: list todo, m: Modify todo, d: Delete todo, q:Quit)? ")
		if (i == 'a' or 'A'):
			at.add_todo()
		elif (i == 'l' or 'L'):
			li.list_todo_due()
		elif (i == 'm' or 'M'):
			md.modify_todo()
		elif (i == 'd' or 'D'):
			dl.del_todo()
		elif (i == 'q' or 'Q'):
			return

if __name__ == "__main__":
    lg.print_logo()
    ct.create_table()
    run_program()
