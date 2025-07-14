import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor() # 입출력 인터페이스 만들기

# ---------------------------------------------------

# 데이터 삽입
cur.execute('''
            INSERT INTO users (name, age) VALUES ('Bob', 25)
            ''')

cur.execute('''
            INSERT INTO users (name, age) VALUES ('Alice', 25)
            ''')

# '?'는 placeholder
# prepared statement 라고 부름.. SQL injection 공격을 막는 패턴

cur.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
            ''',('Charlie', 40))


# -------------------------------------------------------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()