from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_FILE_EXT = {'png','jpg','jpeg','gif','png'} # 중복없음. 유니크한 리스트...? 리스트와 기능은 동일하지만 좀 더 파이썬스러운 자료구조

os.makedirs(UPLOAD_FOLDER,  exist_ok=True)

def allowed_file(filename):
    if '.' not in filename:
        return False

    print('filename: ', filename)
    
    ext = filename.rsplit('.', 1)[1].lower()

    if ext in ALLOWED_FILE_EXT:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_FILE_EXT


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'], )
def upload_file():
    # request.form 의 경우 파일명만 받아옴
    print(request.files) # 실제로 파일내용까지 FileStorage라는 객체 형태로 파일을 받아옴
    file = request.files['file']
    
    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

        # 비즈니스 로직 : 내가 정한 프로세싱 룰들을 여기에 하나 둘 씩 구현
        # 1. 사진 파일만 업로드
    # if allowed_file(file.filename):
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 (현재 폴더 내 uploads 폴더 안에 filename으로 저장)
        filepath = os.path.join('./', UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return '파일업로드에 성공'
    else:
        return '허용되지 않는 파일'

# upload된 파일 목록 출력하기

if __name__=='__main__':
    app.run(debug=True)