import sqlite3

def modify_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    slct_data = "select * from todo where 1 order by what asc"
    cur.execute(slct_data)
    records = cur.fetchall()
    for row in records:
        print(row[5], row[3], row[1], row[2], row[4])

    modify = str(input("What todo do you want to modify? Please enter 'what' "))
    what_m = str(input("What? "))
    due_m = str(input("Due date? (yyyy-mm-dd hh:mm:ss) "))
    importance_m = int(input("Importance? "))
    category_m = str(input("Category? "))
    finished_m = int(input("Finished (1: yes, 0: no)? "))

    sql = "update todo set what = ?, due = ?, importance = ?, category = ?, finished = ? where what = ?"

    cur.execute(sql, (what_m, due_m, importance_m, category_m, finished_m, modify))
    conn.commit()

    print("")
