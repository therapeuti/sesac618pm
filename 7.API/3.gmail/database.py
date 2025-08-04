import sqlite3

DB = 'users.db'

def create_users():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE users (
                    id STRING PRIMARY KEY,
                    nickname STRING,
                    profile_image STRING,
                    age STRING,
                    gender STRING,
                    email STRING,
                    name STRING,
                    birthday STRING)
                ''')
    conn.commit()
    conn.close()

def insert_user(user):
    cols = tuple(user.keys())
    values = tuple(user.values())
    print(cols)
    print(values)


    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute(f'INSERT INTO users {cols} VALUES {values}')
    conn.commit()
    conn.close()

def update_user(user):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute('''UPDATE users
                SET nickname=?, age=?, gender=?, email=?, name=? , birthday=? ''',
                user)
    conn.commit()
    conn.close()
    return