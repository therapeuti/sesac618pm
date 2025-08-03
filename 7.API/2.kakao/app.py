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
kapi_host="https:/kapi.kakao.com"
kauth_host="https://kauth.kakao.com"


@app.route('/')
def index():
    user = session.get('access_token')
    if user:
        return render_template('index.html', user=user)


    return render_template('index.html')

@app.route('/login_kakao')
def login_kakao():
    kakao_auth_url = (
        # 카카오 로그인 주소 엔드포이트 찾아오기, 또한 필요한 입력값들 확인하기
        f'https://kauth.kakao.com/oauth/authorize?'
        f'client_id={KAKAO_CLIENT_ID}&'
        f'redirect_uri={KAKAO_REDIRECT_URI}&'
        f'response_type=code&'
        f'scope=profile_nickname'
    )
    return redirect(kakao_auth_url)


@app.route('/auth/kakao/callback') # 카카오 인증 끝난 후에 돌아올 곳
def kakao_callback():

    # 인가 코드 발급 요청에 필요한 파라미터 구성
    data = {
        'grant_type': 'authorization_code',  # 인증 방식 고정값
        'client_id': KAKAO_CLIENT_ID,              # 내 앱의 REST API 키
        'redirect_uri': KAKAO_REDIRECT_URI,        # 등록된 리다이렉트 URI
        'client_secret': KAKAO_CLIENT_SECRET,      # 선택: 클라이언트 시크릿(Client Secret) 사용 시 추가
        'code': request.args.get("code")     # 전달받은 인가 코드
    }

    # 카카오 인증 서버에 액세스 토큰 요청
    resp = requests.post(kauth_host + "/oauth/token", data=data)

    # 발급받은 액세스 토큰을 세션에 저장 (로그인 상태 유지 목적)
    session['access_token'] = resp.json()['access_token']
    return redirect("/?login=success")




    # # 카카오에게 코드 검증 후 토큰을 발급받을 엔드포인트 및 입력값 확인
    # token_url = (
    # )

    # # 성공했다면 ㅏㅅ용ㅈ ㅏ정보 요청
    # user_info_url = ()

    # user_info = requests.get()


    # # 로그인 ㅓㅅㅇ공
    # print(user_info)
    # return '로그인 성공' # 어디로 보낼 지 알아서 처리

# 액세스 토큰을 사용해 로그인한 사용자의 정보 조회 요청
@app.route("/profile")
def profile():
    # 사용자 정보 요청
    headers = {
        'Authorization': 'Bearer ' + session.get('access_token', '')  # 세션에 저장된 액세스 토큰 전달
    }

    user_info = requests.get(kapi_host + "/v2/user/me", headers=headers)  # 사용자 정보 조회 API 요청 전송
    print(user_info)

    return user_info.text  # 조회한 사용자 정보를 클라이언트에 반환
    # return redirect(url_for('index'))


# @app.route('/profile')
# def profile():
#     # 위리 내용 다 끝나면 ㅏㅅ용자 정보 저장하ㅗㄱ, 수정하고 등등 기능 추가
#     return render_template('profile.html', user=user)


#로그아웃 추가
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__=='__main__':
    app.run(debug=True)
