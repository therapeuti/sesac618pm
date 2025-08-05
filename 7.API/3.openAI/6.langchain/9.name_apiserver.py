from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

load_dotenv()

app = Flask(__name__)

llm1 = OpenAI(temperature=0.9)
llm2 = ChatOpenAI(temperature=0.9)


@app.route('/api/name', methods=['POST'])
def generate_name():
    data = request.get_json()
    product = data.get('product', None)

    # 한글 회사 명으로 한 개만 출력되게
    prompt = f'{product}를 만드는 회사 이름을 한글로 지어서 한 개만 알려줘.'
    result = llm1.invoke(prompt)
    names = result.strip()

    return jsonify({'product': product, 'name': names})


@app.route('/api/name2', methods=['POST'])
def generate_name2():
    data = request.get_json()
    product = data.get('product', None)

    # 한글 회사 명으로 한 개만 출력되게
    prompt = [
        SystemMessage(content='창의적인 회사 이름을 지어주는 작명가 입니다. 사용자가 제시한 제품를 만드는 회사 이름을 한글로 지어서 한 개만 알려주세요.'), 
        HumanMessage(content=f'{product}')]
    
    result2 = llm2.invoke(prompt)
    names = result2.content.strip('"')

    return jsonify({'product': product, 'name': names})



if __name__=='__main__':
    app.run(debug=True)