# 아래 변수들은 내부 변수이니까, 남들이 가져다 쓰지 말라는 의미로 앞에 언더바(_)추가....
_todos = []
_next_id = 1


def get_all():
    
    return _todos


def add_todo(item):
    global _next_id
    _next_id += 1
    new_todo = {'id': _next_id, 'todo': item, 'status': 'incomplete'}
    _todos.append(new_todo)
    return new_todo


def toggle_todo(id_):
    for todo in _todos:
        if todo['id'] == id_ and todo['status'] == 'incomplete':
            todo['status'] = 'complete'
            return todo
        
        elif todo['id'] == id_ and todo['status'] == 'complete':
            todo['status'] = 'incomplete'
            return todo
        

def delete_todo(id_):
    for todo in _todos:
        if todo['id'] == id_:
            _todos.remove(todo)
    
    return _todos



