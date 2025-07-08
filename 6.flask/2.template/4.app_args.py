from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile' : '010-1234-5678'},
    {'name': 'Bob', 'age': 35, 'mobile' : '010-2456-5768'},
    {'name': 'Charlie', 'age': 30, 'mobile' : '010-1284-5178'}
]

@app.route('/') # GET 파라미터 요청이 함께 온다는 것....???
def index():
    name = request.args.get('name')
    print('name: ', name)
    user = None
    if name:
        for i in users:
            print('i: ', i)
            if i['name'].lower() == name.lower():
                print(i['name'])
                user = i
                break



    return render_template('index4.html', users=users, user=user )

if __name__=='__main__':
    app.run(debug=True, port=5000)