from flask import Flask, request, jsonify, send_from_directory
import openai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat/', methods=['POST'])
def chat():
    userinput = request.get_json()
    print(userinput)
    response = ask_chatgpt(userinput)

    return jsonify({'response': response})

history = []
def ask_chatgpt(user_input):
    history.append({'role':'user', 'content':user_input})

    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        message = [
            {'role': 'user', 'content': user_input}
        ]
    )
    chatgpt_response = response.choices[0].message.content
    history.append({'role':'assistant', 'content':chatgpt_response})

    if len(history) > 10:
        history.pop(0)
    print(history)
    print('대화내용 길이: ', len(history))
    return chatgpt_response

if __name__=='__main__':
    app.run(debug=True)