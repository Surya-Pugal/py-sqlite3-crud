import sqlite3


'''
Created on 

@author: Surya

source:
    
'''

def startpy():
    print("Table has been created...")
    # insert(123, "Rajesh", "M", 41753666, "Samsung fit", "India")
    # update(123, "Scotland")
    # delete(102)
    read()



conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute("""CREATE TABLE customerdetails(cus_id int PRIMARY KEY, cus_name Text(30), Gender char(1),
contactno int NOT NULL UNIQUE, product_details varchar (30), address varchar(30))""")
   
def insert(id, name, gender, phno, product, add):
    c.execute(f"""INSERT INTO customerdetails (cus_id, cus_name, Gender, contactno, product_details, address)
    values({id}, '{name}', '{gender}', {phno}, '{product}', '{add}')""")
    conn.commit()

def update(id,add):
    c.execute(f"UPDATE customerdetails SET address='{add}' where cus_id={id}")
    conn.commit()

def delete(id):
    c.execute(f"DELETE FROM customerdetails where cus_id={id}")
    conn.commit()

def read():
   value = c.execute("SELECT * FROM customerdetails")

   for values in value:
    print(values)


if __name__ == '__main__':
    startpy()