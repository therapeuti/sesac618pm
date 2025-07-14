import sqlite3

MY_DATABASE = 'example.db'

# db에 접속하는 함수 생성
def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
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


def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE name=?', (name, ))
    rows = cur.fetchone()

    conn.commit()
    conn.close()
    return rows



# 데이터 수정 함수
def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('UPDATE users SET age=? WHERE name=?', (new_age, name))

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


def main():
    create_table()

    insert_user('Alice', 25)
    insert_user('Bob', 35)
    insert_user('Charlie', 45)
    insert_user('Danny', 47)

    print('데이터 목록 조회')
    users = get_users()
    for user in users:
        print(user)

    # 데이터 업데이트
    print('데이터 업데이트: Alice, 32')
    update_user_age('Alice', 32)

    print('사용자 조회: ')
    print(get_user_by_name('Alice'))

    # 데이터 삭제
    print('데이터 삭제: Bob')
    delete_user_by_name('Bob')

    print('데이터 목록 조회')
    users = get_users()
    for user in users:
        print(user)




if __name__=='__main__':
    main()
