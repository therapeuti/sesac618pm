from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session


app = Flask(__name__)
app.secret_key = 'my'

users = [{'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
         {'name':'Bob', 'id': 'bob', 'pw': 'bobpw12'},
         {'name':'Charlie', 'id': 'chal', 'pw': 'charlie562'}]


@app.route('/', methods=['GET', 'POST']) # get 요청은 url 파라미터에 정보를 담아서 전달, post 요청은 http의 바디에 담아서 전달
def index():
    print(session)
    if session.get('user'):
        return redirect(url_for('profile'))
    
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')

        # print(id, pw)

        user = next((u for u in users if u['id']==id and u['pw']==pw), None)
        if user:
            session['user'] = user #로그인한 사용자 정보를 세션에 저장
            return redirect(url_for('profile'))
        else:
             return '로그인에 실패하였습니다.'
    return render_template('index.html')

@app.route('/profile')
def profile():
     user = session.get('user') # 이건 아까 우리가 저장한 정보
     print(user)
     if user:
        print(session)
        return render_template('dashboard.html', user_name=user['name'])
     else:
        return '로그인 안 된 사용자'
@app.route('/edit_profile')
def edit_page():
    user = session.get('user')
    print('프로필 수정 페이지.', user)
    if user:
        return render_template('edit_profile.html', user=user)
    flash('로그인 먼저 하세요.')
    return redirect(url_for('index'))

@app.route('/api/edit', methods=['GET','POST'])
def edit_profile():
    print('프로필 수정 된거 아냐?')
    user = session.get('user')
    name = request.form.get('name')
    pw = request.form.get('pw')
    print(name, pw)
    if user:
        user
        user['name'] = name
        user['pw'] = pw
        flash('사용자 정보가 수정되었습니다.')
        return redirect(url_for('profile'))
    else:
        flash('로그인 먼저 하세요')
        return redirect(url_for('index'))
     
@app.route('/logout')
def logout():
    print(request)
    if request:
        session.pop('user', None)
        # session.clear()
    return redirect(url_for('index'))
# 미션1. 로그인된 사용자는 dashboard를 만들어서 안녕하셍 00
# 미션2. /에 접속 해서 로그인 된 사용자면 바로 dashboard로 보내기
# 미션3. 로그아웃 ㅜㄱ현. /logout a href
# 숙제. 프로필 화면에서 이름, 비번 수정

if __name__=='__main__':
        app.run(debug=True)