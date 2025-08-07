from flask import Blueprint, request, jsonify
from chatbot_service import chat_gpt, add, toggle, delete
import json


chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/', methods=['POST'])
def chatbot():
    userinput = request.get_json()
    print('사용자가 입력한 내용: ', userinput)

    response = chat_gpt(userinput)

    my_action = json.loads(response)
    action = my_action['action']

    if action == 'add':
        item = my_action['item']
        todo = add(item)

        reply = f'{todo}를 추가했습니다.'

    elif action == 'update':
        item = my_action['item']
        print('투두리스트 업데이트 해야함')

        todo = toggle(item)
        print('업데이트 된 투두리스트', todo)

        if todo['status'] == 'complete':
            reply = f'{todo['todo']}가 완료되었습니다.'
        else:
            reply = f'{todo['todo']}는 완료되지 않았습니다.'            

    elif action =='delete':
        item = my_action['item']
        print('투두리스트 삭제해야함')

        todos =  delete(item)
        print('삭제된 후의 투두리스트 : ', todos)
        reply = f'투두리스트가 삭제되었습니다.'

    elif action == 'list':
        todos = get_all()
        print(todos)

        if len(todos) == 0:
            reply = '현재 할 일 목록이 없습니다.'
        else:
            todolist = [f'{todo['id']}. {todo['todo']} [미완료]' for todo in todos if todo['status'] == 'incomplete']
            reply = '<br>'.join(todolist)
            print(reply)

    else:
        reply = '무슨 말인지 이해를 못 하겠어요 다시 말씀해주세요.'

    return jsonify(reply)

