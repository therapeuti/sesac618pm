import sqlite3
# import db_crud_sqlite as db
from db_crud_sqlite import *

MY_DATABASE = 'example.db'


def main():
    create_table()

    insert_user('Alice', 25)
    insert_user('Bob', 35)
    insert_user('Charlie', 45)
    insert_user('Danny', 47)

    print('데이터 목록 조회')
    users = get_users()
    for user in users:
        print(user)

    # 데이터 업데이트
    print('데이터 업데이트: Alice, 32')
    update_user_age('Alice', 32)

    print('사용자 조회: ')
    print(get_user_by_name('Alice'))

    # 데이터 삭제
    print('데이터 삭제: Bob')
    delete_user_by_name('Bob')

    print('데이터 목록 조회')
    users = get_users()
    for user in users:
        print(user)




if __name__=='__main__':
    main()
