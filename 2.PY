import mysql.connector as mysql
import time
from tabulate import tabulate

myconn = mysql.connect(host="localhost", user="root", password= "arindam ak", database="townlibrary")
cursor=myconn.cursor()

def createaccount(ID, username, passkey):
     sql= "INSERT INTO ACCOUNT (ID ,USERNAME, PASSKEY)VALUES ('{}', '{}', '{}')".format(ID, username, passkey)
     cursor.execute(sql)
     myconn.commit()
     time.sleep(2)
     print("ACCOUNT CREATED !!!")

def searchbook(bookname):
     query="SELECT * FROM BOOK WHERE TITTLE LIKE %s"
     cursor.execute(query, ('%' +bookname+ '%',))
     result = cursor.fetchall()
     if result:
          columns=[col[0] for col in cursor.description]
          print(tabulate(result,headers=columns,tablefmt="grid"))
     else:
          print("BOOKS NOT FOUND !!!")

def searchuser(username):
     query="SELECT * FROM ACCOUNT WHERE USERNAME LIKE %s"
     cursor.execute(query, ('%' +username+ '%',))
     result = cursor.fetchall()
     if result:
          columns=[col[0] for col in cursor.description]
          print(tabulate(result,headers=columns,tablefmt="grid"))
     else:
          print("ACCOUNT NOT FOUND !!!")

def deleteuser(username):
     query="SELECT * FROM ACCOUNT WHERE USERNAME LIKE %s"
     cursor.execute(query, ('%' +username+ '%',))
     result = cursor.fetchall()
     if result:
          sql = "DELETE FROM ACCOUNT WHERE USERNAME LIKE %s"
          cursor.execute(sql,(username,))
          myconn.commit()
          print("USER DELETED SUCCESSFUL !!!")
     else:
          print("ACCOUNT NOT FOUND !!!")

def updateuser(id):
     username=input("ENTER THE NEW USERNAME: ")
     passkey=input("ENTER THE NEW PASSKEY: ")
     cursor.execute("UPDATE ACCOUNT SET USERNAME =%s, PASSKEY =%s WHERE ID =%s",(username,passkey,id))
     myconn.commit()
     print("DETAILS UPDATED SUCCESFULLY")


def userchoice():
     print()
     print("1. CREATE A ACCOUNT.")
     print("2. SEARCH FOR A BOOK.")
     print("3. RETURN A BOOK.")
     n=int(input(">>>"))
     if n==1:
          ID = input("ENTER ID : ")
          username= input('ENTER YOUR NAME: ')
          passkey= input('ENTER PASSWORD: ')
          createaccount(ID, username,passkey)
          time.sleep(1)
          userchoice()
     if n==2:
          print("ENTER THE NAME OF THE BOOK")
          bookname=input(">>>")
          searchbook(bookname)
          



def userrelated():
     print()
     print("1. SEARCH FOR USER.")
     print("2. DELETE USER DEATILS.")
     print("3. UPDATE USER DETAILS.")
     print("4. GO BACK TO PREVIOUS PAGE.")
     N=int(input(">>>"))
     print()
     if N==1:
          print("ENTER THE USER NAME OF THE PERSON.")
          username= input(">>>")
          searchuser(username)
          time.sleep(1)
          userrelated()
     if N==2:
          print("ENTER THE USER NAME OF THE PERSON.")
          username= input(">>>")
          deleteuser(username)
          time.sleep(1)
          userrelated()
     if N==3:
          print("ENTER THE ID OF THE PERSON")
          n=int(input(">>>"))
          updateuser(n)
     if N ==4:
          adminchoice()
     else:
          print("INVAID CHOICE !!!")




def adminchoice():
     print()
     print("1. CREATE A ACCOOUNT.")
     print("2. USER RELATED TASK.")
     print("3. BOOKS RELATED TASK.")
     print("4. EXIT THE PROGRAM.")
     n= int(input(">>>"))
     if n==1:
          ID = input("ENTER ID : ")
          username= input('ENTER YOUR NAME: ')
          passkey= input('ENTER PASSWORD: ')
          createaccount(ID, username,passkey)
          time.sleep(1)
          adminchoice()
     if n==2:
          userrelated()
     if n==4:
          exit("THANKS FOR USING THE PROGRAM.")





def user():
     print("WELCOME TO THE TOWN NEW LIBRARY")
     print()
     print("WHO ARE YOU ? (USER / ADMIN)")
     ob=input(">>>")
     if ob == "USER" or ob =="user" :
          print("WAHT DO YOU WANT TO DO ?")
          time.sleep(1)
          userchoice()

     elif ob == "ADMIN" or ob =="admin":
          print("ENTER USERNAME")
          um=input(">>>")
          print("ENTER YOUR PASSKEY")
          PASS= input(">>>")
          if um == "USER" and PASS=="password123" :
               time.sleep(1)
               adminchoice()
          else :
               print("YOU ARE NOT THE ADMIN!!!")
               time.sleep(3)
               user()
     else:
          print("INVALID CHOICE !!!")

user()