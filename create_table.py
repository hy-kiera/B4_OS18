import sqlite3

def create_table():

    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    table_create_sql = """create table if not exists todo (
            id integer primary key autoincrement,
            what text not null,
            due text not null,
            finished integer); """
    cur.execute(table_create_sql)
    conn.commit()
    conn.close()
