from datetime import datetime
from flask import Flask, jsonify
from flask import request
current_time = datetime.utcnow().isoformat() + 'Z'

app = Flask(__name__)
todo=[]
@app.route("/todo/get", methods=["GET"])

def get_todo():
    if todo==[]:
        return jsonify({"message": "No items found"}), 404
    else:
        return jsonify(todo), 200
    
@app.route("/todo/<int:item>", methods=["GET"])
def single_todo(todo_id):
        for item in todo:
            if item['id']==todo_id:
                res= item
                return jsonify(res), 200
            else:
                return jsonify({"message:", " No todo item with that Id found, try again"}), 404

                 
@app.route("/todo/add" ,methods=["POST"])
def addTodo():
    if 'title' not in request.json:

        return jsonify({"message": "TITLE IS REQUIRED"}), 400
    
    
    title = request.json['title'].strip()
    if not isinstance(title, str):
        return jsonify({"message": "TITLE MUST BE A STRING"}), 400
    if len(title)==0:
        return jsonify({"message": "TITLE CANNOT BE EMPTY"}), 400
    if len(title) > 100:
        return jsonify({"message": "TITLE CANNOT EXCEED 100 CHARACTERS"}), 400

    desc = request.json['description'].strip()
    if not isinstance(desc, str):
        return jsonify({"message": "DESCRIPTION MUST BE A STRING"}), 400
    if len(desc) > 1000:
        return jsonify({"message": "DESCRIPTION CANNOT EXCEED 1000 CHARACTERS"}), 400
    
    todo_item= {
        'id': len(todo)+1,
        'title': title,
        'description': desc,
        'created_at': current_time,
        'updated_at': current_time,
    }
    todo.append(todo_item)
    return jsonify({"message": "Todo item added successfully"}), 201

@app.route("/todo/<int:item>", methods=["PUT"])
def update_todo(item):
    for  todo_item in todo:
        if todo_item['id'] == item:
            if 'title' not in request.json:
                return jsonify({"message": "TITLE IS REQUIRED"}), 400
            title = request.json['title'].strip()
            if not isinstance(title, str):
                return jsonify({"message": "TITLE MUST BE A STRING"}), 400
            if len(title) == 0:
                return jsonify({"message": "TITLE CANNOT BE EMPTY"}), 400
            if len(title) > 100:
                return jsonify({"message": "TITLE CANNOT EXCEED 100 CHARACTERS"}), 400

            desc = request.json['description'].strip()
            if not isinstance(desc, str):
                return jsonify({"message": "DESCRIPTION MUST BE A STRING"}), 400
            if len(desc) > 1000:
                return jsonify({"message": "DESCRIPTION CANNOT EXCEED 1000 CHARACTERS"}), 400

            todo_update = {
                'id': item,
                'title': title,
                'description': desc,
                'created_at': todo_item['created_at'],
                'updated_at': current_time,
            }
            todo.append(todo_update)
            todo.remove(todo_item)
            return jsonify({"message": "Todo item updated successfully"}), 201
    return jsonify({"message": "No todo item with that Id found, try again"}), 404


@app.route("/todo/<int:item>", methods=["DELETE"])
def delete_todo(item):
    for  todo_item in todo:
        if todo_item['id'] == item:
            todo.remove(todo_item)
            return jsonify({"message": "Todo item deleted successfully"}), 200
    return jsonify({"message": "No todo item with that Id found, try again"}), 404


@app.route('/')
def welcome():
    return "Welcome to the Todo API Service"

if __name__ == '__main__':
    app.run(debug=True, port=5000)