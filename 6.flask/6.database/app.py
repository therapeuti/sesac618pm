from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = []
next_id = 1 # 자동 증가

@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id # 글로벌 변수의 내용을 수정하려면  글로벌 변수라고 선언 필요
    if request.method == 'POST':
        # POSt 요청 처리
        name = request.form['name']
        age = int(request.form['age'])

        # 사용자 추가
        users.append({'id': next_id, 'name': name, 'age': age})
        next_id += 1
        return redirect('/') # 추가 끝났으면 페이지 다시 불러오기

    #get 요청 처리
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    # users 변수 뒤져서 id 찾아서 지움
    for i in range(len(users)):
        if users[i]['id'] == user_id:
            del users[i]

    # for i, user in enumerate(users)

    # users = [u for u in users if u['id'] != user_id] # 코드 한 줄이긴 하지만, 리스트를 새로 만들어야 하기 때문에 속도가 느림
    return redirect('/')


@app.route('/update/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    # users 변수 뒤져서 수정
    # method 분기점 나눔. post
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_age = request.form.get('age')
        for user in users:
            if user['id'] == user_id:
                user['name'] = new_name
                user['age'] = new_age
                break
        return redirect('/')    

    # get 요청 처리
    if request.method == 'GET':
        for u in users:
            if u['id'] == user_id:
                user = u
                break

        # users = next((u for u in users if u['id'] == user_id), None)  제너레이터?????
        # print(user)
    return render_template('update_user.html', user=user)

if __name__=='__main__':
    app.run(debug=True)