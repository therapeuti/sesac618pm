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
def orderitems_index():
    page = request.args.get('page', default=1, type=int)
    filtering = {'page':page}
    orderitems, count_orderitems = get_orderitems_list(count_per_page, filtering)
    end_page = math.ceil(count_orderitems / count_per_page)
    return render_template('orderitems_index.html', orderitems=orderitems, end_page=end_page, current_page=page)


if __name__=='__main__':
    app.run(debug=True)

