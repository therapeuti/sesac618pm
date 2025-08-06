// 미션1. /api/todo에 crud 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}

get_todolist()

const todoinput = document.getElementById('todo-input')
const submit = document.getElementById('submit')

// 투두리스트 추가
submit.addEventListener('click', async (e) => {
    e.preventDefault();
    await fetch('/api/todo/', {
        method: 'post',
        headers: {'content-type':'application/json'},
        body: JSON.stringify(todoinput.value)
    })
    await get_todolist()
    todoinput.value = ''
})

document.addEventListener('click', (e) => {
    if ((e.target.tagName === 'LI') && (!e.target.classList.contains('del'))) {
        // 서버로 보내서 정보 수정하고 받아와서 적용
        console.log('클릭: ', e.target)
        updateStatus(e.target.dataset.id);
        get_todolist()
    }

    if (e.target.classList.contains('del')) {
        deleteTodo(e.target.dataset.id)  
        get_todolist()      
    }
})


async function get_todolist() {
    const response = await fetch('/api/todo/')
    const data = await response.json()
    console.log(data.todolist)

    addTodolist(data.todolist)
}

function addTodolist(todolist) {
    const todoList = document.getElementById('todo-list')
    todoList.innerHTML = ''
    for (todo of todolist){
        const li = document.createElement('li')
        li.innerText = todo.todo;
        li.classList.add(todo.status)
        li.dataset.id = todo.id

        const delBtn = document.createElement('button')
        delBtn.classList.add('del')
        delBtn.innerText = 'X'
        delBtn.dataset.id = todo.id
        li.appendChild(delBtn)
        
        todoList.appendChild(li)
    }
}


async function updateStatus(todoid) {
    console.log(todoid)
    const response = await fetch(`/api/todo/${todoid}`,{
        method: 'put',
        headers: {'content-type':'application/json'},
        body: JSON.stringify(todoid)
    })

}

async function deleteTodo(todoid) {
    console.log(todoid)
    await fetch(`/api/todo/${todoid}`, {
        method: 'delete',
        headers: {'content-type':'application/json'},
    })
}