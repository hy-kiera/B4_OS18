import sqlite3

def add_todo():
    global ID, sql
    sql = "insert into todo (what,due,category,finished) values (?,?,?,?)"

    what = input("What? ")
    due = input("Due? yyyy-mm-dd hh:mm:ss")
    category = input("Category? ")

    cur.execute(sql, (what,due,category,0))
    conn.commit()
    # print("inserted")

    sql = "select * from todo where 1"
    cur.execute(sql)
    print("\n")
