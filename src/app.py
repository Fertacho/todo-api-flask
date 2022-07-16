from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]
todo  = [ { "label": "Sam67ple Todo 37434",  "done": True}, { "label": "My first task", "done": False }]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    dict = { "label": "My first task", "done": False }
    request_body = request.data
    json_text = jsonify(todo)
    print(request_body)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    print("This is the position to delete: ",position)
    return 'something'



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)