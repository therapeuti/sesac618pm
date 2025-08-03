from flask import Flask, render_template, redirect, url_for, request # 클라이언트가 나한테 요청할 때
from flask import session
from dotenv import load_dotenv
import os
import requests # 내가 남한테 요청할 때
import database as db

# TODO: sqlite에 사용자가 있는지 확인하고, 있으면 그 정보 가져와서 세션에 저장. 없으면 DB에 삽입.
# 확장시킬 경우, 사용자 없으면 회원가입 페이지로 보내서 추가 정보 입력받아 DB에 저장

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
NAVER_REDIRECT_URI = os.getenv('NAVER_REDIRECT_URI')

@app.route('/')
def index():    
    user = session.get('user')
    if user:
        return render_template('index.html', user=user)
    return render_template('index.html')

@app.route('/login_naver')
def login_naver():
    # 실제 네이버 로그인 인증 할 주소
    auth_url = (
        f'https://nid.naver.com/oauth2.0/authorize?'
        f'response_type=code&client_id={NAVER_CLIENT_ID}'
        f'&redirect_uri={NAVER_REDIRECT_URI}&state=xyz'
    )
    return redirect(auth_url)

@app.route('/naver/callback') # 네이버 인증 끝난 후에 돌아올 곳
def naver_callback():
    code = request.args.get('code') # 서버가 인증 성공의 대가로 준 값
    state = request.args.get('state') # 내 사이트에서 갔다 온건지 확인용.
    print(code, state)
    # 내가 네이버와 앞으로 대화하기 위한 인증 토큰 요청( code를 검증한 이후 맞으면 서버는 토큰을 줌)
    token_url = (
        f'https://nid.naver.com/oauth2.0/token?'
        f'grant_type=authorization_code&client_id={NAVER_CLIENT_ID}'
        f'&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}'
    )

    token_response = requests.get(token_url).json()
    print(token_response)
    access_token = token_response.get('access_token')

    # 사용자가 제대로 인증하고 온 것 확인했으니, 네이버에게 해당 사용자 정보 요청
    headers = {"Authorization": f'Bearer {access_token}'}
    profile = requests.get('https://openapi.naver.com/v1/nid/me',
        headers=headers).json()

    print(f'최종적으로 받아온 사용자 정보: {profile}')

    # 세션에 저장
    session['user'] = profile['response']
    user = session.get('user')

    # db.create_users()    
    db.insert_user(user)

    return redirect(url_for('index'))

@app.route('/edit_profile')
def edit_profile():
    user = session.get('user')
    if user:
        return render_template('profile.html', user=user)

    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update():
    print(request.form)
    nickname = request.form.get('nickname')
    age = request.form.get('age')    
    gender = request.form.get('gender')
    email = request.form.get('email')
    name = request.form.get('name')
    birthday = request.form.get('birthday')

    user = session.get('user')
    print(user)

    user['nickname'] = nickname
    user['age'] = age
    user['gender'] = gender
    user['email'] = email
    user['name'] = name
    user['birthday'] = birthday

    session['user'] = user

    print(session)

    updated_user = (nickname, age, gender, email, name, birthday)
    db.update_user(updated_user)


    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    user = session.get('user')
    if user:
        session.clear()
        return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)
