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
def store_index():
    page = request.args.get('page', default=1, type=int)
    filtering = {'page':page}
    stores, count_stores = get_stores_list(count_per_page, filtering)
    end_page = math.ceil(count_stores / count_per_page)
    return render_template('store_index.html', stores=stores, end_page=end_page, current_page=page)


if __name__=='__main__':
    app.run(debug=True)

