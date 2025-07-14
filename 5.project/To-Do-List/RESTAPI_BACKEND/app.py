from flask import Flask, jsonify, send_file, request
from database import *

app = Flask(__name__)


create_table()

@app.route('/')
def index():
    return send_file('todolist.html')

@app.route('/send_data')
def send_data():
    todolist = get_todolist()
    print(todolist)
    return jsonify({'data':todolist})

@app.route('/add', methods=['POST'])
def add_todolist():
    print('메소드 받았니?')
    print(request)
    data = request.get_json()
    print(data)
    insert_todo(data['todo'], data['status'], data['date'])
    print(get_todolist())
    return '', 204 # 204 no content 클라이언트에게 반환할 데이터 없음


@app.route('/delete', methods=['DELETE'])
def delete_todolist():
    print(request)
    print(request.data)
    data = request.get_json()
    print(data)
    print(data['todo'])
    delete_todo(data['todo'])
    return '', 204


@app.route('/edit_status', methods=['PUT'])
def edit_status():
    data = request.get_json()
    print(data)
    print(data['status'])
    update_status(data['todo'], data['status'])
    print(get_todolist())  


    return '', 204

if __name__=='__main__':
    app.run(debug=True)