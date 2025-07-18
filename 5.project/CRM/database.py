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

def get_users_gender():
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT gender from users')
    gender = cur.fetchall()
    gender_value = gender.values()
    logging.debug(gender_value)
    return gender_value

def get_user_by_id(id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE id=?', (id ,))
    user = cur.fetchone()[0]
    logging.debug(user)

    conn.close()
    if not user:
        user = '사용자 정보가 없음'
        return user
    else:
        logging.debug(dict(user))
        user_dict = dict(user)
        return user_dict


def get_stores_list(count, filtering):
    offset_num = (filtering['page'] - 1) * count

    # SQL 쿼리문 작성위해 where 조건이 있는 경우와 없는 경우로 구분
    filter_keys = []   # ex) id LIKE ?
    filter_values = []  # ex) %김%
    for key, value in filtering.items(): 
        if key not in ['page', 'type', 'orderby']:
            filter_keys.append(f'{key} LIKE ?')
            filter_values.append(f'%{value}%')
        elif key == 'type':
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
        sql_query = f'SELECT * FROM stores ORDER BY {filtering["orderby"]} LIMIT ? OFFSET ?'
        cur.execute(sql_query, (count, offset_num))
        stores = cur.fetchall()
        # 쿼리문 실행 - 사용자 데이터 개수 가져오기
        cur.execute('SELECT COUNT(*) FROM stores')
        count_stores = cur.fetchone()[0]
    # 필터링 조건에 따른 사용자 목록 가져오기
    else:    
        where_keys = ' AND '.join(filter_keys)
        where = 'WHERE ' + where_keys
        sql_query = 'SELECT * FROM stores ' + where + ' ORDER BY '+ filtering['orderby']+' LIMIT ? OFFSET ?'
        sql_count_query = 'SELECT COUNT(*) FROM stores ' + where
        logging.debug(f'SQL 쿼리문:  {sql_query}')
        logging.debug(f'파라미터 튜플 :  {parameter_tuple}')
        cur.execute(sql_query, parameter_tuple)
        stores = cur.fetchall()
        logging.debug(f'사용자 목록 가져온건 맞음? {stores}')
        logging.debug(sql_count_query)
        logging.debug(parameter_count_tuple)
        cur.execute(sql_count_query, parameter_count_tuple)
        count_stores = cur.fetchone()[0]
        logging.debug(count_stores)
    cur.close()

    # 검색된 사용자가 없는 경우... 한 명만 있는 경우... 여러 명인 경우...
    logging.debug(f'전체 사용자 수: {count_stores}')
    if count_stores == 0:
        stores_dict = []
        logging.debug('검색 조건에 해당하는 사용자를 찾을 수 없습니다.')
    else:
        logging.debug(f'첫번째 스토어 정보만 가져옴. -> {stores[0]}')
        stores_dict = [dict(s) for s in stores]
        logging.debug(stores_dict)
        logging.debug(count_stores)

    cur.close()
    return stores_dict, count_stores

def get_store_type():
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT DISTINCT type from stores')
    store_type = cur.fetchall()
    logging.debug(store_type)
    type_values = [dict(s)['type'] for s in store_type]
    logging.debug(type_values)
    return type_values

def get_store_by_id(id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM stores WHERE id=?', (id ,))
    store = cur.fetchone()
    conn.close()
    if not store:
        store = '스토어 정보가 없음'
        return store
    else:
        logging.debug(dict(store))
        store_dict = dict(store)
        return store_dict

def get_items_list(count, filtering):
    offset_num = (filtering['page'] - 1) * count

    conn = get_connect()
    cur = conn.cursor()

    sql_query = f'SELECT * FROM items ORDER BY {filtering["orderby"]} LIMIT ? OFFSET ?'
    cur.execute(sql_query, (count, offset_num))

    items = cur.fetchall()
    items_dict = [dict(s) for s in items]

    cur.execute('SELECT COUNT(*) from items')
    count_items = cur.fetchone()[0]
    logging.debug(items_dict)
    logging.debug(count_items)

    cur.close()
    return items_dict, count_items

def get_item_by_id(id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM items WHERE id=?', (id ,))
    item = cur.fetchone()
    conn.close()
    if not item:
        item = '아이템 정보가 없음'
        return item
    else:
        logging.debug(dict(item))
        item_dict = dict(item)
        return item_dict

def get_orders_list(count, filtering):
    offset_num = (filtering['page'] - 1) * count

    conn = get_connect()
    cur = conn.cursor()

    sql_query = f'SELECT * FROM orders ORDER BY {filtering["orderby"]} LIMIT ? OFFSET ?'
    cur.execute(sql_query, (count, offset_num))

    orders = cur.fetchall()
    orders_dict = [dict(s) for s in orders]

    cur.execute('SELECT COUNT(*) from orders')
    count_orders = cur.fetchone()[0]
    logging.debug(orders_dict)
    logging.debug(count_orders)

    cur.close()
    return orders_dict, count_orders

def get_order_by_id(id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM orders WHERE id=?', (id ,))
    order = cur.fetchone()
    conn.close()
    if not order:
        order = '아이템 정보가 없음'
        return order
    else:
        logging.debug(dict(order))
        order_dict = dict(order)
        return order_dict



def get_orderitems_list(count, filtering):
    offset_num = (filtering['page'] - 1) * count

    conn = get_connect()
    cur = conn.cursor()

    sql_query = f'SELECT * FROM orderitems ORDER BY {filtering["orderby"]} LIMIT ? OFFSET ?'
    cur.execute(sql_query, (count, offset_num))

    orderitems = cur.fetchall()
    orderitems_dict = [dict(s) for s in orderitems]

    cur.execute('SELECT COUNT(*) from orderitems')
    count_orderitems = cur.fetchone()[0]
    logging.debug(orderitems_dict)
    logging.debug(count_orderitems)

    cur.close()
    return orderitems_dict, count_orderitems

def get_orderitem_by_id(id):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute('SELECT * FROM orderitems WHERE id=?', (id ,))
    orderitem = cur.fetchone()
    conn.close()
    if not orderitem:
        orderitem = '아이템 정보가 없음'
        return orderitem
    else:
        logging.debug(dict(orderitem))
        orderitem_dict = dict(orderitem)
        return orderitem_dict