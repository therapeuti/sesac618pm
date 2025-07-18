from flask import Flask, render_template, request, url_for, redirect
from database import *
import math
import logging

logging.basicConfig(level=logging.DEBUG,
                       format='%(asctime)s [%(levelname)s] %(message)s',
                       datefmt='%Y-%m-%d %H-%M-%S')

app = Flask(__name__)

count_per_page = 10
@app.route('/')
def orders_index():
    page = request.args.get('page', default=1, type=int)
    filtering = {'page':page}
    orders, count_orders = get_orders_list(count_per_page, filtering)
    end_pages = math.ceil(count_orders / count_per_page)
    return render_template('orders_index.html', orders=orders, end_page=end_pages, current_page=page)


if __name__=='__main__':
    app.run(debug=True)

