from flask import Blueprint, request, jsonify
from chatbot_service import chat_gpt, do_action
from database import save_conversation


chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/', methods=['POST'])
def chatbot():
    userinput = request.get_json()
    print('사용자가 입력한 내용: ', userinput)
    save_conversation('user', userinput['userInput'])


    response = chat_gpt(userinput)
    save_conversation('assistant', response)

    reply = do_action(response)
    save_conversation('chatbot', reply)

    return jsonify(reply)

