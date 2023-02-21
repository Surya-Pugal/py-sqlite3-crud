import sqlite3


'''
Created on 

@author: Surya

source:
    
'''

def startpy():
    print("Table created")





conn = sqlite3.connect('customer.db')
c=conn.cursor()

c.execute("create table customer(custID int primary key, first_name varchar(30), last_name varchar(20), custContactNo int, Address varchar(30), City(20), PostalCode varchar(20), Country varchar(20))")

if __name__ == '__main__':
    startpy()


