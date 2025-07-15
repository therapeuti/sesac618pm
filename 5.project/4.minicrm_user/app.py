from flask import Flask, render_template, request
import database as db
import math


app = Flask(__name__)

@app.route('/')
def index():
    page = int(request.args.get('page', default=1)) # page 넘어갈 경우 예외처리
    count = 10 # 한 페이지에 출력할 데이터 개수
    users = db.get_users(page, count)
    user_count = db.get_user_count()
    print(user_count[0])
    total_pages = math.ceil(int(user_count[0]) / count)
    return render_template('index.html', users=users, page=page, total_pages=total_pages)


if __name__=='__main__':
    app.run(debug=True)