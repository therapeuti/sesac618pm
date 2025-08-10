import sqlite3

DB = 'todolist.db'

def create_table():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS todolist 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 todo STRING,
                 status STRING)
                 ''')
    cur.execute('''CREATE TABLE IF NOT EXISTS conversation
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                role STRING,
                content TEXT)
                ''')
    conn.commit()
    conn.close()


def get_connect():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def get_todolist():
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM todolist')
    todolist = cur.fetchall()
    todolist = [dict(todo) for todo in todolist]

    conn.close()
    print(todolist)
    return todolist


def get_status(id):
    conn = get_connect()    
    cur = conn.cursor()

    cur.execute('SELECT status FROM todolist WHERE id=?', (id, ))
    status = cur.fetchone()
    return dict(status)


def insert_todo(todo, status):
    conn = get_connect()
    cur = conn.cursor()
    
    cur.execute('INSERT INTO todolist (todo, status) VALUES (?, ?)', (todo, status))

    conn.commit()
    conn.close()


def update_todo(todo_id, status):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('UPDATE todolist SET status=? WHERE id=?', (status, todo_id))
    conn.commit()

    cur.execute('SELECT * FROM todolist WHERE id=?', (todo_id, )) 
    todo = cur.fetchone()   
    conn.close()
    return dict(todo)


def delete_todo(todo_id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('DELETE FROM todolist WHERE id=?', (todo_id, ))

    conn.commit()
    conn.close()


def save_conversation(role, content):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('INSERT INTO conversation (role, content)VALUES (?, ?)', (role, content))

    conn.commit()
    conn.close()


if __name__=='__main__':
    create_table()