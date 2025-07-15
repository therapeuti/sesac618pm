from flask import Flask, render_template, request, redirect
from models import db, User


# flask 초기화
# def create_app(): # 함수로 만든 이유가...? db 초기화때문에....?
#     app = Flask(__name__)
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
#     db.init_app(app)
#     return app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    print(users)
    return render_template('index.html', users=users)


@app.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    # 필요한 에러체크를 넣는 것이 좋음. 중복, 누락 등등
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/') # redirect(url_for('index'))가 좀 더 나음...

@app.route('/delete/<user_id>')
def delete_user(user_id):
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음: ', id)
    return redirect('/')

@app.route('/edit/<user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = db.session.get(User, user_id)
    # 에러체크.... 사용자 없으면 처리할 거...

    if request.method == 'POST':
        print('post 요청 옴')
        name = request.form.get('name')
        age = request.form.get('age')
        user.name = name
        user.age = int(age)
        db.session.commit()
        return redirect('/')
    return render_template('edit_user.html', user=user)


if __name__=='__main__':
    # app = create_app()
    app.run(debug=True)