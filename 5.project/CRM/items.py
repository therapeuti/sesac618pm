# from flask import Flask
from flask import Blueprint
from flask import render_template, request, url_for, redirect
from database import *
import math
import logging

logging.basicConfig(level=logging.DEBUG,
                       format='%(asctime)s [%(levelname)s] %(message)s',
                       datefmt='%Y-%m-%d %H-%M-%S')

# app = Flask(__name__)
items_bp = Blueprint('items', __name__)

count_per_page = 10
# @app.route('/')
@items_bp.route('/')
def items_index():
    page = request.args.get('page', default=1, type=int)
    orderby = request.args.get('orderby', default='name', type=str)
    filtering = {'page':page, 'orderby':orderby}
    items, count_items = get_items_list(count_per_page, filtering)
    end_page = math.ceil(count_items / count_per_page)
    return render_template('items_index.html', items=items, end_page=end_page, current_page=page)

@items_bp.route('/info/<id>')
def item_info(id):
    logging.debug('아이템 정보 요청')
    item = get_item_by_id(id)
    return render_template('item_info.html', item=item)

# if __name__=='__main__':
#     app.run(debug=True)

