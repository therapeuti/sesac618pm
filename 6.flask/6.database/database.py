import sqlite3

MY_DATABASE = 'users.db'


# db에 접속하는 함수 생성
def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row # 각 행이 튜플이 아닌 딕셔너리로 반환된다.
    return conn

# users 테이블 생성 함수 작성
def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, name TEXT, age INTEGER)')

    conn.commit()
    conn.close()


# 데이터 삽입 함수
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

    conn.commit()
    conn.close()


# 데이터 조회 함수
def get_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()

    conn.commit()
    conn.close()
    return rows


def get_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE id=?', (id, ))
    rows = cur.fetchone()

    conn.commit()
    conn.close()
    return rows



# 데이터 수정 함수
def update_user(id, new_name, new_age):
    print(id)
    print(new_name)
    print(new_age)
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('UPDATE users SET name=?, age=? WHERE id=?', (new_name, new_age, id))

    conn.commit()
    conn.close()


# 데이터 삭제 함수
def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('DELETE FROM users WHERE name=?', (name,))

    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur= conn.cursor()

    cur.execute('DELETE FROM users WHERE=?', (id,))

    conn.commit()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('DELETE FROM users WHERE=?', (age,))

    conn.commit()
    conn.close()