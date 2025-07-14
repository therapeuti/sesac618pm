import sqlite3

MY_DATABASE = 'todolist.db'


# db에 접속하는 함수 생성
def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row # 각 행이 튜플이 아닌 딕셔너리로 반환된다.
    return conn

# todolist 테이블 생성 함수 작성
def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
                CREATE TABLE IF NOT EXISTS todolist
                (id INTEGER PRIMARY KEY NOT NULL, 
                todo TEXT, 
                status TEXT,
                completed_date DATETIME)
                ''')

    conn.commit()
    conn.close()


# 데이터 삽입 함수
def insert_todo(todo, status, date):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('INSERT INTO todolist (todo, status, completed_date) VALUES (?, ?, ?)', (todo, status, date))

    conn.commit()
    conn.close()


# 데이터 조회 함수
def get_todolist():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM todolist')
    rows = cur.fetchall()
    todolist = [dict(row) for row in rows]  # Row 객체를 dict로 변환

    conn.commit()
    conn.close()
    return todolist


# 데이터 수정 함수
def update_status(todo, status):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('UPDATE todolist SET status=? WHERE todo=?', (status, todo))

    conn.commit()
    conn.close()


# 데이터 삭제 함수
def delete_todo(todo):
    conn = connect_db()
    cur= conn.cursor()

    cur.execute('DELETE FROM todolist WHERE todo=?', (todo,))

    conn.commit()
    conn.close()
