import sqlite3
import create_table as ct
import duecheck as dc

import inquirer

def add_todo():
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()

    sql = "insert into todo (what, due, importance, category, finished) values (?, ?, ?, ?, ?)"

    # lambda를 어떻게 작성해야 할지 모르겠어요.
    
    # questions = [
    #     inquirer.Text('what', message="What?"),
    #     inquirer.Text('due', message="Due? (yyyy-mm-dd hh:mm:ss)",
    #             validate=lambda x, _: re.match('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', x),
    #             ),
    #     inquirer.Text('importance', message="Importance? (1 ~ 5)",
    #             validate=lambda x, _: re.match('\d', x),
    #             ),
    #     inquirer.Text('category', message="Category?"),
    #     ]
    # answers = inquirer.prompt(questions)

    while True:
        what = str(input("What? "))
        if what != '':
            break

    while True:
        due = str(input("Due? (yyyy-mm-dd hh:mm:ss) "))
        if dc.isdue(due):
            break
        elif due == '':
            due = '0000-00-00 00:00:00'
            break
        else:
            print('Invaild input! Please check your input')
    
    while True:
        importance = str(input("Importance? (1 ~ 5) "))
        if importance == '':
            importance = 0
            break
        elif importance.isdigit() and 1 <= int(importance) <= 5:
            break
        else:
            print('Invaild input! Please check your input')

    category = str(input("Category? "))    
    if category == '':
        category = 'GENERAL'

    # data = [answers['what'], answers['due'], int(answers['importance']), answers['category'], "n"]
    data = [what, due, importance, category, "n"]

    cur.execute(sql, data)
    conn.commit()

    print("")
