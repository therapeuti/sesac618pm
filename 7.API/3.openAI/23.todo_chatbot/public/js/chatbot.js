// 미션1. /api/todo에 crud 추가
// GET /api/todo
// POST /api/todo
// PUT /api/todo/${id}
// DELETE /api/todo/${id}



const todoinput = document.getElementById('todo-input')
const submit = document.getElementById('submit')

// 투두리스트 추가
submit.addEventListener('click', (e) => {
    e.preventDefault();
    const response = fetch('/api/todo', {
        method: 'post',
        headers: {'content-type':'application/json'},
        body: todoinput.value
    })
})