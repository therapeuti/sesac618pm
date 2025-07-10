from flask import Flask, jsonify, send_file, request, redirect, url_for, render_template
import uuid

app = Flask(__name__)

todolist = [{'id':'0','todo': '1번', 'status': 0}, 
            {'id':'1','todo': '2번', 'status': 0}, 
            {'id':'2','todo': '3번', 'status': 1}]

@app.route('/')
def index():
    return render_template('todolist.html', todolist=todolist)


@app.route('/add', methods=['POST'])
def add_todolist():
    global todolist
    print('메소드 받았니?')
    print(request)
    data = request.form.get('todo')
    print(data)
    u_id = uuid.uuid4()
    new_todo = {'id':str(u_id) ,'todo':data, 'status':0}
    todolist.append(new_todo)
    print(todolist)
    return redirect(url_for('index'))


@app.route('/delete/<id>')
def delete_todolist(id):
    global todolist
    print(id)
    for i in range(len(todolist)):
        print(todolist[i]['id'])
        if todolist[i]['id'] == id:
            del todolist[i]
            break
    print(todolist)
    return redirect(url_for('index'))

@app.route('/edit_status/<id>')
def edit_status(id):
    print(id)
    for li in todolist:
        print(li['id'])
        if li['id'] == id:
            print(li['status'])
            if li['status'] == 1:
                li['status'] = 0
            else:
                li['status'] = 1
            print(li['status'])
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)