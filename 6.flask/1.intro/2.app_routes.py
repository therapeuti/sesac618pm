from flask import Flask

app = Flask(__name__)

@app.route('/') # 사용자가 /접속하면 아래 함수를 호출해줘.
def home():
    return '<h1>Hello, Flask!</h1>'

@app.route('/user')
def user():
    return '<h1>Hello, User!</h1>'

@app.route('/user/<username>') # 따로 정의하지 않으면 문자열 타입. 바꾸고 싶으면 타입 지정 가능.
def username(username): # @ flask에서 데코레이터에서 정한 변수명. <변수명>으로 함수 인자로 전달
    print(username)
    return f'<h1>Hello, {username}!</h1>' # 서버사이드 렌더링. (서버에서 필요한 html을 만들어줌...?)

@app.route('/user/<int:age>') # 따로 정의하지 않으면 문자열 타입. 바꾸고 싶으면 타입 지정 가능.
def userage(age): # @ flask에서 데코레이터에서 정한 변수명. <변수명>으로 함수 인자로 전달
    print(age)
    return f'<h1>Hello, {age}살 고객님!</h1>' # 서버사이드 렌더링. (서버에서 필요한 html을 만들어줌...?)

@app.route('/user/<float:weight>') # 따로 정의하지 않으면 문자열 타입. 바꾸고 싶으면 타입 지정 가능.
def userweight(weight): # @ flask에서 데코레이터에서 정한 변수명. <변수명>으로 함수 인자로 전달
    if weight > 60:
        message = "몸무게가 60이 넘네요"
    elif weight < 40:
        message= "몸무게나 너무 적게 나가네요. 밥 좀 잘 먹으세요"    
    print(weight)
    return f'{weight}kg의 고객님! {message}</h1>' # 서버사이드 렌더링. (서버에서 필요한 html을 만들어줌...?)

@app.route('/user/<name>/<int:age>/<float:weight>')
def greet_user(name, age, weight):
    return f"<H1>안녕하세요!</H1><h2>사용자정보</h2><ul><li>이름: {name}</li><li>나이: {age}</li><li>몸무게: {weight}</li>"    


@app.route('/product')
def product():
    return '<h1>Hello, Product!!</h1>'

if __name__=="__main__":
    print(__name__)
    print('여기가 메인 함수')
    app.run(debug=True)  # debug true인 상태로 릴리즈 하면 안 됨. 에러메시지가 다 웹브라우저에 뜨고, 코드 노출됨.

# 5000번 포트가 기본값. 맥북에서는 안 될 수 있음. 5000번 포트 쓰는 소프트웨어가 있어서?
# node.js는 3000번 포트가 기본값