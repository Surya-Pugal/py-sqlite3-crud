'''
Created on 

@author: Surya

source:
   
'''

from flask import Flask, request
import sqlite3

conn=sqlite3.connect('customer.db', check_same_thread=False)
print("The database connected")

# conn.execute("""CREATE TABLE orderdetails (Order_id integer primary key, 
# First_Name Text(20), Last_Name Text(30), Phone_No int unique not null, City varchar(20), State varchar(10), Country varchar(20))""")


app=Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return "Hello"

@app.route('/insert',methods=['GET', 'POST'])
def insert():
    print("Order details has been inserted")
    id = request.args.get("Order_id")
    fname=request.args.get("First_Name")
    lname=request.args.get("Last_Name")
    phno=request.args.get("Phone_No")
    city=request.args.get("City")
    state=request.args.get("State")
    country=request.args.get("Country")
    print(f"""INSERT INTO orderdetails(Order_id, First_Name, Last_Name, 
    Phone_No, City, State, Country) values({id}, '{fname}', '{lname}', {phno}, '{city}', '{state}', '{country}')""")
    conn.execute(f"""INSERT INTO orderdetails(Order_id, First_Name, Last_Name, 
    Phone_No, City, State, Country) values({id}, '{fname}', '{lname}', {phno}, '{city}', '{state}', '{country}')""")
    conn.commit()
    insert_value=read()
    return insert_value

@app.route('/update',methods=['GET','POST'])
def update():
    id=request.args.get("Order_id")
    # fname=request.args.get("First_Name")
    # lname=request.args.get("Last_Name")
    city=request.args.get("City")
    # state=request.args.get("State")
    # country=request.args.get("Country")
    # print(f"UPDATE orderdetails SET City = '{city}', State ='{state}', Country ='{country}' where Order_id ={id}")
    print(f"UPDATE orderdetails SET City = '{city}' where Order_id ={id}")
    conn.execute(f"UPDATE orderdetails SET City = '{city}' where Order_id ={id}")
    # print(f"UPDATE orderdetails SET Last_Name ='{lname}' where Order_id ={id}")
    # conn.execute(f"UPDATE orderdetails SET Last_Name ='{lname}' where Order_id ={id}")
    # conn.execute(f"UPDATE orderdetails SET City = '{city}', State ='{state}', Country ='{country}' where Order_id ={id}")
    conn.commit()
    update_value=read()
    return update_value

@app.route('/delete',methods=['Get','POST'])
def delete():
    id=request.args.get("Order_id")
    conn.execute(f"DELETE FROM orderdetails where Order_id={id}")
    conn.commit()
    delete_value=read()
    return delete_value

@app.route('/getvalue', methods=['GET', 'POST'])
def read():
    values=conn.execute("SELECT * FROM orderdetails")
    print(f"read values: {values}")

    emp_list=[]
    for value in values:
        print(f"inside for: {value}")
        emp_list.append(value)
    return emp_list



if __name__ == '__main__':
    app.run(debug=True)