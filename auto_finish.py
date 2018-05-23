import sqlite3
import duecheck as dc

def auto_fin():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    slct_data = "select * from todo where finished = 0"
    cur.execute(slct_data)
    records = cur.fetchall()
    for row in records:
        if not dc.istime(row[2]):
            sql = "update todo set finished = 1 where id = ?"
            cur.execute(sql,[row[0]])
            conn.commit()
