from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import timedelta
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd'
# app.secret_key = 'd'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
DB_FILENAME = 'user.db'

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def get_user(username, password):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute('SELECT * FROM users WHERE username=? ', (username, ))
    user = cur.fetchone()
    
    if user:
        print(user)
        hashed_password = user['password']

        conn.close()
        if bcrypt.checkpw(password.encode(), hashed_password):
            return user
        else:
            return None
    else:
        return None

def get_user_by_username(username):
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE username=?', (username, ))
    user = cur.fetchone()
    conn.close()
    return user

def create_user(user_id, user_pw, user_name):
    hashed_pw = hash_password(user_pw)
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password, name) VALUES (?, ?, ?)',
                (user_id, hashed_pw, user_name))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    id_ =  request.form.get('id')
    pw = request.form.get('pw')

    user = get_user(id_, pw)
    if user:
        flash('로그인에 성공했습니다.', 'success')
        session['user'] = {'id': user['id'], 'name': user['name']}
        return redirect(url_for('user', user=user))
    
    flash('아이디, 패스워드가 일치하지 않습니다.', 'danger')
    return redirect(url_for('index'))


@app.route('/user')
def user():
    if 'user' in session:
        # user = session['user']
        user = session.get('user')
        # user = session.get('user', None)
        return render_template('user.html', user=user)
    else:
        flash('로그인부터 하세요', 'warning')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
        flash('정상적으로 로그아웃 되었습니다.', 'success')
        return redirect(url_for('index'))

    else:
        flash('이미 로그아웃 되었습니다.', 'warning')
        return redirect(url_for('index'))


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('id')
        user_pw = request.form.get('pw')
        user_pw2 = request.form.get('pw2')
        user_name = request.form.get('name')
        if not user_id or not user_pw or not user_pw2 or not user_name:
            flash('모든 필드를 입력하세요.', 'warining')
            return redirect(url_for('register'))

        if user_pw != user_pw2:
            flash('비밀번호가 일치하지 않습니다.')
            return redirect(url_for('register'))

        if get_user_by_username(user_id):
            flash('이미 존재하는 사용자 아이디입니다.', 'danger')
            return redirect(url_for('register'))

        create_user(user_id, user_pw, user_name)
        flash('회원가입이 완료되었습니다. 로그인 해주세요.', 'success')
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True)