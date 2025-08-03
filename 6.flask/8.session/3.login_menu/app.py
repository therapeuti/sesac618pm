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

cart = [
    # {'id': id, 'count': count}
]
# id_in_cart = {}


@app.route('/')
def home():
    return render_template('index.html', login=login)

@app.route('/login', methods=['GET','POST'])
def login():
    user = session.get('user')
    if user:
        return redirect(url_for('user'))
    
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
    
    print(len(cart))
    for item in items:
        if item['id'] == id:
            for i in cart:
                if id == i['id']:
                    i['count'] += 1
                    session['cart'] = cart
                    print('장바구니 : ', session['cart'])
                    return redirect(url_for('product'))
            item['count'] = 1
            cart.append(item)
            session['cart'] = cart
    print('장바구니 : ', session['cart'])
    return redirect(url_for('product'))


@app.route('/cart')
def in_cart():
    user = session.get('user')
    if not user:
        error = '로그인부터 하세요'
        return redirect(url_for('login', error=error))
    
    print('세션 장바구니 ', session['cart'])
    items_in_cart = session['cart']
    print('장바구니 : ', items_in_cart)
    total_price = 0
    for item in items_in_cart:
        price = item['count'] * item['price']
        total_price += price

    return render_template('cart.html', items_in_cart=items_in_cart, total_price=total_price)


@app.route("/empty_cart")
def empty_cart():
    session.pop('cart', None)
    return redirect(url_for('in_cart'))

@app.route('/plus/<id>')
def plus(id):
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    
    print(f"개수 추가 전 장바구니 : {session['cart']}")
    items_in_cart = session['cart']
    for item in items_in_cart:
        print(item)
        if item['id'] == id:
            print(f'개수 추가한 아이템: {item}')
            item['count'] += 1
            print(f' 개수 추가 후 세션 내 장바구니 아이템: {items_in_cart}')
            session['cart'] = items_in_cart
            break

    return redirect(url_for('in_cart'))



@app.route('/subtraction/<id>')
def subtraction(id):
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    
    print(f"개수 감소 전 장바구니 : {session['cart']}")
    items_in_cart = session['cart']
    for item in items_in_cart:
        print(item)
        if item['id'] == id:
            print(f'개수 감소한 아이템: {item}')
            item['count'] -= 1
            print(f' 개수 감소 후 세션 내 장바구니 아이템: {items_in_cart}')
            session['cart'] = items_in_cart
            break

    return redirect(url_for('in_cart'))

@app.route('/delete_row/<id>')
def delete_row(id):
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    
    print(f"삭제 전 장바구니 : {session['cart']}")
    items_in_cart = session['cart']
    for item in items_in_cart:
        print(item)
        if item['id'] == id:
            print(f'삭제하기로 선택한 아이템: {item}')
            items_in_cart.remove(item)
            print(f'삭제 후 세션 내 장바구니 아이템: {items_in_cart}')
            session['cart'] = items_in_cart
            break

    return redirect(url_for('in_cart'))



if __name__=='__main__':
    app.run(debug=True)