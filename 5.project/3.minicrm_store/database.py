import sqlite3

DATABASE = 'mycrm.db'

def get_connect():
    conn = sqlite3.connect(DATABASE)
    # 미션 1-1 DB로부터 가져온 내용을 dict로 바꾸고 싶으면?
    conn.row_factory = sqlite3.Row
    return conn


def get_stores():
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores')
    stores = cursor.fetchall()
    conn.close()

    stores = [dict(s) for s in stores]

    # 미션 1-2 : 미션1을 안 했다면. 여기에 튜플형의 데이터를 딕셔너리로 바꾸는 작업이 필요.
    # key = ['id','name','type','address']
    # stores_dict_list = []
    # for s in stores:
    #     for i in range(len(s)):
    #         dic = {}
    #         dic[key[i]] = s[i]
    #     stores_dict_list.append(dic)           

    # stores_dict = [{'id': s[0], 'name': s[1], 'type': s[2], 'address': s[3]} for s in stores]
    return stores


def search_stores(query):
    conn = get_connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM stores WHERE name Like ? ', (f'%{query}%', ) )
    stores = cursor.fetchall()
    conn.close()
    # for s in stores:
    #     print(dict(stores))
    return stores