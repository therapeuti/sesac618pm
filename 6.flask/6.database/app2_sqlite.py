from flask import Flask, render_template, request, redirect
from database import *

app = Flask(__name__)

# db 초기화는 어디서?
create_table()

# @app.before_first_request
# def initialise():
#     create_table()
#     print('users 테이블 생성')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # POSt 요청 처리
        name = request.form['name']
        age = int(request.form['age'])

        # 사용자 추가
        insert_user(name, age)
        return redirect('/') # 추가 끝났으면 페이지 다시 불러오기

    users = get_users()
    print(users)
    #get 요청 처리
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # users 변수 뒤져서 id 찾아서 지움
    delete_user_by_id(user_id)

    return redirect('/')


@app.route('/update/<int:user_id>', methods=['GET','POST'])
def update(user_id):
    user = get_user_by_id(user_id)
    if not user:
        print('사용자를 찾을 수 없습니다.')

    # method 분기점 나눔. post
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = request.form.get('age')

        update_user(user_id, new_name, new_age)
        
        return redirect('/')    

    return render_template('update_user.html', user=user)

if __name__=='__main__':
    # create_table()
    # print('user 테이블 생성?')  # debug 모드에서는 두 번 불림.
    app.run(debug=True)