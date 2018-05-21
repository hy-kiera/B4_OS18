import sqlite3

def modify_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "update todo set what=?, due=?, category=?, finished=? where id=?"

    id_num = input("Record id? ")
    what_m = input("Todo? ")
    due_m = input("Due date? (yyyy-mm-dd hh:mm:ss) ")
    importance_m = input("Importance? ")
    category_m = input("Category? ")
    finished_m = input("Finished (1: yes, 0: no)? ")

    cur.execute(sql, (what_m,due_m,importance_m,category_m,finished_m,id_num))
    conn.commit()

    sql = "select * from todo where 1"
    cur.execute(sql)
    print("")
