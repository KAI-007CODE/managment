import mysql.connector as sqltor
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

def employee():
     
          print("1. ADD EMPLOYEE ")
          print("2. DELETE EMPLOYEE ")
          print("3. UPDATE EMPLOYEE ")
          print("4. VIEW ALL EMPLOYEE ")
          print("5. EXIT")
          chr=int(input("Enter your choice: "))
          if chr==1:
               id=int(input("enter employee id"))
               name=input("enter employee name")
               salary=int(input("enter employee salary"))
               department=input("enter employee department")
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
               rows=cursor.fetchall()
               for row in rows:
                print(row)
               employee()
          if chr==5:
               print("exiting...")
               main()
          else:
               print("Invalid choice")
               employee()

def medicine():
    
          print("1.ADD MEDICINE ")
          print("2.DELETE MEDICINE ")
          print("3.UPDATE MEDICINE ")
          print("4.VIEW ALL MEDICINE ")
          print("5.EXIT")
          chr=int(input("Enter your choice: "))
          if chr==1:
               id=int(input("enter medicine id"))
               name=input("enter medicine name")
               price=float(input("enter medicine price"))
               quantity=int(input("enter medicine quantity"))
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
               rows=cursor.fetchall()
               for row in rows:
                print(row)
               medicine()
          if chr==5:
               print("exiting the program")
               main()
          else : 
               print("invalid choice")
               medicine()

def main():
     print("1. EMPLOYEE ")
     print("2. MESICINE ")
     print("3. EXIT")
     choice=int(input("Enter your choice: "))
     if choice==1:
          employee()
     elif choice==2:
          medicine()
     elif choice==3:
          print("exiting...")
     else:
          print("Invalid choice")
          quit("""thanks for using medicine management system""")
          
main()