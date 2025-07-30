from flask import Flash, render_template, request, redirect, url_for, flash, session

app = Flash(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u_id = request.form.get('id')
        pw = request.form.get('pw')
        user = next((u for u in users if u['id']==id and u['pw']==pw))
        if user:
            flash('로그인에 성공했습니다.')
            session['user'] = user
            return redirect(url_for('user'))
    else:
        if 'user' in session:
            flash('이미 로그인된 사용자')
            return redirect(url_for('user'))   

    return render_template('login.html')


@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('정상적으로 로그인 되었씁니다.')
    return redirect(url_for('login'))
if __name__=='__main__':
    app.run(debug=True)