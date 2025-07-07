from flask import Flask, request

app = Flask(__name__)

@app.route('/') 
def home():
    
    return """
    <html>
    <head></head>
    <body>
    <h1>Hello, Flask</h1>
    <h2>안녕하세요</h2>
    <p>상품목록</p>
    <div>
        <ul>
            <li>아메리카노</li>
            <li>카페라떼</li>
            <li>돌체라떼</li>
        </ul>
    </div>
    </body>
    </html>
    """

if __name__=='__main__':
    app.run(debug=True, port=5000)