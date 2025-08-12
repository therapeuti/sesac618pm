from flask import Flask, jsonify, request
import os
from vectorstore import initialize_vector_db, create_vector_db, answer_question, delete_file_from_vsstore
from chatbot import initialize_llm


app = Flask(__name__, static_url_path="")

DATA_DIR = './DATA'

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': '파일이 없습니다.'}), 400
    
    file = request.files['file']
    print(file.filename)
    if file:
        file_path = os.path.join(DATA_DIR, file.filename)
        file.save(file_path)

        result = create_vector_db(file_path)
        if result:
            return jsonify({'message':'파일이 성공적으로 업로드 되었습니다.'})
        else:
            return jsonify({'message':'파일은 업로드 되었으나, 벡터DB 생성 오류 발생'})



@app.route('/ask', methods=['POST'])
def chatbot():
    data = request.get_json()
    print(data)
    question = data.get('question', '')
    print(question)

    response = answer_question(question)

    return jsonify({'message': f'질문을 받았습니다. {response}'})

@app.route('/files')
def get_files():
    file_list = os.listdir(DATA_DIR)
    print(file_list)

    files = [f for f in os.listdir(DATA_DIR) if os.path.isfile(os.path.join(DATA_DIR, f))]
    return jsonify({'file_list': file_list})


@app.route('/delete_file/<filename>', methods=['DELETE'])
def delete_file(filename):
    # 벡터db에서도 삭제해야함.
    delete_file_from_vsstore(filename)

    print(filename)
    filepath = os.path.join(DATA_DIR, filename)
    print(filepath)
    if os.path.exists:
        os.remove(filepath)
        return jsonify({'message':'파일이 삭제되었습니다.'})
    else:
        print('파일이 존재하지 않음.')
        return jsonify({'message':'해당 파일이 존재하지 않습니다.'})



if __name__=='__main__':
    initialize_vector_db()
    initialize_llm()
    app.run(debug=True)