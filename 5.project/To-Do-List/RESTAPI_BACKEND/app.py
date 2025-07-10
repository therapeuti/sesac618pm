from flask import Flask, jsonify, send_file, request, redirect, url_for

app = Flask(__name__)

todolist = [{'todo': '1번', 'status': 'not_complete'}, 
            {'todo': '2번', 'status': 'not_complete'}, 
            {'todo': '3번', 'status': 'complete'}]

@app.route('/')
def index():
    return send_file('todolist.html')

@app.route('/send_data')
def send_data():
    return jsonify({'data':todolist})

@app.route('/add', methods=['POST'])
def add_todolist():
    global todolist
    print('메소드 받았니?')
    print(request)
    print(request.data)
    data = request.get_json()
    print(data)
    todolist.append(data)
    print(todolist)
    return '', 204 # 204 no content 클라이언트에게 반환할 데이터 없음


@app.route('/delete', methods=['DELETE'])
def delete_todolist():
    global todolist
    print(request)
    print(request.data)
    data = request.get_json()
    print(data)
    for i in range(len(todolist)):
        if todolist[i]['todo'] == data['todo']:
            del todolist[i]
            break
    print(todolist)
    return '', 204

@app.route('/edit_status', methods=['PUT'])
def edit_status():
    data = request.get_json()
    print(data)
    for i in todolist:
        if i['todo'] == data['todo']:
            i['status'] = data['status']
            break
    print(todolist)
    return '', 204

if __name__=='__main__':
    app.run(debug=True)