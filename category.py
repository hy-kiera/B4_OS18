import sqlite3

def show_category():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    slct_data = "select distinct category from todo where 1 order by category asc"
    cur.execute(slct_data)
    records = cur.fetchall()
    for row in records:
<<<<<<< HEAD
        print(row[0])
=======
        print(row[0])

    print("")
>>>>>>> 945079e0ae26e38c73bf8c8c331baa19f551c407
