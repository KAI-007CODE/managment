import mysql.connector as sqltor
from tabulate import tabulate
myconn = sqltor.connect(user='root', password='arindam ak', host='127.0.0.1')
cursor= myconn.cursor()
cursor.execute('CREATE DATABASE  IF NOT EXISTS mydatabase')
cursor.execute('USE mydatabase')
cursor.execute("""CREATE TABLE IF NOT EXISTS EMPLOYEE (
               EMPLOYEE_ID INT PRIMARY KEY, 
               NAME VARCHAR(255),
               SALARY INT,
               DEPARTMENT VARCHAR(255))""")
myconn.commit()
cursor.execute('CREATE TABLE IF NOT EXISTS MEDICINES(ID INT PRIMARY KEY, NAME VARCHAR (100),PRICE INT,QUANTITY INT)')
myconn.commit()
cursor.execute('CREATE TABLE IF NOT EXISTS SUPPLIERS(ID INT PRIMARY KEY, NAME VARCHAR (100), ADDRESS VARCHAR (255), PHONE_NUMBER VARCHAR(50))')
myconn.commit()
cursor.execute('CREATE TABLE IF NOT EXISTS BILLS(UID INT PRIMARY KEY, NAME VARCHAR(255), TOTAL_AMOUNT INT)')
myconn.commit()

#added suppliers data
def suppliers():
     print("1.ADD SUPPLIERS")
     print("2.DELETE SUPPLIERS")
     print("3.UPDATE SUPPLIERS")
     print("4.VIEW SUPPLIERS")
     print("5.EXIT")
     chr=int(input("Enter your choice: "))
     if chr==1:
          id= int(input("enter supplier id: "))
          name=input("enter supplier name: ")
          address=input("enter supplier address: ")
          phone_number=int(input("enter supplier phone number: "))
          sql=cursor.execute("insert into SUPPLIERS (ID , NAME, ADDRESS, PHONE_NUMBER ) VALUES ({},'{}', '{}', {})".format(id, name, address, phone_number))
          cursor.execute(sql)
          myconn.commit()
          print('supplier details add succesfully')
          suppliers()
     if chr==2:
          id = int(input('enter supplier id you want to delete: '))
          sql = cursor.execute("delete from SUPPLIERS where ID=%s",(id,))
          myconn.commit()
          print('supplier deleted succesfully')
          suppliers()
     if chr==3:
          id = int(input("enter supplier id you want to update: "))
          name = input ("enter the updated supplier name: ")
          address = input("enter the updated supplier address: ")
          phone_number = int(input("enter the updated supplier phone number: "))
          sql=cursor.execute("UPDATE SUPPLIERS SET NAME=%s, ADDRESS=%s, PHONE_NUMBER=%s WHERE ID=%s",(name, address, phone_number, id))
          myconn.commit()
          print('supplier details updated succesfully')
          suppliers()
     if chr==4:
          sql=cursor.execute("SELECT * FROM SUPPLIERS")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(tabulate(rows,headers=columns,tablefmt="grid"))
          suppliers()
     if chr==5:
          print('GOING BACK TO MAIN MENU')
          main()
     else:
          print("INVALID CHOICE")
          suppliers()

#added bills data
def bills():  
     print("1.ADD BILLS")
     print("2.DELETE BILLS")
     print("3.UPDATE BILLS")
     print("4.VIEW BILLS")
     print("5. EXIT")
     chr = int(input("Enter your choice: "))
     if chr==1:
          id = int(input("enter bill id: "))
          name=input("enter customer name: ")
          amount=int(input("enter bill amount: "))
          sql=cursor.execute("insert into BILLS (UID , NAME, TOTAL_AMOUNT ) VALUES ({},'{}', {})".format(id, name, amount))
          cursor.execute(sql)
          myconn.commit()
          print('bill details add succesfully')
          bills()
     if chr==2:
          id = int(input('enter bill id you want to delete: '))
          sql = cursor.execute("delete from BILLS where UID=%s",(id,))
          myconn.commit()
          print('bill deleted succesfully')
          bills()
     if chr==3:
          id = int(input("enter bill id you want to update: "))
          name = input ("enter the updated customer name: ")
          amount = int(input("enter the updated bill amount: "))
          sql=cursor.execute("UPDATE BILLS SET NAME=%s, TOTAL_AMOUNT=%s WHERE UID=%s",(name, amount, id))
          myconn.commit()
          print('bill details updated succesfully')
          bills()
     if chr==4:
          sql=cursor.execute("SELECT * FROM BILLS")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(tabulate(rows,headers=columns,tablefmt="grid"))
          bills()
     if chr==5:
          print('GOING BACK TO MAIN MENU')
          main()
     else:
          print("INVALID CHOICE")
          bills()

#added employee data
def employee():
     
          print("1. ADD EMPLOYEE ")
          print("2. DELETE EMPLOYEE ")
          print("3. UPDATE EMPLOYEE ")
          print("4. VIEW ALL EMPLOYEE ")
          print("5. EXIT")
          chr=int(input("Enter your choice: "))
          if chr==1:
               id=int(input("enter employee id: "))
               name=input("enter employee name: ")
               salary=int(input("enter employee salary: "))
               department=input("enter employee department: ")
               sql=cursor.execute("insert into EMPLOYEE (EMPLOYEE_ID , NAME, SALARY, DEPARTMENT ) VALUES ({},'{}',{}, '{}')".format(id, name, salary, department))
               cursor.execute(sql)
               myconn.commit()
               print('employee details add succesfully')
               employee()
          if chr==2:
               id = int(input('enter employee id you want to delete: '))
               sql = cursor.execute("delete from EMPLOYEE where EMPLOYEE_ID=%s",(id,))
               myconn.commit()
               print('employee deleted succesfully')
               employee()
          if chr==3:
               id = int(input("enter employee id you want to update: "))
               name = input ("enter the updated employee name: ")
               salary = int(input("enter the updated employee salary: "))
               department = input("enter the updated employee department: ")
               sql=cursor.execute("UPDATE EMPLOYEE SET NAME=%s, SALARY=%s, DEPARTMENT=%s WHERE EMPLOYEE_ID=%s",(name, salary, department, id))
               myconn.commit()
               print('employee details updated succesfully')
               employee()
          if chr==4:
               sql=cursor.execute("SELECT * FROM EMPLOYEE")
               columns =[col[0] for col in cursor.description]
               rows=cursor.fetchall()
               print(tabulate(rows,headers=columns,tablefmt="grid"))
               employee()
          if chr==5:
               print("exiting...")
               main()
          else:
               print("Invalid choice")
               employee()

#added medicine data
def medicine():
    
          print("1.ADD MEDICINE ")
          print("2.DELETE MEDICINE ")
          print("3.UPDATE MEDICINE ")
          print("4.VIEW ALL MEDICINE ")
          print("5.EXIT")
          chr=int(input("Enter your choice: "))
          if chr==1:
               id=int(input("enter medicine id: "))
               name=input("enter medicine name: ")
               price=float(input("enter medicine price: "))
               quantity=int(input("enter medicine quantity: "))
               sql=cursor.execute("insert into MEDICINES (ID,NAME,PRICE,QUANTITY)values({},'{}',{},{})".format(id, name, price, quantity))
               cursor.execute(sql)
               myconn.commit()
               print('medicine details add succesfully')
               medicine()
          if chr==2:
               id = int(input('enter medicine id you want to delete: '))
               sql = cursor.execute("delete from medicines where id=%s",(id,))
               myconn.commit()
               print('medicine deleted succesfully')
               medicine()
          if chr==3:
               id = int(input("enter medicine id you wnat to update: "))
               name =input ("enter the updated medicine name: ")
               price =float(input("enter the updated medicine price: "))
               quantity =int(input("enter the updated maedicne quantity: "))
               sql=cursor.execute("UPDATE MEDICINES SET NAME=%s, PRICE=%s, QUANTITY=%s WHERE ID=%s",(name, price, quantity, id))
               myconn.commit()
               print('medicine details updated succesfully')
               medicine()
          if chr==4:
               sql=cursor.execute("SELECT * FROM MEDICINES")
               columns=[col[0] for col in cursor.description]
               rows=cursor.fetchall()
               print(tabulate(rows,headers=columns,tablefmt="grid"))
               medicine()
          if chr==5:
               print("exiting the program")
               main()
          else : 
               print("invalid choice")
               medicine()

#defining main function which will run the program
def main():
     print("1. EMPLOYEE ")
     print("2. MEDICINE ")
     print("3. SUPPLIERS ")
     print("4. BILLS ")
     print("5. EXIT")
     choice=int(input("Enter your choice: "))
     if choice==1:
          employee()
     elif choice==2:
          medicine()
     elif choice==3:
          suppliers()
     elif choice==4:
          bills()
     elif choice==5:
          print("exiting...")
          quit("""thanks for using medicine management system""")
     else:
          print("Invalid choice")
          main()
main()