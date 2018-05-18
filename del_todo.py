import sqlite3
import create_table as ct

def del_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    slct_data = "select * from todo where finished = 0 order by what asc"
    # finished = 0 일때를 보여줄지, finished 값과 상관없이 보여줄지 고민
    cur.execute(slct_data)
    records = cur.fetchall()
    for row in records:
        print(row[5], row[3], row[1], row[2], row[4])

    delete_data = str(input("What todo do you delete? Please enter the 'what'."))

    del_record = "delet from todo where what = ?"
    cur.execute(del_record, delete_data)

    print("Deleted")