from flask import Flask, request, jsonify
from chatbot_bp import chatbot_bp


app = Flask(__name__, static_folder='public', static_url_path='')
app.register_blueprint(chatbot_bp, url_prefix='/api/chat')

# 내 메모 리스트 담을 곳
todos = []

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/api/todo/', methods=['GET'])
def get_todos():
    print(todos)
    return jsonify({'todolist': todos})


@app.route('/api/todo/', methods=['POST'])
def add_todo():
    new_todo = request.get_json()
    print(new_todo)

    todo_id = len(todos) + 1
    todos.append({'id': todo_id, 'todo':new_todo, 'status': 'incomplete'})

    return jsonify({'message': '투두리스트에 저장됨'})


@app.route('/api/todo/<int:todoID>', methods=['PUT'])
def toggle_todos(todoID):
    print(todoID)
    for todo in todos:
        if todo['id'] == todoID:
            if todo['status'] == 'complete':
                todo['status'] = 'incomplete'
                break
            else: 
                todo['status'] = 'complete'
                break
    print(todos)
    return jsonify({'message':'ToDo 완료 여부 수정'})


@app.route('/api/todo/<int:todoID>', methods=['DELETE'])
def delete_todos(todoID):
    
    print(todoID)
    for todo in todos:
        if todo['id'] == todoID:
            todos.remove(todo)
            break
    print(todos)
    return jsonify({'meassage':'ToDo 삭제'})


#미션2-1. 
#미션3. 채팅 아무말 받아서 gpt에게 주고 응답 받아서 채팅창에 출력
#미션. 챗봇과 투두 crud 연동
#미션. 히스토리 기능 추가해서




if __name__ =='__main__':
    app.run(debug=True)