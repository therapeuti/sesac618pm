import sqlite3
import logging

#로깅 설정
logging.basicConfig(level=logging.DEBUG,  # 로깅 레벨 설정. DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL 순으로 레벨이 높음. 설정된 레벨 이상의 로그만 출력됨.im
                    format="%(asctime)s [%(levelname)s] %(message)s", # 로그 출력 형식을 정의(포맷팅). 로그 발생 시각, 로그 레벨 이름, 출력 메시지(사용자가 정의..?) 
                    datefmt='%Y-%m-%d %H-%M-%S') # 로그 발생 시각의 출력 형식을 정의


DATABASE = 'mycrm.db'

# 데이터베이스 연결
def get_connect():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# 사용자 전체 조회
def get_users_list(count: int, page: int):
    offset_num = int((page - 1 ) * count)
    logging.debug(f'count: {count}, page: {page}')
    logging.debug(f'offset_num: {offset_num}')
    conn = get_connect()
    cur = conn.cursor() # 커서 객체(입출력 인터페이스) 생성.
    cur.execute('SELECT * FROM users LIMIT ? OFFSET ?', (count, offset_num))
    users = cur.fetchall()
    logging.debug(f'사용자 전체 조회해서 첫번째 사용자 정보만 가져옴. -> {users[0]}')
    users_dict = [dict(u) for u in users]
    cur.close()
    return users_dict

def count_users():
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM users')
    count_users = cur.fetchone()[0]
    logging.debug(f'전체 사용자 수: {count_users}')
    cur.close()
    return count_users

def get_users_by_id(id: str):
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id=?', (id, ))
    user = cur.fetchone() # id가 겹칠 일을 없겠지만.. 혹시나 겹치는 일이 있다면...?? 예외처리 어떻게..?
    logging.debug(f'id로 찾은 사용자 정보 : {user}')
    cur.close()
    return user