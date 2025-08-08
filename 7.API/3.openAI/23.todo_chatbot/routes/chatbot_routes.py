from flask import Blueprint, request, jsonify
from services.chatbot_service import chat_gpt, do_action


chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/', methods=['POST'])
def chatbot():
    userinput = request.get_json()
    print('사용자가 입력한 내용: ', userinput)

    response = chat_gpt(userinput)

    reply = do_action(response)

    return jsonify(reply)

