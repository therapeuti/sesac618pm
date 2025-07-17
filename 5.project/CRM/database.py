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
def get_users_list(count: int, filtering: dict):
    offset_num = int((filtering['page'] - 1 ) * count)
    logging.debug(f'count: {count}, page: {filtering["page"]}, offset_num: {offset_num}')
    logging.debug(f'필터링 조건 확인: {filtering}')

    # SQL 쿼리문 작성위해 where 조건이 있는 경우와 없는 경우로 구분
    filter_keys = []   # ex) id LIKE ?
    filter_values = []  # ex) %김%
    for key, value in filtering.items(): 
        if key not in ['page', 'gender', 'orderby']:
            filter_keys.append(f'{key} LIKE ?')
            filter_values.append(f'%{value}%')
        elif key == 'gender':
            filter_keys.append(f'{key}=?')
            filter_values.append(value)
    parameter_count_tuple = tuple(filter_values)
    filter_values.extend([count, offset_num])
    parameter_tuple = tuple(filter_values)
    logging.debug(f'where 조건이 없으면 0, 있으면 1 이상 : {len(filter_keys)}')

    conn = get_connect()
    cur = conn.cursor()
    # 전체 사용자 목록 가져오기 (필터링 조건 없음)
    if len(filter_keys) == 0:
        # 쿼리문 실행 - 사용자 목록 가져오기
        logging.debug(f'order by 조건: {filtering["orderby"]}')
        sql_query = f'SELECT * FROM users ORDER BY {filtering["orderby"]} LIMIT ? OFFSET ?'
        cur.execute(sql_query, (count, offset_num))
        users = cur.fetchall()
        # 쿼리문 실행 - 사용자 데이터 개수 가져오기
        cur.execute('SELECT COUNT(*) FROM users')
        count_users = cur.fetchone()[0]
    # 필터링 조건에 따른 사용자 목록 가져오기
    else:    
        where_keys = ' AND '.join(filter_keys)
        where = 'WHERE ' + where_keys
        sql_query = 'SELECT * FROM users ' + where + ' ORDER BY '+ filtering['orderby']+' LIMIT ? OFFSET ?'
        sql_count_query = 'SELECT COUNT(*) FROM users ' + where
        logging.debug(f'SQL 쿼리문:  {sql_query}')
        logging.debug(f'파라미터 튜플 :  {parameter_tuple}')
        cur.execute(sql_query, parameter_tuple)
        users = cur.fetchall()
        logging.debug(f'사용자 목록 가져온건 맞음? {users}')
        logging.debug(sql_count_query)
        logging.debug(parameter_count_tuple)
        cur.execute(sql_count_query, parameter_count_tuple)
        count_users = cur.fetchone()[0]
        logging.debug(count_users)
    cur.close()

    # 검색된 사용자가 없는 경우... 한 명만 있는 경우... 여러 명인 경우...
    logging.debug(f'전체 사용자 수: {count_users}')
    if count_users == 0:
        users_dict = []
        logging.debug('검색 조건에 해당하는 사용자를 찾을 수 없습니다.')
    else:
        logging.debug(f'사용자 전체 조회해서 첫번째 사용자 정보만 가져옴. -> {users[0]}')
        users_dict = [dict(u) for u in users]
    return users_dict, count_users

def get_stores_list(count, filtering):
    offset_num = (filtering['page'] - 1) * count

    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * from stores LIMIT ? OFFSET ?', (count, offset_num))
    stores = cur.fetchall()
    stores_dict = [dict(s) for s in stores]

    cur.execute('SELECT COUNT(*) from stores')
    count_stores = cur.fetchone()[0]
    logging.debug(stores_dict)
    logging.debug(count_stores)

    cur.close()
    return stores_dict, count_stores