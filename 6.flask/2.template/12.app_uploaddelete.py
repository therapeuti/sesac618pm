from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = {'png','jpg','jpeg','gif','png'} # 중복없음. 유니크한 리스트...? 리스트와 기능은 동일하지만 좀 더 파이썬스러운 자료구조

os.makedirs(UPLOAD_FOLDER,  exist_ok=True)

def allowed_file(filename):
    if '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()

    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXT

def get_file_size(file):
    pos = file.stream.tell() # 이전 작업 고려하여 현재 fd의 위치 저장
    file.stream.seek(0, os.SEEK_END) # 파일 끝으로 가라
    size = file.stream.tell() # 위치 기반 크리를 알려줘라
    file.stream.seek(pos) # 원래 위치로 가라
    return size

max_size = 1 * 1024 * 1024

@app.route('/')
def index():
    #루트페이지에 파일목록 출력
    file_list = os.listdir(UPLOAD_FOLDER)
    print(file_list)

    del_file = request.args.get('filename')
    print(del_file)
    if del_file:
        os.remove(f'{UPLOAD_FOLDER}/{del_file}')
        file_list = os.listdir(UPLOAD_FOLDER)
        
    return render_template('upload2.html', file_list=file_list)

@app.route('/upload', methods=['POST'], )
def upload_file():
    # request.form 의 경우 파일명만 받아옴
    print(request.files) # 실제로 파일내용까지 FileStorage라는 객체 형태로 파일을 받아옴
    file = request.files['file']
    
    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    file_size = get_file_size(file)
    if file_size > max_size:
        return '파일 용량이 1MB를 초과합니다.'
        # 비즈니스 로직 : 내가 정한 프로세싱 룰들을 여기에 하나 둘 씩 구현
        # 1. 사진 파일만 업로드
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 (현재 폴더 내 uploads 폴더 안에 filename으로 저장)
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return redirect(url_for('index'))
    else:
        return '허용되지 않는 파일'

# 1. 파일 목록 보여준다 메인 라우트에서 uploads 폴더 내의 파일명 보여주기
# 2. 각 파일명 옆에 삭제 버튼 추가
# 3. 실제 파일 삭제
# 4. 파일 욜량이 1MB보다 크면 허용하지 않는다.

if __name__=='__main__':
    app.run(debug=True)