
from flask import Flask, render_template, request
import math

app = Flask(__name__)

# 더미 유저 100명 생성
users = [{'id': i, 'name': f'user{i}', 'age': 20+i % 10, 'mobile':f'010-0000-{str(i).zfill(4)}'} for i in range(1, 108)]
max_page = math.ceil(len(users)//10)

# http://localhost:5000/?page=1
@app.route('/')
def index():
    page = request.args.get('page', default=None, type=int)
    print(page)
    start = 0
    end = None
    if page:
        start = page*10 - 10
        end = page*10

       
    return render_template('users copy.html', users=users[start:end], page=page, max_page=max_page)

if __name__=='__main__':
    app.run(debug=True)


