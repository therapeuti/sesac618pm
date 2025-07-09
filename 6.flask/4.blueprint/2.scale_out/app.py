from flask import Flask, render_template
from user.user_route import user_bp
from admin.admin_route import admin_bp
from product.product_route import product_bp

app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')
# app.register_blueprint(product_bp, url_prefix='product')

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)