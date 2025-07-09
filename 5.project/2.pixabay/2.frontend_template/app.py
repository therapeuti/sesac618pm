from flask import Flask, jsonify, url_for, render_template, request

app = Flask(__name__)

images = [
    {'filename':"cat.jpg", 'tag':['cat','cute','pet']},
    {'filename':"cat2.jpg", 'tag':['cat','cute','pet']}
]

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




if __name__=='__main__':
    app.run(debug=True)