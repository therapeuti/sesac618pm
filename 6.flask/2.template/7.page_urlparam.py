from flask import Flask

app = Flask(__name__)

# 더미 유저 100명 생성

@app.route('/')
def index():
    return 'hello'

if __name__=='__main__':
    app.run(debug=True)


