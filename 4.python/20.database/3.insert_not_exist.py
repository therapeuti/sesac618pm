import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor() # 입출력 인터페이스 만들기

# ---------------------------------------------------

# 데이터 조회 먼저
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]

if count == 0:
    # 데이터 삽입
    cur.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")
    cur.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?),('Charlie', 40)")
else:
    print('이미 데이터가 존재하여 더 이상 데이터 삽입을 하지 않음.')
    print('현재 사용자 데이터 개수: ', count)


# -------------------------------------------------------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()