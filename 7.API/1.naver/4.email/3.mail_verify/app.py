from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import random

load_dotenv()


app = Flask(__name__)
app.secret_key = "dfgh"

app.config['MAIL_SERVER'] = "smtp.naver.com" # smtp 거나 imap이거나
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

mail = Mail(app)

print("MAIL_SERVER:", app.config['MAIL_SERVER'])
print("MAIL_PORT:", app.config['MAIL_PORT'])
print("USERNAME:", app.config['MAIL_USERNAME'])
print("PASSWORD:", app.config['MAIL_PASSWORD'])



@app.route('/')
def signup():
    
    return render_template('index.html')


@app.route('/send-code', methods=['POST'])
def send_code():

    
    email = request.get_json()# 사용자로ㅜ터 받아오기
    print(email)

    # 미션1. 6자리 숫자 랜덤값 만들기
    code = random.randint(100000, 999999)
    print(code)

    session['code'] = code
    
    msg = Message('회원 가입 인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f'인증코드: {code}'
    mail.send(msg)

    return jsonify({'message': '인증 코드가 전송되었습니다.'})


@app.route('/verify-code', methods=['POST'])
def verify_code():

    # 미션2. 내가 보낸 코드와 입력된 코드가 같은 지 확인
    user_code = request.get_json()
    print(user_code, type(user_code))
    code2 = session.get('code')
    print(code2, type(code2))

    # 미션2-1. 저장된 세션으로부터 코드 가져와서, 사용자 입력한 코드랑 내가 저장해둔 코드랑 같은지 확인
    if int(user_code) == code2:
        print('인증성공')
        return jsonify({'message': '인증 성공'})
    else:
        print('인증실패')
        return jsonify({'message': '인증 실패'})




if __name__=='__main__':
    app.run(debug=True)