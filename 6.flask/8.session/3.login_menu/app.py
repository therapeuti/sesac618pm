from flask import Flask, render_template, redirect, url_for, request
from flask import session

app = Flask(__name__)
app.secret_key = 'd'

users = [
    {'name': 'taemin', 'id':'tm', 'pw':'123'}
]

items = [
    {'id': 'prod-001', 'name': '사과', 'price': 1000},
    {'id': 'prod-002', 'name': '바나나', 'price': 2000},
    {'id': 'prod-003', 'name': '딸기', 'price': 3000}
]

carts = [
    # {'id': id, 'count': count}
]


@app.route('/')
def home():
    return render_template('index.html', login=login)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        pw = request.form.get('pw')

        user = next((u for u in users if u['id']==id and u['pw']==pw), None)
        if user:
            session['user'] = user
            print(session)
            return redirect(url_for('user', login=logout))
        else:
            error = '로그인 실패'
            return render_template('login.html', error=error)
    # if error:
    #     return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    print(session)
    # session.pop('user', None) # user가 없으면 KeyError 발생. 
    return redirect(url_for('login'))


@app.route('/user')
def user():
    user = session.get('user')
    if user:
        user = session['user']
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user, items=items)

@app.route('/add-to-cart/<id>', methods=['GET', 'POST'])
def add_to_cart(id):
    user = session.get('user')
    print(id)
    if not user:
        error = '로그인부터 하세요'
        return redirect(url_for('login', error=error))
    print(len(carts))
    if len(carts) != 0 :
        for item in carts:
            if id == item['id']:
                item['count'] += 1
                session['carts'] = carts
        carts.append({'id': id, 'count': 1})
        session['carts'] = carts
    else:
        carts.append({'id': id, 'count': 1})
        session['carts'] = carts
    print('carts: ', carts)
    print('세션 내 carts: ', session['carts'])
    return render_template('product.html', user=user, items=items)

@app.route('/carts')
def in_carts():
    user = session.get('user')
    if not user:
        error = '로그인부터 하세요'
        return redirect(url_for('login', error=error))
    items_in_cart = session.get('carts')
    print(items_in_cart)


    return render_template('cart.html', items_in_cart=items_in_cart)



if __name__=='__main__':
    app.run(debug=True)