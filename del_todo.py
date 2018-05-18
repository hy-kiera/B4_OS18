import sqlite3
import create_table as ct

def del_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    slct_data = "select * from todo order by what asc where finished = 1"
    cur.execute(slct_data)
    records = cur.fetchall()
    for row in records:
        print(row[5], row[3], row[1], row[2], row[4])

    d = input("What todo do you delete? Please enter the 'what'.")

    del_record = "delet from todo where what = ?"
    cur.execute(del_record, d)
