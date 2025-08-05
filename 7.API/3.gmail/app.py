from flask import Flask, render_template, request, jsonify, session
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import random
import string

load_dotenv()


app = Flask(__name__)
app.secret_key = "dfgh"

app.config['MAIL_SERVER'] = "smtp.gmail.com" # smtp 거나 imap이거나
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('GMAIL_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('GMAIL_PASSWORD')

mail = Mail(app)

print("MAIL_SERVER:", app.config['MAIL_SERVER'])
print("MAIL_PORT:", app.config['MAIL_PORT'])
print("USERNAME:", app.config['MAIL_USERNAME'])
print("PASSWORD:", app.config['MAIL_PASSWORD'])



@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/forgot_pw')
def forgot_password():

    return render_template('forgot_pw.html')


@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.get_json() # 사용자로부터 받아오기
    print(email)

    code = random.randint(100000, 999999)
    print(code)

    session['email'] = email
    session['code'] = str(code)
    msg = Message('인증 코드', sender=app.config['MAIL_USERNAME'], recipients=[email])
    msg.body = f'인증코드: {code}'
    mail.send(msg)
    return jsonify({'message': '인증 코드가 전송되었습니다.'})


@app.route('/verify-code', methods=['POST'])
def verify_code():
    user_code = request.get_json()
    print(user_code, type(user_code))
    code2 = session.get('code')
    print(code2, type(code2))

    if user_code == code2:
        print('인증성공')
        return jsonify({'message': '인증 성공', 'status': 'true'})
    else:
        print('인증실패')
        return jsonify({'message': '인증 실패', 'status': 'false'})

@app.route('/temporary_pw', methods=['POST'])
def temporary_password():
    user_code = request.get_json()
    print(user_code, type(user_code))
    code2 = session.get('code')
    print(code2, type(code2))

    if user_code == code2:
        print('인증성공')
        email = session.get('email')
        print(email)

        # 사용할 문자 집합: 대문자 + 숫자
        chars = string.ascii_uppercase + string.digits  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        # 임시 비밀번호 생성
        temporary_pw = ''.join(random.choices(chars, k=12))

        session['temporary_pw'] = str(temporary_pw)
        msg = Message('임시 비밀번호', sender=app.config['MAIL_USERNAME'], recipients=[email])
        msg.body = f'임시 비밀번호: {temporary_pw}'
        mail.send(msg)
        return jsonify({'message': '임시 비밀번호가 전송되었습니다.'})
    else:
        print('인증실패')
        return jsonify({'message': '인증 실패'})




if __name__=='__main__':
    app.run(debug=True)