from flask import Flask, jsonify
from flask import request
from flask import json

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]
todo  = [ { "label": "Sam67ple Todo 37434",  "done": True}]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body =json.loads(request.data)
    todos.append(request_body)
    print(todos)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    print("This is the position to delete: ",position)
    return json_text



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)