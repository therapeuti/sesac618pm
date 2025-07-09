from flask import Flask, url_for, redirect, render_template, request
import os
from collections import defaultdict

app = Flask(__name__)
app.config['image_folder'] = 'static/img'

# 이미지 리스트 가져오기
images = []
img_list = os.listdir(app.config['image_folder'])
print(img_list)
for i in img_list:
    print(i)
    img = {}
    img['filename'] = i
    img['url'] = os.path.join('static/img', i)
    print(img)
    images.append(img)
print(images)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search')
def search():
    query = request.args.get('q','').lower()
    results = []
    found = False
    for i in images:
        if query in i['tag']:
            found = True
        if found:
            image_url = url_for('static',filename=f'/img/{i['filename']}')
            results.append(image_url)

    # return jsonify({'url':image_url}) 순수 백엔드 개발자는 여기까지하면 ok
    return render_template('result.html', query=query, results=results)

@app.route('/admin') # 이미지 업로드 및 관리
def admin():
    return render_template('admin.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_img():
    img = request.files['img']
    print(img)
    filepath = os.path.join(app.config['image_folder'], img.filename)
    img.save(filepath)
    return redirect(url_for('admin'))



@app.route('/delete/<filename>')
def delete_img(filename):
    del_file = os.path.join(app.config['image_folder'], filename)
    os.remove(del_file)
    return redirect(url_for('admin'))


if __name__=='__main__':
    app.run(debug=True)