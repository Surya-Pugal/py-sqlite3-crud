import sqlite3


'''
Created on 

@author: Surya

source:
    
'''

def startpy():
    insert(1, "Rahul", 9876654356, "Trichy", 33760.45)





conn = sqlite3.connect('customer.db')
c=conn.cursor()

# c.execute("create table customerdetails(custID int primary key, custName varchar(20), custContactNo Int, custAddress varchar(30), custSalary float(8,2))")

def insert(custID, custName, custContactNo, custAddress, custSalary):
    conn.execute(f"""INSERT INTO CUSTOMERDETAILS (custID, custName, custContactNo, custAddress, custSalary) VALUES
    ({custID},'{custName}', {custContactNo}, '{custAddress}', {custSalary}); """)
    conn.commit()

if __name__ == '__main__':
    startpy()