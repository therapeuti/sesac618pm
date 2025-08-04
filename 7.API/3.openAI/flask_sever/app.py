from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI()

def ask_chatgpt(history):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages = history
    )
    return response.choices[0].message.content


history = []
@app.route('/')
def index():

    return render_template('index.html')
    
@app.route('/api/chat_gpt/', methods=['POST'])
def chat_gpt():
    user_input = request.get_json('user')
    gpt_question = {'role': 'user', 'content': user_input}
    history.append(gpt_question)
    print('gpt에게 던지는 메시지 : ', history)

    response = ask_chatgpt(history)
    print('gpt가 보낸 메시지 : ', response)
    gpt_response = {'role':'assistant', 'content': response}
    history.append(gpt_response)
    return jsonify(gpt_response)



if __name__=='__main__':
    app.run(debug=True)