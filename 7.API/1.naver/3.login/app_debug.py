from flask import Flask, render_template, redirect, url_for, request
from flask import session
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET_KEY', 'test-key')

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
NAVER_REDIRECT_URI = os.getenv('NAVER_REDIRECT_URI')

@app.route('/')
def index():
    # 설정 상태 확인
    config_status = {
        'client_id': 'OK' if NAVER_CLIENT_ID else 'MISSING',
        'client_secret': 'OK' if NAVER_CLIENT_SECRET else 'MISSING',
        'redirect_uri': 'OK' if NAVER_REDIRECT_URI else 'MISSING'
    }
    
    user = session.get('user')
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>네이버 로그인 디버깅</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            .error {{ color: red; }}
            .success {{ color: green; }}
            .config {{ background: #f5f5f5; padding: 10px; margin: 10px 0; }}
            button {{ padding: 10px 20px; font-size: 16px; margin: 10px 0; }}
        </style>
    </head>
    <body>
        <h1>네이버 로그인 디버깅</h1>
        
        <div class="config">
            <h3>설정 상태:</h3>
            <p>CLIENT_ID: <span class="{'success' if config_status['client_id'] == 'OK' else 'error'}">{config_status['client_id']}</span></p>
            <p>CLIENT_SECRET: <span class="{'success' if config_status['client_secret'] == 'OK' else 'error'}">{config_status['client_secret']}</span></p>
            <p>REDIRECT_URI: <span class="{'success' if config_status['redirect_uri'] == 'OK' else 'error'}">{config_status['redirect_uri']}</span></p>
            
            {f'<p>실제 REDIRECT_URI: {NAVER_REDIRECT_URI}</p>' if NAVER_REDIRECT_URI else ''}
        </div>
        
        {'<div class="error"><h3>⚠️ 설정 오류</h3><p>.env 파일의 네이버 설정을 확인하세요!</p></div>' if not all([NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, NAVER_REDIRECT_URI]) else ''}
        
        {f'''
        <div>
            <h3>로그인 상태: 로그인됨</h3>
            <p>이름: {user.get('name', '없음')}</p>
            <p>이메일: {user.get('email', '없음')}</p>
            <button onclick="location.href='/logout'">로그아웃</button>
        </div>
        ''' if user else '''
        <div>
            <h3>로그인 상태: 로그인되지 않음</h3>
            <button onclick="location.href='/login_naver'">네이버로 로그인</button>
            <button onclick="location.href='/test_url'">인증 URL 테스트</button>
        </div>
        '''}
        
        <hr>
        <p><a href="/debug">상세 디버그 정보 보기</a></p>
        <p><a href="/routes">등록된 라우트 보기</a></p>
    </body>
    </html>
    '''

@app.route('/debug')
def debug():
    """상세 디버그 정보"""
    debug_info = {
        'NAVER_CLIENT_ID': NAVER_CLIENT_ID,
        'NAVER_CLIENT_SECRET': NAVER_CLIENT_SECRET[:10] + '...' if NAVER_CLIENT_SECRET else None,
        'NAVER_REDIRECT_URI': NAVER_REDIRECT_URI,
        'SESSION_SECRET_KEY': 'SET' if app.secret_key else 'NOT SET'
    }
    
    # 생성될 인증 URL
    if all([NAVER_CLIENT_ID, NAVER_REDIRECT_URI]):
        auth_url = (
            f'https://nid.naver.com/oauth2.0/authorize?'
            f'response_type=code&client_id={NAVER_CLIENT_ID}'
            f'&redirect_uri={NAVER_REDIRECT_URI}&state=xyz'
        )
    else:
        auth_url = "설정 오류로 인해 URL 생성 불가"
    
    return f'''
    <h1>디버그 정보</h1>
    <h3>환경변수:</h3>
    <pre>{debug_info}</pre>
    
    <h3>생성될 인증 URL:</h3>
    <p><a href="{auth_url}" target="_blank">{auth_url}</a></p>
    
    <h3>세션 정보:</h3>
    <pre>{dict(session)}</pre>
    
    <p><a href="/">돌아가기</a></p>
    '''

@app.route('/test_url')
def test_url():
    """인증 URL을 직접 보여주기"""
    if not all([NAVER_CLIENT_ID, NAVER_REDIRECT_URI]):
        return "설정 오류: CLIENT_ID 또는 REDIRECT_URI가 없습니다."
    
    auth_url = (
        f'https://nid.naver.com/oauth2.0/authorize?'
        f'response_type=code&client_id={NAVER_CLIENT_ID}'
        f'&redirect_uri={NAVER_REDIRECT_URI}&state=xyz'
    )
    
    return f'''
    <h1>네이버 인증 URL 테스트</h1>
    <p>아래 링크를 클릭해서 네이버 로그인이 되는지 확인하세요:</p>
    <p><a href="{auth_url}" target="_blank">{auth_url}</a></p>
    <p><a href="/">돌아가기</a></p>
    '''

@app.route('/routes')
def list_routes():
    """등록된 모든 라우트 표시"""
    routes = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        routes.append(f"{rule.rule} -> {rule.endpoint} [{methods}]")
    
    return f'''
    <h1>등록된 라우트</h1>
    <pre>{'<br>'.join(routes)}</pre>
    <p><a href="/">돌아가기</a></p>
    '''

@app.route('/login_naver')
def login_naver():
    print("=== login_naver 라우트 호출됨 ===")
    print(f"CLIENT_ID: {NAVER_CLIENT_ID}")
    print(f"REDIRECT_URI: {NAVER_REDIRECT_URI}")
    
    if not NAVER_CLIENT_ID:
        return "에러: NAVER_CLIENT_ID가 설정되지 않았습니다."
    
    if not NAVER_REDIRECT_URI:
        return "에러: NAVER_REDIRECT_URI가 설정되지 않았습니다."
    
    auth_url = (
        f'https://nid.naver.com/oauth2.0/authorize?'
        f'response_type=code&client_id={NAVER_CLIENT_ID}'
        f'&redirect_uri={NAVER_REDIRECT_URI}&state=xyz'
    )
    
    print(f"리다이렉트 URL: {auth_url}")
    
    try:
        return redirect(auth_url)
    except Exception as e:
        print(f"리다이렉트 에러: {e}")
        return f"리다이렉트 에러: {e}"

@app.route('/naver/callback')
def naver_callback():
    print("=== 네이버 콜백 호출됨 ===")
    code = request.args.get('code')
    state = request.args.get('state')
    error = request.args.get('error')
    
    print(f"code: {code}")
    print(f"state: {state}")
    print(f"error: {error}")
    
    if error:
        return f"네이버 인증 에러: {error}"
    
    if not code:
        return "인증 코드가 없습니다."
    
    # 여기서는 일단 성공했다고 표시
    return f'''
    <h1>콜백 성공!</h1>
    <p>code: {code}</p>
    <p>state: {state}</p>
    <p>이제 토큰 교환 과정을 진행합니다...</p>
    <p><a href="/">홈으로</a></p>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("=== Flask 앱 시작 ===")
    print(f"CLIENT_ID 설정됨: {'예' if NAVER_CLIENT_ID else '아니오'}")
    print(f"CLIENT_SECRET 설정됨: {'예' if NAVER_CLIENT_SECRET else '아니오'}")
    print(f"REDIRECT_URI: {NAVER_REDIRECT_URI}")
    print("http://localhost:5000 에서 앱이 실행됩니다.")
    app.run(debug=True)