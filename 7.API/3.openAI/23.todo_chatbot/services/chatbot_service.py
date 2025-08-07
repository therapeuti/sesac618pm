from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from services.todo_service import get_all
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    raise RuntimeError('API키가 없습니다!')


def chat_gpt(userinput):
    my_todo_list = get_all()

    prompt = ChatPromptTemplate.from_messages([
    ('system', '''당신은 투두리스트 관리는 돕는 인공지능 챗봇 "아길레온"입니다. 
                  아래의 [투두리스트]를 참고하여 [출력형식]에 맞춰 간결하게 답변하세요.
     [투두리스트]
     {todos}

     [출력 형식]
    {{ "action": "add", "item": [항목] }} - 할 일을 추가해야 할 때
    {{ "action": "delete", "item": [항목ID] }} - 할 일을 안 하겠다고 하거나, 잘못 추가했을 때
    {{ "action": "update", "item": [항목ID] }} - 할 일을 완료했거나, 완료를 취소해야 할 때
    {{ "action": "list" }} - 할 일을 보여줘야 할 때
    {{ "action": "nothing" }} - 어떻게 판단해야할지 모를때 또는 TODO 리스트와는 쓸대없는 질문이 들어왔을때
        '''),
        ('human', "{user_input}" )
    ])

    llm = ChatOpenAI(model='gpt-4o', max_tokens=256)
    chain = prompt | llm

    input_prompt = {'todos': my_todo_list, 'user_input': userinput}
    response = chain.invoke(input_prompt)

    print(response.content)
    
    return response.content


def add(item):
    todos = get_all()

    new_id = len(todos) + 1
    new_todo = {'id': new_id, 'todo': item, 'status': 'incomplete'}
    todos.append(new_todo)
    return new_todo['todo']


def toggle(item):
    todos = get_all()

    for todo in todos:
        if todo['id'] == item and todo['status'] == 'incomplete':
            todo['status'] = 'complete'
            return todo
        elif todo['id'] == item and todo['status'] == 'complete':
            todo['status'] = 'incomplete'
            return todo
        

def delete(item):
    todos = get_all()

    for todo in todos:
        if todo['id'] == item:
            todos.remove(todo)
    return todos




# client = ChatOpenAI(api_key=API_KEY)

# def ask_gpt(question):
#     my_todo_list = get_all()

#     system_prompt = f'''
#     당신은 투두리스트를 관리하고 투두리스트에 대한 질문에 답변을 하는 챗봇입니다. 사용자의 질문에 간결하게 답하세요.
#     {my_todo_list}
#     '''

#     response = client.chat.completions.create(
#         model='gpt-3.5-turbo',
#         messages=[
#             {'role':'system', 'content':  system_prompt},
#             {'role':'user', 'content': question}
#         ]
#     )