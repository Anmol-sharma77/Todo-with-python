from flask import Flask, render_template, jsonify as json, request as req
from controlleres import create_todo, get_todos, delete_todo, update_status, update_task

app = Flask(__name__)

@app.route("/",methods=['GET'])
def loadHome():
    return render_template("todo.html")

@app.route("/todo",methods=['GET','PUT','POST','DELETE','PATCH'])
def api():
    match(req.method):
        case 'POST':
            return create_todo(req.json)
        case 'GET':
            return get_todos()
        case 'DELETE':
            return delete_todo(req.json)
        case 'PATCH':
            return update_status(req.json)
        case 'PUT':
            return update_task(req.json)
    
if __name__=="__main__":
    app.run(debug=True)