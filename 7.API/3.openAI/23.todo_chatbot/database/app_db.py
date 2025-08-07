from flask import Flask, request, jsonify
from chatbot_routes import chatbot_bp
from todolist_routes import todo_bp


app = Flask(__name__, static_folder='public', static_url_path='')
app.register_blueprint(chatbot_bp, url_prefix='/api/chat')
app.register_blueprint(todo_bp)

@app.route('/')
def home():
    return app.send_static_file('index.html')




if __name__ =='__main__':
    app.run(debug=True)