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
    print('name: ', name)
    print('age: ', age)
    user_data = users
    if name and age:
        user_data = [i for i in users if i['name']==name and i['age']==age]
    elif name and (age == ''):
        user_data = [i for i in users if i['name'].lower()==name.lower()]
    elif age and (name == ''):
        user_data = [i for i in users if i['age']==int(age)]
    
    return render_template('index5.html', users=user_data )

if __name__=='__main__':
    app.run(debug=True, port=5000)