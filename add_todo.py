import sqlite3
import create_table as ct
import duecheck as dc

def add_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "insert into todo (what, due, importance, category, finished) values (?, ?, ?, ?, ?)"

    what = str(input("What? "))
    while True:
        due = str(input("Due? (yyyy-mm-dd hh:mm:ss) "))
        if(dc.isdue(due)):
            break
        else:
            print('Invaild input! Please check your input')
    importance = int(input("Importance? (1 ~ 5) "))
    category = str(input("Category? "))

    data = [what, due, importance, category, 0]

    cur.execute(sql, data)
    conn.commit()

    print("")
