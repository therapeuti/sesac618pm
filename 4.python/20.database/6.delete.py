import sqlite3

# DB 연결
conn = sqlite3.connect('example.db')

# 커서 객체 생성
cur = conn.cursor() # 입출력 인터페이스 만들기

# ---------------------------------------------------

# 데이터 삭제
cur.execute('DELETE FROM users WHERE name="Alice"')

# cur.exectue('DELETE FROM users WHERE name=?', ('Bob')) # 이렇게 표현하면 튜플인지, ()단일 인자인지, True/False를 계산하려는 건지 모름. 그래서 단일 인자일때도 튜플을 강제로 표현하기 위해 빈 콤마를 넣어줘야 함.
cur.execute('DELETE FROM users WHERE name=?',('Bob',))

# -------------------------------------------------------------------

# 커밋하여 변경사항 저장
conn.commit()

# DB 연결 종료
conn.close()