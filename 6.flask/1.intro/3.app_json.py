from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile' : '010-1234-5678'},
    {'name': 'Bob', 'age': 35, 'mobile' : '010-2456-5768'},
    {'name': 'Charlie', 'age': 30, 'mobile' : '010-1284-5178'}
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):
    # 이름일치하는지 확인하는 코드    
    u = None
    for user in users:
        if name.lower() == user['name'].lower():
            u = user
            break # 반복문을 중단
    if u:
        return jsonify(u)
    else:
        return jsonify({'error':'user not found'}), 404
    

@app.route('/user/<int:age>')
def get_user_by_age(age):
    print('나이: ', age)
    user = None
    for u in users:
        if int(age) == u['age']:
            user = u
            break
    if user:
        return jsonify(user)
    else:
        return jsonify({'error':'User not found'}), 404
        




if __name__=='__main__':
    app.run(debug=True, port=5000)