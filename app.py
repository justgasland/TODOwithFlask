from flask import Flask, jsonify

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

                 
# @app.route("/todo/add" ,method=["PUT"])
# def addTodo()
    

