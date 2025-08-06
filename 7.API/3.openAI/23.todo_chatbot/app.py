from flask import Flask, request, jsonify

app = Flask(__name__, static_folder='public', static_url_path='')

# 내 메모 리스트 담을 곳
todos = []

@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route('/api/todo', methods=['GET'])
def get_todos():
    return jsonify({'error':'구현 중'})


@app.route('/api/todo', methods=['POST'])
def add_todo():
    return jsonify({'error':'구현 중'})


@app.route('/api/todo/<int:todoID>', methods=['PUT'])
def toggle_todos(todoID):
    return jsonify({'error':'구현 중'})


@app.route('/api/todo/<int:todoID>', methods=['DELETE'])
def delete_todos(todoID):
    return jsonify({'error':'구현 중'})


#미션1. 투두의 CRUD 완성
#미션2. 챗봇을 프론트에 추가. 요청 라우트 분리..?
#미션2-1. 
#미션3. 채팅 아무말 받아서 gpt에게 주고 응답 받아서 채팅창에 출력
#미션. 챗봇과 투두 crud 연동
#미션. 히스토리 기능 추가해서




if __name__ =='__main__':
    app.run(debug=True)