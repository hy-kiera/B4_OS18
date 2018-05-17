import sqlite3
import create_table as ct

def add_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "insert into todo (what,due,importance,category,finished) values (?,?,?,?)"

    what = input("What? ")
    due = input("Due? (yyyy-mm-dd hh:mm:ss) ")
    importance = input("importance? ")
    category = input("Category? ")

    cur.execute(sql, (what,due,importance,category,0))
    conn.commit()
    # print("inserted")

    print("")
