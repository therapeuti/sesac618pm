from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Example data structure to hold todos
todos = []

@app.route('/')
def index():
    return render_template('index.html')

# Route to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to add a new todo
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    todos.append(todo)
    return jsonify({'message': 'Todo added successfully!'}), 201

# Route to update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id] = request.json.get('todo')
        return jsonify({'message': 'Todo updated successfully!'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

# Route to delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
        return jsonify({'message': 'Todo deleted successfully!'})
    else:
        return jsonify({'error': 'Todo not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)