from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 /접속하면 아래 함수를 호출해줘.
def home():
    return '<h1>Hello, Flask!</h1>'

@app.route('/user')
def user():
    return '<h1>Hello, User!</h1>'

@app.route('/product')
def product():
    return '<h1>Hello, Product!</h1>'

if __name__=="__main__":
    print(__name__)
    print('여기가 메인 함수')
    app.run()
    # app.run(host="0.0.0.0", debug=True) # 외부에서 접속 가능..

# 5000번 포트가 기본값. 맥북에서는 안 될 수 있음. 5000번 포트 쓰는 소프트웨어가 있어서?
# node.js는 3000번 포트가 기본값