from flask import Flask, url_for, redirect, render_template, request
import os
import csv

app = Flask(__name__)
app.config['image_folder'] = 'static/img'


# 이미지 리스트 가져오기
def image_list_from_db(filepath):
    images = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            print(csv_reader)
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
            image_url = url_for('static', filename=f'/img/{i["filename"]}')
            results.append(image_url)
    return render_template('result.html', query=query, results=results)

@app.route('/admin') # 이미지 업로드 및 관리
def admin():
    # db를 불러와서 전송
    return render_template('admin.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_img():
    img = request.files['img']
    print(img)
    filepath = os.path.join(app.config['image_folder'], img.filename)
    img.save(filepath)
    # 이미지 업로드는 되지만, 페이지에 바로 뜨지 않음. images에 반영하여 db 업데이트 해야함.
    images.append({'filename':img.filename, 'url':filepath, 'tag':''})
    update_image_db(images)
    return redirect(url_for('admin'))

@app.route('/delete/<filename>')
def delete_img(filename):
    del_file = os.path.join(app.config['image_folder'], filename)
    os.remove(del_file)
    # 사진은 삭제됨. 그러나 다른 정보들은 남아있음. 파일명이랑 키워드가 남아있음. 아예 전부 싹다 사라지게 만들어야 함. db 업데이트
    for i in range(len(images)):
        if images[i]['filename'] == filename:
            del images[i]
    update_image_db(images)
    return redirect(url_for('admin'))

@app.route('/edit_tag/<filename>', methods=['POST'])
def edit_tag(filename):
    print(request.form)
    tag = request.form['tag'].split(',')
    # ,로 split해서 각각 서로 다른 단어로 구분.
    print(tag)
    keywords = [word.strip() for word in tag ]
    print(keywords)
    for img in  images:
        if img['filename'] == filename:
            img['tag'] = tag
            break
    print(images)
    update_image_db(images)
    return redirect(url_for('admin'))


if __name__=='__main__':
    app.run(debug=True)