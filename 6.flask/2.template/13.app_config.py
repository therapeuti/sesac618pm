from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_FILE_EXT'] = {'png','jpg','jpeg','gif','png'}
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 용량이 크면 자동으로 예외 발생시킴


os.makedirs(app.config['UPLOAD_FOLDER'],  exist_ok=True)

def allowed_file(filename):
    if '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()

    if ext in app.config['ALLOWED_FILE_EXT']:
        return True
    else:
        return False

def allowed_file_pythonic(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in app.config['ALLOWED_FILE_EXT']


@app.route('/')
def index():
    #루트페이지에 파일목록 출력
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    print(file_list)

    del_file = request.args.get('filename')
    print(del_file)
    if del_file:
        os.remove(f'{app.config['UPLOAD_FOLDER']}/{del_file}')
        file_list = os.listdir(app.config['UPLOAD_FOLDER'])
        
    return render_template('upload2.html', file_list=file_list)

@app.route('/upload', methods=['POST'], )
def upload_file():
    # request.form 의 경우 파일명만 받아옴
    print(request.files) # 실제로 파일내용까지 FileStorage라는 객체 형태로 파일을 받아옴
    file = request.files['file']
    
    if file.filename == '':
        return '파일이 올바르게 전송되지 않았습니다.'

    
    if allowed_file_pythonic(file.filename):
        # 파일 저장하기 (현재 폴더 내 uploads 폴더 안에 filename으로 저장)
        filepath = os.path.join('./', app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('index'))
    else:
        return '허용되지 않는 파일'

# 1. 파일 목록 보여준다 메인 라우트에서 uploads 폴더 내의 파일명 보여주기
# 2. 각 파일명 옆에 삭제 버튼 추가
# 3. 실제 파일 삭제
# 4. 파일 욜량이 1MB보다 크면 허용하지 않는다.



@app.errorhandler(413)
def too_large(e):
    size_mb = app.config['MAx_CONTENT_LENGTH'] /(1024*1024)
    return f'업로드한 파일이 너무 큽니다. 최대 {size_mb}MB까지만 허용됩니다.'



if __name__=='__main__':
    app.run(debug=True)