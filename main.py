import logo as lg
import add_todo as at
import list as li
import create_table as ct
import modify as md

def run_program():
    import sqlite3
    while True:
    	i = input("choose what to do\n(a: Add todo, l: list todo, m: Modify todo, q:Quit)? ")
    	if (i == 'a'):
        	at.add_todo()
    	elif (i == 'l'):
    	    li.list_todo()
    	elif (i == 'm'):
       		md.modify_todo()
    	elif (i == 'q'):
        	return
            
if __name__ == "__main__":
    lg.print_logo()
    ct.create_table()
    run_program()
