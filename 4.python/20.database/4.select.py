import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor() # 입출력 인터페이스 만들기

# ---------------------------------------------------


# 데이터조회
cur.execute('SELECT * FROM users')

# 결과 가져오기 - 모든 행 가져오기 fetchall()
rows = cur.fetchall()
# print(rows)

for row in rows:
    print(row)


print('-'*30)
cur.execute('SELECT * FROM users')
rows = cur.fetchone()
print(rows)

print('-'*30)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchall()
print(rows)

print('-'*30)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone()
print(rows)

print('-'*30)
cur.execute('SELECT COUNT(*) FROM users')
rows = cur.fetchone()[0]
print(rows)
# -------------------------------------------------------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()