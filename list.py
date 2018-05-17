import sqlite3

def list_todo():
    # 데이터를 패치합니다.
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("\n")

def list_todo_importance():

def list_todo_input():
