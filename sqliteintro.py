import sqlite3


'''
Created on 

@author: Surya

source:
    
'''

def startpy():

    # print("Tact101")
    # insert(4, "Sakshara", 976553765, "Mumbai", 30000)
    # update(60000)
    # delete(2)
    read()


conn = sqlite3.connect('employee.db')
c=conn.cursor()
# c.execute("create table employee(id integer primary key, empName varchar(20), empContactNo Int, empAddress varchar(30), empSalary)")

def insert(id, empName, empContactNo, empAddress, empSalary):
    conn.execute(f"""INSERT INTO EMPLOYEE (id, empName, empContactNo, empAddress, empSalary) VALUES
    ({id},'{empName}', {empContactNo}, '{empAddress}', {empSalary}); """)
    conn.commit()

def update(newsalary):
    conn.execute(f"update employee set empSalary = {newsalary} where id = 3")
    conn.commit()

def delete(id):
    conn.execute(f"delete from employee where id = {id}")
    conn.commit()

def read():
    values=conn.execute("select * from employee where empName='Chaaya'")

    for value in values:
        print(value)
    # print(values)


if __name__ == '__main__':
    startpy()
  