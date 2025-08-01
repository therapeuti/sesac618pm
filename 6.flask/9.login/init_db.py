import sqlite3
import hashlib

DB_FILENAME = 'user.db'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()


cur.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                name TEXT NOT NULL)
            ''')

# 테스타 사용자 추가
password1 = hash_password('password1')
password2 = hash_password('password2')

cur.execute('INSERT INTO users (username, password, name) VALUES (?, ?, ?)',
            ("user1", password1, "UserName1"))
cur.execute('INSERT INTO users (username, password, name) VALUES (?, ?, ?)',
            ("user2", password2, "UserName2"))

conn.commit()
conn.close()