from flask import Flask, send_from_directory, jsonify, request
from database import *
import math

logging.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s [%(levelname)s] %(messages)s',
                   datefmt='%Y-%m-%d %H-%M-%S')

app = Flask(__name__)

@app.route('/')
def index():
    logging.debug('시작!?')
    return send_from_directory(app.static_folder, 'index.html')


count_per_page = 10
@app.route('/api/getUsers')
def send_users():
    page = request.args.get('page', default=1)
    users = get_users(count_per_page, page)
    logging.debug(f'send_user() : {users[0]['id'], users[0]['name']}')
    return jsonify(users)

@app.route('/api/pages')
def send_pages():
    all_users = get_count_users()
    total_pages = math.ceil(all_users // count_per_page)
    logging.debug(f'전체 페이지 수: {total_pages}')
    return jsonify({'data': total_pages})

if __name__=='__main__':
    app.run(debug=True)