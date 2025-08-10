from flask import Blueprint, request, jsonify, session
from database import database as TODO

todo_bp = Blueprint('todo', __name__)


# 라우트의 목적인 입력과 출력 프로세싱이 목적이고 그 중간의 비즈니스 로직은 다른 부분에서 담당하도록 하는게 좋음
# 코드 리팩토링 할 것!

@todo_bp.route('/api/todo/', methods=['GET'])
def get_todos():

    todos = TODO.get_todolist()
    return jsonify({'todolist': todos})


@todo_bp.route('/api/todo/', methods=['POST'])
def add_():
    new_todo = request.get_json()
    print(new_todo)

    TODO.insert_todo(new_todo, 'incomplete')
    return jsonify({'message': '투두리스트에 저장됨'})


@todo_bp.route('/api/todo/<int:todoID>', methods=['PUT'])
def toggle_(todoID):
    status = TODO.get_status(todoID)
    print(status)
    if status['status'] == 'complete':
        todos = TODO.update_todo(todoID, 'imcomplete')
    else:
        todos = TODO.update_todo(todoID, 'complete')
    print('상태 수정됨: ', todos)
    return jsonify({'message':'ToDo 완료 여부 수정'})


@todo_bp.route('/api/todo/<int:todoID>', methods=['DELETE'])
def delete_(todoID):

    todos = TODO.delete_todo(todoID)    
    print('삭제됨: ', todos)
    return jsonify({'meassage':'ToDo 삭제'})


