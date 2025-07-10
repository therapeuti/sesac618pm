from flask import Flask, send_file, jsonify
# 프론트 엔드를 내가 서빙하거나... cors 추가를 하거나...
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return 'HI'

@app.route('/')
def index():
    return send_file('4.fetch.html')

@app.route('/data')
def data():
    return jsonify({'result':'success', 'message':'안녕하세요 반갑습니다 /data'})

if __name__=='__main__':
    app.run(debug=True)