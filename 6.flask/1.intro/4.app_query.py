from flask import Flask, request

app = Flask(__name__)

@app.route('/search') # /search?q=apple&page=2
def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    print('query: ', query, 'page: ', page)
    return "Hello"

if __name__=='__main__':
    app.run(debug=True, port=5000)