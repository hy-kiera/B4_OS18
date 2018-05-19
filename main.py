import sqlite3
import logo as lg
import add_todo as at
import list as li
import create_table as ct
import modify as md
import del_todo as dl
import category as ctg

def run_program():
	while True:
		print("Choose what to do")
		mode = str(input("(a: Add todo, l: list todo, m: Modify todo, d: Delete todo, c: Show category q:Quit)? "))
		print(mode)
		if mode == 'a' or 'A':
			at.add_todo()
		elif mode == 'l' or 'L':
			li.list_todo_due()
		elif mode == 'm' or 'M':
			md.modify_todo()
		elif mode == 'd' or 'D':
			dl.del_todo()
		elif mode == 'c' or 'C':
			ctg.show_category()
		elif mode == 'q' or 'Q':
			break

if __name__ == "__main__":
    lg.print_logo()
    ct.create_table()
    run_program()