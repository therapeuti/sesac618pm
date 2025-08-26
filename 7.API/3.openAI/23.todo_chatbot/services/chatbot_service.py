from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import LLMChain
from database import database as db
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    raise RuntimeError('API키가 없습니다!')

# 랭체인말고 걍 openai 라이브러리 사용하는 경우에 deque 사용
# from collections import deque
# HISTORY = deque(maxlen=10)
# def save_history(role, content):
#     HISTORY.append({'role': role, 'content': content})


memory = ConversationBufferWindowMemory(
    k=10,
    return_messages=True,
    memory_key='chat_history',
    input_key='user_input'
)


def get_system_prompt():
    prompt = ChatPromptTemplate.from_messages([
    ('system', '''당신은 투두리스트 관리는 돕는 인공지능 챗봇 "아길레온"입니다. 
                  아래의 [투두리스트]를 참고하여 [출력형식]에 맞춰 간결하게 답변하세요.
                [투두리스트]
                {todos}

                [출력 형식]
                {{ "action": "add", "item": [항목] }} - 할 일을 추가해야 할 때
                {{ "action": "delete", "item": [항목ID] }} - 할 일을 안 하겠다고 하거나, 잘못 추가했을 때, "삭제"해야할 때
                {{ "action": "update", "item": [항목ID] }} - 할 일을 "완료"했거나, 완료를 취소해야 할 때
                {{ "action": "list" }} - 할 일을 보여줘야 할 때
                {{ "action": "nothing" }} - 어떻게 판단해야할지 모를때 또는 TODO 리스트와는 쓸대없는 질문이 들어왔을때
                    '''), # 시스템 프롬프트
        MessagesPlaceholder(variable_name="chat_history"), # 이전 대화 내용
    ('human', "{user_input}" ) # 새로운 대화 내용
    ])

    return prompt


def chat_gpt(userinput):
    user_input = userinput['userInput']
    my_todo_list = db.get_todolist()
    
    # llm = ChatOpenAI(model='gpt-4o', max_tokens=256)
    llm = ChatOpenAI(model='gpt-5')

    prompt = get_system_prompt()

    # chain = prompt | llm    # 메모리 지원이 안 됨. 대화 히스토리 수동으로 처리해야함.
    chain = LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)

    input_prompt = {'todos': my_todo_list, 'user_input': user_input}

    # response = chain.invoke(input_prompt) # LCEL 표준
    response = chain.predict(**input_prompt) # 메모리에 자동 저장

    print('llm의 응답 : ', response)
    
    return response


def do_action(response):
    my_action = json.loads(response)
    action = my_action['action']

    if action == 'add':
        item = my_action['item']
        db.insert_todo(item, 'incomplete')
        
        reply = f'{item}를 추가했습니다.'

    elif action == 'update':
        item = my_action['item']
        print('투두리스트 업데이트 해야함')
        status = db.get_status(item)

        if status == 'complete':
            todo = db.update_todo(item, 'incomplete')
            print('업데이트 된 투두리스트', todo)
            reply = f'{todo['todo']}가 완료되지 않았습니다.'
        else:
            todo = db.update_todo(item, 'complete')
            print('업데이트 된 투두리스트', todo)
            reply = f'{todo['todo']}는 완료되었습니다.'            

    elif action =='delete':
        item = my_action['item']
        print('투두리스트 삭제해야함')

        todos =  db.delete_todo(item)
        print('삭제된 후의 투두리스트 : ', todos)
        reply = f'투두리스트가 삭제되었습니다.'

    elif action == 'list':
        todos = get_all()
        print(todos)

        if len(todos) == 0:
            reply = '현재 할 일 목록이 없습니다.'
        else:
            todolist = [f'{todo['id']}. {todo['todo']} [미완료]' for todo in todos if todo['status'] == 'incomplete']
            reply = '\n'.join(todolist)
            print('줄바꿈 : ', reply)

    else:
        reply = '무슨 말인지 이해를 못 하겠어요 다시 말씀해주세요.'

    return reply


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

if __name__ == "__main__":
    print("투두 챗봇 아길레온이 시작되었습니다!")
    print("대화를 시작하세요. ('quit'을 입력하면 종료됩니다.)")
    
    while True:
        user_input = input("\n사용자: ")
        
        if user_input.lower() == 'quit':
            break
        
        response = chat_gpt(user_input)
        print(f"아길레온: {response}")
    
    print("대화가 종료되었습니다.")