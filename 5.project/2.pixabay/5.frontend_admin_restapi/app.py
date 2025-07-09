from flask import Flask, jsonify, url_for, request, send_from_directory
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

images = [
    {'filename':"cat.jpg", 'tag':['cat','cute','pet']},
    {'filename':"cat2.jpg", 'tag':['cat','cute','pet']},
    {'filename':"2019-07-24.png", 'tag':['png']}
]

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
            filepath = url_for('static',filename=f'img/{img['filename']}')
            img['url'] = filepath
            print(img)
            data.append(img)
        else:
            print('tag 없음')
    return jsonify({'imgs':data})




if __name__=='__main__':
    app.run(debug=True)