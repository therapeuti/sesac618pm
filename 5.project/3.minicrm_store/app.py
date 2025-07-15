from flask import Flask, render_template, request, redirect
import database as db


app = Flask(__name__)

@app.route('/')
def index():
    stores = db.get_stores()

    if request:
        print('요청 들어옴')
        print(request.args.get('q', ''))
        query = request.args.get('q','').strip()
        stores = db.search_stores(query)

    return render_template('index.html', stores=stores, query=query)




if __name__=='__main__': # flask run으로 실행하면 이 아래는 실행되지 않음. 
    app.run(debug=True)