import sqlite3
import create_table as ct

def add_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "insert into todo (what, due, importance, category, finished) values (?, ?, ?, ?, ?)"

    what = str(input("What? "))
    due = str(input("Due? (yyyy-mm-dd hh:mm:ss) "))
    importance = int(input("Importance? (1 ~ 5) "))
    category = str(input("Category? "))

    data = [what, due, importance, category, 0]

    cur.execute(sql, data)
    conn.commit()

    print("")