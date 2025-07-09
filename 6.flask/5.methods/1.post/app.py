from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# 사용자 목록
users = [
    {'name': "Alice", 'id': 'alice123', 'pw':'12345678'},
    {'name': "Alicia", 'id': 'alicia456', 'pw':'asdfghjkl'},
    {'name': "Ali", 'id': 'aligood', 'pw':'qwertyuiop'}
    # 사용 이름, 아이디, 암호 3명 이상, 아래에서 id pw 맞는지 체크, 맞으면 로그인성공->사용자페이지로 이동, 실패하면 로그인실패 출력
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        id = request.form["id"]
        pw = request.form['pw']
        print(f'요청된 아이디{id} 비번{pw}')
        user = None
        for u in users:
            if id == u['id'] and pw == u['pw']:
                user = u
                print(user)
                print(type(user))
                return render_template( 'user.html', user=user)
        if user is None:
            print('로그인실패')
            loginfail = '로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요'
            return render_template('login.html', loginfail=loginfail)
    else:
        return render_template('login.html')
    
@app.route('/user')
@app.route('/user/<user>')
def user(user=None): # user 초기값 할당
    print(user)
    print(type(user))
    # user = jsonify(user)
    user = dict(user)
    print(type(user))
    return render_template('user.html', user=user)

@app.route('/product')
def product():
    return render_template('product.html')

if __name__=='__main__':
    app.run(debug=True)