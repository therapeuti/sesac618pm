from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET']) # GET은 기본값. 아무것도 안 넣어도 get 받을 수 있음.
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name') # POST로 전달 된 폼에서 name이 키인 것
    age = request.form.get('age')
    print(request.form)
    return f'안녕하세요, {age}세 {name}님'


if __name__=='__main__':
    app.run(debug=True)