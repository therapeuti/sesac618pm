from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile' : '010-1234-5678'},
    {'name': 'Alice', 'age': 30, 'mobile' : '010-1564-5678'},
    {'name': 'Bob', 'age': 35, 'mobile' : '010-2456-5768'},
    {'name': 'Charlie', 'age': 30, 'mobile' : '010-1284-5178'},
    {'name': 'Danny', 'age': 30, 'mobile' : '010-1222-5178'}
]

@app.route('/') # GET 파라미터 요청이 함께 온다는 것....???
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    phone = request.args.get('mobile')
    print('name: ', name)
    print('age: ', age)
    filtered_users = users

    # 전체목록에서 이름비교
    # 위 결과에서 나이 비교
    # 위 결과에서 성별 비교...
    if name:
        filtered_users = [u for u in filtered_users if name.lower() == u['name'].lower()] 

    if age:
        filtered_users = [u for u in filtered_users if int(age) == u['age']]

    if phone:
        filtered_users = [u for u in filtered_users if phone in u['mobile']]

    return render_template('index6.html', users=filtered_users)

if __name__=='__main__':
    app.run(debug=True, port=5000)