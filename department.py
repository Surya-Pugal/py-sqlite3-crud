import sqlite3

'''
Created on 

@author: Surya

source: https://www.geeksforgeeks.org/python-sqlite-join-clause/
    
'''


def startpy():
    print("Table created")
    # create tables()
    insert(106, 'Rama', 'priya', 'Buffalo', 25000.3, 70, 'Engineering', 143, 'USA')
    update(100, 'Ram', 'Sunil', 'HongKong', 48000, 10, 'Finance', 154, 'China')
    read()
 



conn=sqlite3.connect('department.db')
c=conn.cursor()

# def create tables():
c.execute("""CREATE TABLE Employee
(Emp_ID int primary key unique, First_Name Text, Last_Name Text, Address varchar(30) not null, Salary real, Dep_ID int)""")
c.execute("""CREATE Table Department
(Dep_ID int primary key unique, Dep_Name Text not null, Manager_Id numeric, Location Text)""")
    # conn.commit()

def insert(emp_id, fname, lname, add, salary,dep_id, depname, mg_id, loc):
    c.execute(f"INSERT INTO Employee(Emp_ID, First_Name, Last_Name, Address, Salary, Dep_ID) values ({emp_id}, '{fname}', '{lname}', '{add}', {salary}, {dep_id})")
    c.execute(f"INSERT INTO Department(Dep_ID, Dep_Name, Manager_Id, Location) values({dep_id}, '{depname}', {mg_id}, '{loc}')")
    conn.commit()


def update(emp_id, fname, lname, add, salary,dep_id, depname, mg_id, loc):
    # c.execute(f"UPDATE Employee SET Dep_ID = 20 where Emp_ID = 101")
    c.execute(f"INSERT INTO Employee(Emp_ID, First_Name, Last_Name, Address, Salary, Dep_ID) values ({emp_id}, '{fname}', '{lname}', '{add}', {salary}, {dep_id})")
    c.execute(f"INSERT INTO Department(Dep_ID, Dep_Name, Manager_Id, Location) values({dep_id}, '{depname}', {mg_id}, '{loc}')")
    conn.commit()

def read():

    #Inner join
    values = c.execute(f"""SELECT Employee.Emp_ID, Employee.First_Name, 
    Employee.Last_Name, Department.Dep_Name, Employee.Salary
    FROM Employee
    INNER JOIN Department ON Employee.Dep_ID=Department.Dep_ID""") 

    # Left join
    values = c.execute(f"""SELECT Employee.Emp_ID, Employee.First_Name,
    Employee.Last_Name, Department.Location
    From Employee
    LEFT JOIN DEPARTMENT ON Employee.Dep_ID=Department.Dep_ID""")

    #Right join
    values = c.execute(f"""SELECT Employee.Emp_ID, Department.Dep_Name, Department.Location
    From Employee
    RIGHT JOIN DEPARTMENT on Employee.Dep_ID=Department.Dep_ID""")

    #Full outer join
    values =c.execute(f"""SELECT Employee.First_Name, Employee.Salary, Department.Manager_ID, Department.Location
    From Employee
    FULL OUTER JOIN Department on Employee.Dep_ID=Department.Dep_ID
    ORDER BY Employee.First_Name""")

    # Self join
    values=c.execute(f"""SELECT Employee.Emp_ID AS EmpID1, Employee.Salary AS Sal, Department.Location as Loc
    From Employee, Department
    WHERE Employee.Emp_ID <> Department.Dep_ID
    ORDER BY Salary""")


    for value in values:
        print(value)
    conn.commit()


if __name__ == '__main__':
    startpy()

