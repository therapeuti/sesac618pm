from flask import Flask, jsonify, url_for, request, send_from_directory
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)

app.config['image_folder'] = 'static/img'


# 이미지 리스트 가져오기
def image_list_from_db(filepath):
    images = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                images.append(row)
        return images
    except FileNotFoundError as e:
        return None

def image_list():
    images = image_list_from_db('image_db')
    if images:
        return images
    else:
        images = []
        img_list = os.listdir(app.config['image_folder'])
        for i in img_list:
            print(i)
            img = {}
            img['filename'] = i
            img['url'] = os.path.join(app.config['image_folder'], i)
            img['tag'] = ''
            images.append(img)
        print(images)
        update_image_db(images)
        return images

def update_image_db(images):
    with open('image_db', 'w', encoding='utf-8', newline='') as file:
        fieldname = images[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldname)
        csv_writer.writeheader()
        for i in images:
            csv_writer.writerow(i)

    
images = image_list()
print(images)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/search')
def search():
    print('요청들어옴')
    print(request.args.get('q'))
    query = request.args.get('q')
    data = []
    for img in images:
        if query in img['tag']:
            print('tag 있음')
            filepath = url_for('static',filename=f'img/{img["filename"]}')
            img['url'] = filepath
            print(img)
            data.append(img)
        else:
            print('tag 없음')
    return jsonify({'imgs':data})

@app.route('/admin')
def admin():
    return send_from_directory(app.static_folder, 'admin.html')

@app.route('/api/send_images')
def send_images():
    print('프론트에서 요청이 들어왔나?')
    images = image_list()
    print(images)
    return jsonify({'data':images})

@app.route('/api/upload', methods=['POST'])
def upload_images():
    img = request.files['img']
    print(img.filename)
    # 파일 받았으니까 저장하고, images에 리스트화
    filepath = os.path.join(app.config['image_folder'], img.filename)
    img.save(filepath)
    images.append({'filename':img.filename, 'url':filepath, 'tag':''})
    update_image_db(images)
    return jsonify({'data':images})

@app.route('/api/delete/<filename>')
def delete_images(filename):
    print(f'{filename}삭제 ㄱㄱ')
    for i in range(len(images)):
        if images[i]['filename'] == filename:
            del images[i]
            break
    print(images)
    update_image_db(images)
    return jsonify({'data':images})

@app.route('/api/edit_tag/<filename>', methods=['POST'])
def edit_tag(filename):
    tag = request.form['tag']
    print('태그 수정 요청 들어옴', tag, filename)
    for img in images:
        if img['filename'] == filename:
            img['tag'] = tag
            break
    update_image_db(images)
    return jsonify({'data':images})



if __name__=='__main__':
    app.run(debug=True)