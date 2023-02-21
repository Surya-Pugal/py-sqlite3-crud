'''
Created on 

@author: Surya

source:
   
'''

from flask import Flask, request
import sqlite3


conn = sqlite3.connect('hobby.db', check_same_thread=False)
print("Opened database successfully")

c = conn.cursor()
# c.execute("CREATE TABLE hobbies(id int primary key, name varchar(20), hobby1 varchar (30), hobby2 varchar(30))")

app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello'

    
# a) insert 5 records into the table by getting values from the user with flask
@app.route('/insert', methods=['GET', 'POST'])
def insert():
    # print("inserted values")
    id = request.args.get("id")
    name=request.args.get("name")
    hobby1=request.args.get("hobby1")
    hobby2=request.args.get("hobby2")
    print(f"INSERT INTO hobbies(id, name, hobby1, hobby2) values({id}, '{name}', '{hobby1}', '{hobby2}')")
    c.execute(f"INSERT INTO hobbies(id, name, hobby1, hobby2) values({id}, '{name}', '{hobby1}', '{hobby2}')")
    conn.commit()
    values = get()
    return values

# b) update hobby2 to 'swimming' of the person with id = 3
@app.route('/update', methods=['GET','POST'])
def update():
    print("update")
    id = request.args.get("id")
    hobby2=request.args.get("hobby2")
    print(f'id={id},hobby2={hobby2}')
    print(f"UPDATE hobbies SET hobby2 = {hobby2} where id = {id}")
    c.execute(f"UPDATE hobbies SET hobby2 = {hobby2} where id = {id}")
    conn.commit()
    values = get()
    return values


# c) delete a row where the id = 5
@app.route('/delete')
def delete():
    id = request.args.get("id")
    print(f"DELETE FROM hobbies where id={id}")
    c.execute(f"DELETE FROM hobbies where id={id}")
    conn.commit()
    values = get()
    print("Deleted")
    return values


@app.route('/getall', methods=['GET', 'POST'])
def get():
    values=conn.execute("SELECT * FROM hobbies")

    emp_list=[]
    for value in values:
        emp_list.append(value)
    print(emp_list) 

    return emp_list



if __name__ == '__main__':
    app.run(debug = True)


