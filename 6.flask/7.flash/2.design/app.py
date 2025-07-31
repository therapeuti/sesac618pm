from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'm'

users = [{'id': 'tm', 'pw':'pw', 'name':'태민'}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u_id = request.form.get('id')
        pw = request.form.get('pw')
        user = next((u for u in users if u['id']==u_id and u['pw']==pw), None)
        if user:
            session['user'] = user
            return redirect(url_for('user'))
        else:
            flash('로그인 실패', 'danger')
            return redirect(url_for('login'))
    else:
        if 'user' in session:
            flash('이미 로그인된 사용자', 'warning')
            print(session['user'])
            return redirect(url_for('user'))   
    return render_template('login.html')

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        flash('로그인에 성공했습니다.', 'success')
        return render_template('user.html', user=user)
    flash('비정상 접근. 로그인 먼저 하세요.','warning')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('정상적으로 로그아웃 되었습니다.', 'success')
    return redirect(url_for('login'))



if __name__=='__main__':
    app.run(debug=True)