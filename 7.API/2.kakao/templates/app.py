from flask import Flask, render_template, redirect, url_for, request # 클라이언트가 나한테 요청할 때
from flask import session
from dotenv import load_dotenv
import os
import json
import requests # 내가 남한테 요청할 때

# TODO: sqlite에 사용자가 있는지 확인하고, 있으면 그 정보 가져와서 세션에 저장. 없으면 DB에 삽입.
# 확장시킬 경우, 사용자 없으면 회원가입 페이지로 보내서 추가 정보 입력받아 DB에 저장

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY')

KAKAO_CLIENT_ID = os.getenv('KAKAO_CLIENT_ID')
KAKAO_CLIENT_SECRET = os.getenv('KAKAO_CLIENT_SECRET')
KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')
KAKAO_REST_API = os.getenv('KAKAO_REDIRECT_URI')

@app.route('/')
def index():

    kakao_auth_url = (
        # 카카오 로그인 주소 엔드포이트 찾아오기, 또한 필요한 입력값들 확인하기
    )
    return render_template('index.html')


@app.route('/auth/kakao/callback') # 카카오 인증 끝난 후에 돌아올 곳
def kakao_callback():
    code = request.args.get('code') # 서버가 인증 성공의 대가로 준 값
    print('code: ', code)


    # 카카오에게 코드 검증 후 토큰을 발급받을 엔드포인트 및 입력값 확인
    token_url = (
    )

    # 성공했다면 ㅏㅅ용ㅈ ㅏ정보 요청
    user_info_url = ()

    user_info = requests.get()


    # 로그인 ㅓㅅㅇ공
    print(user_info)
    return '로그인 성공' # 어디로 보낼 지 알아서 처리


@app.route('/profile')
def profile():
    # 위리 내용 다 끝나면 ㅏㅅ용자 정보 저장하ㅗㄱ, 수정하고 등등 기능 추가
    return render_template('profile.html', user=user)


#로그아웃 추가
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)
