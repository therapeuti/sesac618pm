from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = ['alice','bob','charlie','danny','echo']
    return render_template('index2.html', names=users)

if __name__=='__main__':
    app.run(debug=True, port=5000)