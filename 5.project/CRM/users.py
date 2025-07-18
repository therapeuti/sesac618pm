# from flask import Flask
from flask import Blueprint, current_app
from flask import send_from_directory, jsonify, request
from database import *
import math

logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s [%(levelname)s] %(messages)s',
                   datefmt='%Y-%m-%d %H-%M-%S')

# app = Flask(__name__)
users_bp = Blueprint('users', __name__)

# @app.route('/')
@users_bp.route('/')
def users():
    logging.debug('시작!?')
    return send_from_directory(current_app.static_folder, 'users_index.html')


count_per_page = 10
# @app.route('/api/getUsers/')
@users_bp.route('/api/getUsers')
def send_users():
    page = request.args.get('page', default=1, type=int)
    u_id = request.args.get('id', type=str)
    name = request.args.get('name', type=str)
    address = request.args.get('address', type=str)
    gender = request.args.get('gender', type=str)
    orderby = request.args.get('orderby', default='name', type=str)
    logging.debug(f'GET 파라미터 : {page}, {u_id}, {name}, {address}, {gender}, {orderby}')
    
    filtering = {}
    filtering['page'] = page
    filtering['orderby'] = orderby
    if u_id:
        filtering['id'] = u_id
    if name:
        filtering['name'] = name
    if address:
        filtering['address'] = address
    if gender:
        filtering['gender'] = gender

    logging.debug(filtering)

    users, count_users = get_users_list(count_per_page, filtering)
      
    total_pages = math.ceil(count_users / count_per_page)
    logging.debug(f'send_user() : {users}')
    logging.debug(f'전체 페이지 수: {total_pages}')
    return jsonify({'users':users, 'total_pages':total_pages})


# if __name__=='__main__':
    # app.run(debug=True)