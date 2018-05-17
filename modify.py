import sqlite3

def modify_todo() :
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    mID = input("Record ID?")
    mTodo = input("Todo?")
    mDue = input("Due date?")
    mFinished = input("Finished (1: yes, 0: no)?")
    cur.execute("""UPDATE todo SET what = ?, due = ?, finished = ? WHERE id = ?""", (mTodo, mDue, mFinished, mID))
    conn.commit()
    cur.close()
    conn.close()