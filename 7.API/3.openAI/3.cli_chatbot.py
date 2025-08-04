import openai
from dotenv import load_dotenv
import os
load_dotenv()

client = openai.OpenAI()

history = []

def ask_chatgpt(user_input):
    gpt_question = {'role': 'user', 'content': user_input}
    history.append(gpt_question)
    print('gpt에게 던지는 메시지 : ', history)
    print('-------------------------------------------')
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages = history
    )
    gpt_response = {'role':'assistant', 'content':response.choices[0].message.content}
    history.append(gpt_response)
    return gpt_response

# print('[챗봇응답]', ask_chatgpt('gpt가 뭐야'))


while True:
    user_input = input('[사용자]: ')
    if user_input == 'quit':
        print('대화 종료')
        break

    print('[챗봇응답]: ', ask_chatgpt(user_input))