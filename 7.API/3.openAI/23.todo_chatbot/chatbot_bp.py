from flask import Blueprint, request, jsonify
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

chatbot_bp = Blueprint('chatbot', __name__)


prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 투두리스트 관리는 돕는 인공지능 챗봇 "아길레온"입니다.'),
    ('human', "{user_input}" )
])

llm = ChatOpenAI(model='gpt-4o')

chain = prompt | llm


@chatbot_bp.route('/', methods=['POST'])
def chatbot():
    userinput = request.get_json()
    print('사용자가 입력한 내용: ', userinput)

    user_input = {'user_input': userinput}

    print('실제 입력될 프롬프트 내용: ', prompt.invoke(user_input))
    
    response = chain.invoke(user_input)

    print(response)
    print(response.content)
    return jsonify(response.content)

