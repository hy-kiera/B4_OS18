import sqlite3

def list_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "select * from todo where 1"
    cur.execute(sql)
    # 데이터를 패치합니다.
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("")

def list_todo_importance():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    print("")

def list_todo_input():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    print("")
