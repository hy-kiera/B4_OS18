import sqlite3

conn = sqlite3.connect("task.db")
cur = conn.cursor()

def create_table():

    table_create_sql = """create table if not exists todo (
            id integer primary key autoincrement,
            what text not null,
            due text not null,
            category text not null,
            finished integer); """
    cur.execute(table_create_sql)
    conn.commit()
    conn.close()
