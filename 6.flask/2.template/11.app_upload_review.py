from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)
app.config['accepted_ext'] = {'png','jpg','jpeg','gif'}
app.config['Upload_folder'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 자동으로 업로드 파일 용량 제한됨

os.makedirs(app.config['Upload_folder'], exist_ok=True,) # 시작할 때 폴더 없으면 만들기

@app.route('/')
def home():
    file_list = os.listdir(app.config['Upload_folder'])
    return render_template('upload3.html', file_list=file_list)


@app.route('/upload', methods=['POST'])
def upload(): # 용량 제한, 확장자 제한
    file = request.files['file']
    print(file.filename)
    # 확장자 확인
    ext = file.filename.rsplit('.')[-1].lower()
    if ext in app.config['accepted_ext']:
        # 폴더명, 파일명으로 알아서 경로 만들어 주는 함수. './'는 현재 디렉터리를 의미
        filepath = os.path.join('./', app.config['Upload_folder'], file.filename) 
        print(filepath)
        file.save(filepath)
    else:
        return '이미지 파일만 업로드 가능'
    return redirect(url_for('home'))

@app.route('/delete/<filename>')
def delete(filename):
    del_file = os.path.join('./', app.config['Upload_folder'], filename)
    os.remove(del_file)
    return redirect(url_for('home'))


@app.errorhandler(413)
def error_handler(error):
    return '파일크기가 1MB를 초과했습니다.', 413


if __name__=='__main__':
    app.run(debug=True)