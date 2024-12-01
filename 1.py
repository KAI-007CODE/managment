import mysql.connector as sqltor
from tabulate import tabulate
import time
from colorama import Fore,Style,init

init()
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
     print(Fore.RED+"1.ADD SUPPLIERS")
     print(Fore.RED+"2.DELETE SUPPLIERS")
     print(Fore.RED+"3.UPDATE SUPPLIERS")
     print(Fore.RED+"4.VIEW SUPPLIERS")
     print(Fore.RED+"5.EXIT")
     chr=input(Fore.GREEN+"Enter your choice: ")
     if chr=='1':
          id= int(input(Fore.YELLOW+"enter supplier id: "))
          name=input("enter supplier name: ")
          address=input("enter supplier address: ")
          phone_number=int(input("enter supplier phone number: "))
          sql=cursor.execute("insert into SUPPLIERS (ID , NAME, ADDRESS, PHONE_NUMBER ) VALUES ({},'{}', '{}', {})".format(id, name, address, phone_number))
          cursor.execute(sql)
          myconn.commit()
          print('supplier details add succesfully')
          time.sleep(3)
          suppliers()
     if chr=='2':
          id = int(input(Fore.YELLOW+'enter supplier id you want to delete: '))
          sql = cursor.execute("delete from SUPPLIERS where ID=%s",(id,))
          myconn.commit()
          print('supplier deleted succesfully')
          time.sleep(3)
          suppliers()
     if chr=='3':
          id = int(input(Fore.YELLOW+"enter supplier id you want to update: "))
          name = input ("enter the updated supplier name: ")
          address = input("enter the updated supplier address: ")
          phone_number = int(input("enter the updated supplier phone number: "))
          sql=cursor.execute("UPDATE SUPPLIERS SET NAME=%s, ADDRESS=%s, PHONE_NUMBER=%s WHERE ID=%s",(name, address, phone_number, id))
          myconn.commit()
          print('supplier details updated succesfully')
          time.sleep(3)
          suppliers()
     if chr=='4':
          sql=cursor.execute("SELECT * FROM SUPPLIERS")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(Fore.RESET+(tabulate(rows,headers=columns,tablefmt="grid")))
          time.sleep(5)
          suppliers()
     if chr=='5':
          print(Fore.YELLOW+'\033[1mGOING BACK TO MAIN MENU\033[0m')
          main()
     else:
          print(Fore.RED+"\033[1mINVALID CHOICE\033[0m")
          suppliers()

#added bills data
def bills():  
     print(Fore.RED+"1.ADD BILLS")
     print(Fore.RED+"2.DELETE BILLS")
     print(Fore.RED+"3.UPDATE BILLS")
     print(Fore.RED+"4.VIEW BILLS")
     print(Fore.RED+"5. EXIT")
     chr = input(Fore.GREEN+"Enter your choice: ")
     if chr=='1':
          id = int(input(Fore.YELLOW+"enter bill id: "))
          name=input("enter customer name: ")
          amount=int(input("enter bill amount: "))
          sql=cursor.execute("insert into BILLS (UID , NAME, TOTAL_AMOUNT ) VALUES ({},'{}', {})".format(id, name, amount))
          cursor.execute(sql)
          myconn.commit()
          print('bill details add succesfully')
          time.sleep(3)
          bills()
     if chr=='2':
          id = int(input(Fore.YELLOW+'enter bill id you want to delete: '))
          sql = cursor.execute("delete from BILLS where UID=%s",(id,))
          myconn.commit()
          print('bill deleted succesfully')
          time.sleep(3)
          bills()
     if chr=='3':
          id = int(input(Fore.YELLOW+"enter bill id you want to update: "))
          name = input ("enter the updated customer name: ")
          amount = int(input("enter the updated bill amount: "))
          sql=cursor.execute("UPDATE BILLS SET NAME=%s, TOTAL_AMOUNT=%s WHERE UID=%s",(name, amount, id))
          myconn.commit()
          print('bill details updated succesfully')
          time.sleep(3)
          bills()
     if chr=='4':
          sql=cursor.execute("SELECT * FROM BILLS")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(Fore.WHITE+(tabulate(rows,headers=columns,tablefmt="grid")))
          time.sleep(5)
          bills()
     if chr=='5':
          print(Fore.YELLOW+'\033[1mGOING BACK TO MAIN MENU\033[0m')
          main()
     else:
          print(Fore.RED+"\033[1mINVALID CHOICE\033[0m")
          bills()

#added employee data
def employee():
     
          print(Fore.RED+"1. ADD EMPLOYEE ")
          print(Fore.RED+"2. DELETE EMPLOYEE ")
          print(Fore.RED+"3. UPDATE EMPLOYEE ")
          print(Fore.RED+"4. VIEW ALL EMPLOYEE ")
          print(Fore.RED+"5. EXIT")
          chr=input(Fore.GREEN+"Enter your choice: ")
          if chr=='1':
               id=int(input(Fore.YELLOW+"enter employee id: "))
               name=input("enter employee name: ")
               salary=int(input("enter employee salary: "))
               department=input("enter employee department: ")
               sql=cursor.execute("insert into EMPLOYEE (EMPLOYEE_ID , NAME, SALARY, DEPARTMENT ) VALUES ({},'{}',{}, '{}')".format(id, name, salary, department))
               cursor.execute(sql)
               myconn.commit()
               print('employee details add succesfully')
               time.sleep(3)
               employee()
          if chr=='2':
               id = int(input(Fore.YELLOW+'enter employee id you want to delete: '))
               sql = cursor.execute("delete from EMPLOYEE where EMPLOYEE_ID=%s",(id,))
               myconn.commit()
               print('employee deleted succesfully')
               time.sleep(3)
               employee()
          if chr=='3':
               id = int(input(Fore.YELLOW+"enter employee id you want to update: "))
               name = input ("enter the updated employee name: ")
               salary = int(input("enter the updated employee salary: "))
               department = input("enter the updated employee department: ")
               sql=cursor.execute("UPDATE EMPLOYEE SET NAME=%s, SALARY=%s, DEPARTMENT=%s WHERE EMPLOYEE_ID=%s",(name, salary, department, id))
               myconn.commit()
               print('employee details updated succesfully')
               time.sleep(3)
               employee()
          if chr=='4':
               sql=cursor.execute("SELECT * FROM EMPLOYEE")
               columns =[col[0] for col in cursor.description]
               rows=cursor.fetchall()
               print(Fore.RESET+(tabulate(rows,headers=columns,tablefmt="grid")))
               time.sleep(5)
               employee()
          if chr=='5':
               print(Fore.YELLOW+"\033[1mEXITING...\033[0m")
               main()
          else:
               print(Fore.RED+"\033[1mInvalid choice\033[0m")
               employee()

#added medicine data
def medicine():
    
          print(Fore.RED+"1.ADD MEDICINE ")
          print(Fore.RED+"2.DELETE MEDICINE ")
          print(Fore.RED+"3.UPDATE MEDICINE ")
          print(Fore.RED+"4.VIEW ALL MEDICINE ")
          print(Fore.RED+"5.EXIT")
          chr=input(Fore.GREEN+"Enter your choice: ")
          if chr=='1':
               id=int(input(Fore.YELLOW+"enter medicine id: "))
               name=input("enter medicine name: ")
               price=float(input("enter medicine price: "))
               quantity=int(input("enter medicine quantity: "))
               sql=cursor.execute("insert into MEDICINES (ID,NAME,PRICE,QUANTITY)values({},'{}',{},{})".format(id, name, price, quantity))
               cursor.execute(sql)
               myconn.commit()
               print('medicine details add succesfully')
               time.sleep(3)
               medicine()
          if chr=='2':
               id = int(input(Fore.YELLOW+'enter medicine id you want to delete: '))
               sql = cursor.execute("delete from medicines where id=%s",(id,))
               myconn.commit()
               print('medicine deleted succesfully')
               time.sleep(3)
               medicine()
          if chr=='3':
               id = int(input(Fore.YELLOW+"enter medicine id you wnat to update: "))
               name =input ("enter the updated medicine name: ")
               price =float(input("enter the updated medicine price: "))
               quantity =int(input("enter the updated maedicne quantity: "))
               sql=cursor.execute("UPDATE MEDICINES SET NAME=%s, PRICE=%s, QUANTITY=%s WHERE ID=%s",(name, price, quantity, id))
               myconn.commit()
               print('medicine details updated succesfully')
               time.sleep(3)
               medicine()
          if chr=='4':
               sql=cursor.execute("SELECT * FROM MEDICINES")
               columns=[col[0] for col in cursor.description]
               rows=cursor.fetchall()
               print(Fore.WHITE+(tabulate(rows,headers=columns,tablefmt="grid")))
               time.sleep(5)
               medicine()
          if chr==5:
               print(Fore.YELLOW+"\033[1mExiting the program\033[0m")
               main()
          else : 
               print(Fore.RED+"\033[1mInvalid choice\033[0m")
               medicine()

#defining main function which will run the program
def main():
     print(Fore.GREEN+"1. EMPLOYEE ")
     print(Fore.GREEN+"2. MEDICINE ")
     print(Fore.GREEN+"3. SUPPLIERS ")
     print(Fore.GREEN+"4. BILLS ")
     print(Fore.GREEN+"5. EXIT")
     choice=input("Enter your choice: ")
     if choice=='1':
          employee()
     elif choice=='2':
          medicine()
     elif choice=='3':
          suppliers()
     elif choice=='4':
          bills()
     elif choice=='5':
          print(Fore.RED+"\033[1mexiting...\033[0m")
          quit("""\033[1mThanks for using medicine management system\033[0m""")
     else:
          print(Fore.RED+"\033[1mInvalid choice\033[0m")
          main()
main()