from flask import Flask, render_template

app = Flask(__name__)
# static 폴더 이름을 변경 가능하지만 굳이 바꿀 이유가 없음.
# app = Flask(__name__, static_folder='static')
# static 폴더를 만들면, 자동으로 외부에 노출됨.
# index.html 안에서 static을 전달 할 때 하드코딩해도 되지만, url_for('static', ~~)을 사용하여 전달하는게 더 좋은 코딩. 혹시 static 폴더 이름이 바뀌어도 변경할 필요가 없음.

@app.route('/')
def home():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)