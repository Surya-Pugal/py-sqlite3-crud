'''
Created on 

@author: Surya

source:
   
'''

from flask import Flask, request
import sqlite3

conn = sqlite3.connect('employee.db', check_same_thread=False)

app=Flask(__name__)

@app.route('/')
def home():
    return 'welcome'

@app.route('/insert', methods=['GET', 'POST'])
def insert():
    conn.execute("INSERT INTO employee (id , empName, empContactNo, empAddress, empSalary) values (2, 'Sivasree', 987654356, 'Chennai', 50000)")
    conn.commit()
    values = read()
    return values


@app.route('/update')
def update():
    id = request.args.get("id")
    contact=request.args.get("contact")
    conn.execute(f"UPDATE employee SET empContactNo = {contact} where id = {id}")
    conn.commit()
    values = read()
    return values

@app.route('/delete')
def delete():
    conn.execute("DELETE FROM employee where id = 4")
    conn.commit()
    values = read()
    return values



def read():
    values = conn.execute("SELECT * FROM employee")
    
    emp_list=[]
    for value in values:
        emp_list.append(value)
    return emp_list 





# def startpy():

#     print("Tact101")
    

if __name__ == '__main__':
    app.run(debug == True)