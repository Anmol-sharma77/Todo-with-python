from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
import random
import jwt  

app = Flask(__name__)
CORS(app)
import mysql.connector as sql
db=sql.connect(
    host="localhost",
    user="root",
    password="",
    database="react-todo")
cursor=db.cursor()

  
header = {  
  "alg": "HS256",  
  "typ": "JWT"  
}  

secret = "Ravipass"  

# @app.route('/signup', methods=['POST'])
# def signup():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')
#         email=data.get("email")
#         query="select * from user where email=%s"
#         cursor.execute(query, (email,))
#         result=cursor.fetchone()
#         if result:
#             return make_response('', 400)
#         id=random.randrange(340,2000)
#         query = """INSERT INTO user (userid,name, password, email,role) VALUES(%s,%s,%s,%s,%s)"""
#         cursor.execute(query,(id,username,password,email,"user"))
#         db.commit()
#         return make_response('', 200)

#     except Exception as e:
#         print(e)
#         return make_response('', 400)
@app.route('/todo', methods=['POST'])
def addemp():
    try:
        data=request.get_json()
        task=data["task"]
        id=data["id"]
        createdby=data["createdby"]
        flag=data["flag"]
        query="insert into todo values(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(id,task,createdby,flag))
        db.commit()
        return jsonify({'message':'Employee added successfully!'}),200
    except Exception as e:
        print(e)
        return jsonify({'error':'Something went wrong!'}),500

@app.route('/todos', methods=['GET'])
def data():
    query="select * from todo"
    cursor.execute(query)
    result=cursor.fetchall()
    employee_data = []
    for row in result:
        employee = {
            "id": row[0],
            "task": row[1],
            "createdby": row[2],
            "flag": row[3],
        }
        employee_data.append(employee)
    return jsonify(employee_data)
@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        data = request.get_json()
        emp_id = data.get('Employee_id')
        query = 'Delete From Employee Where Employee_Id = %s'
        cursor.execute(query, (emp_id,))
        db.commit()
        return make_response("", 200)
    except Exception as e:
        print(e)
        return make_response("Error Deleting the record", 400)

@app.route('/update', methods=['POST'])
def update():
    try:
        data = request.get_json()
        emp_id = data.get('Employee_id')
        name = data.get('name')
        department = data.get('department')
        position = data.get('position')
        phone = data.get('phone_num')
        email = data.get('email')
        if not all([emp_id,name,department,position,phone]):
            return make_response("Missing data", 400)
        else:
            query = '''UPDATE employee SET Name=%s, Department=%s, Position=%s, Phone_Num=%s,email=%s,Employee_id=%s WHERE Employee_ID=%s'''
            cursor.execute(query,(name,department,position,phone,email,emp_id,emp_id))
            db.commit()
            return make_response("Data updated successfully.", 200)
    except Exception as e:
        print(e)
        return make_response('Error in updating data', 400)
# @app.route('/login', methods=['POST'])
# def user_login():
#     data = request.get_json()
#     email=data.get("mail")
#     password = data.get('password')
#     query="select * from user where email=%s and password=%s"
#     cursor.execute(query,(email,password))
#     result=cursor.fetchone()
#     cols = [c[0] for c in cursor.description]
#     user = dict(zip(cols,result))
#     print(user)
#     if result==None:
#         return jsonify({'msg':"not found"}),404
    
#     token = jwt.encode({'role':user['role'],'id':user['userid']}, secret, algorithm='HS256', headers=header) 

#     if result:   
#         return jsonify({'user':user,'token':token}),200
#     else:
#         return make_response('', 400)
if __name__ == '__main__':
    app.run(debug=True)
