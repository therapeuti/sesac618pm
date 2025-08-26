async function uploadFile() {
    console.log("업로드 실행")
    const fileInput = document.getElementById('fileinput');
    const file = fileInput.files[0]
    console.log('file')
    const formData = new FormData();
    formData.append('file', file)

    const response = await fetch('/upload', {
        method: 'post',
        body: formData
    })
    const result = await response.json();
    alert(result.message)
    get_files()
}


async function askQuestion() {
    const questionInput = document.getElementById('questioninput');
    const question = questionInput.value;
    const response = await fetch('/ask', {
        method: 'post',
        body : JSON.stringify({'question':question}),
        headers: {'content-type':'application/json'}
    })
    const data = await response.json()
    const result = document.getElementById('answer');
    result.innerHTML = data.message;
}

async function get_files() {
    const uploadedFiles = document.getElementById('uploadedFiles')

    const response = await fetch('/files')
    const data = await response.json()
    console.log(data)
    uploadedFiles.innerHTML = ''
    for (let file of data.file_list) {
        const li = document.createElement('li')
        const del_btn = document.createElement('button')
        del_btn.classList.add('delete')
        del_btn.innerText = '삭제'
        del_btn.dataset.id = file
        console.log(file)
        li.innerText = file
        li.appendChild(del_btn)
        uploadedFiles.appendChild(li)
    }
}


document.addEventListener('click', async (e) => {
    if (e.target.classList.contains('delete')) {
        console.log('삭제 버튼 누름')
        console.log(e.target.dataset.id)

        // if (!confirm(`"${e.target.dataset.id}"를 정말 삭제하시겠습니까?`)) return; 버블링때문에 일단 삭제

        const response = await fetch(`/delete_file/${e.target.dataset.id}`, {
            method: 'DELETE'
        })
        const data = await response.json()
        console.log(data.message)
        get_files()

    }
}
)

async function delete_file() {


}


get_files()