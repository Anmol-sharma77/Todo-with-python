import uuid
import mysql.connector as sql
from flask import jsonify as json

db = sql.connect(
    host="localhost",
    user="root",
    database="tododatabase" 
)

cursor = db.cursor()

def create_todo(todo):
    print(todo)
    try:
        todo = {
            'id':str(uuid.uuid4()),
            'title': todo['title'],
            'discription': todo['description'],
            'date':todo['date'],
            'status':'pending',
            'enddate':todo['enddate'],
            'starttime':todo['starttime'],
            'endtime':todo['endtime']
        }
        cursor.execute('insert into todo values(%s,%s,%s,%s,%s,%s,%s,%s)',tuple(todo.values()))
        db.commit()
        if cursor.rowcount>0:
            return json({'msg':"success",'todo':todo}),200
        else:
            return json({'msg':'Something went wrong'}),304
    except Exception as e:
        print(e)
        return json({'err':'intenal server error'}),500
    
def get_todos():
    try:
        cursor.execute('select * from todo')
        cols = [c[0] for c in cursor.description]
        todos = [dict(zip(cols,row)) for row in cursor.fetchall()]
        return json(todos),200
    except Exception as e:
        return json({'err':'internal server error : %s'%repr(e)}),500
    
def delete_todo(body):
    try:
        cursor.execute('delete from todo where id = "%s"'%body['id'])
        db.commit()
        if cursor.rowcount>0:
            return json({'msg':'success'}),200
        else:
            return json({'msg':'error occured while deleting'}),304
    except Exception as e:
        return json({'err':repr(e)}),500
    

def update_status(body):
    try:
        cursor.execute('update todo set status = "%s"'%body['status']+' where id = "%s"'%body['id'])
        db.commit()
        if cursor.rowcount>0:
            return json({'msg':'success'}),200
        else:
            return json({'msg':'error while updating status'}),304
    except Exception as e:
        print(e)
        return json({'err':repr(e)}),500
    

def update_task(body):
    print(body)
    try:
        cursor.execute('update todo set title=%s, discription=%s, date=%s,enddate=%s,starttime=%s,endtime=%s where id=%s',(body['title'],body['description'],body['date'],body['enddate'],body['date'],body['enddate'],body['id']))
        print(cursor)
        db.commit()
        return "",200
    except Exception as e:
        print(repr(e))
        db.rollback()
        return json({'err':repr(e)}),500