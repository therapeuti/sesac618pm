from flask import Flask, render_template

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile' : '010-1234-5678'},
    {'name': 'Bob', 'age': 35, 'mobile' : '010-2456-5768'},
    {'name': 'Charlie', 'age': 30, 'mobile' : '010-1284-5178'}
]

@app.route('/')
def index():
    return render_template('index3.html', users=users)

if __name__=='__main__':
    app.run(debug=True, port=5000)