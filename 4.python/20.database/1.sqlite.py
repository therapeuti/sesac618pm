import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor() # 입출력 인터페이스 만들기

# 커서를 중심으로 DB에 입출력을 한다.
cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL, 
                age INTEGER NOT NULL
            )
            ''')

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()