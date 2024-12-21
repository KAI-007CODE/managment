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

def addbook():
     print()
     print("ENTER THE NAME OF THE BOOK")
     name=input(">>>")
     print("ENTER AUTOR NAME")
     AUTHOR_name=input(">>>")
     print("ENTER THE ISBN")
     ISBN=input(">>>")
     print("ENTER THE GENRE OF THE BOOK")
     GEN=input(">>>")
     print("PUBLISHER")
     PUB=input(">>>")
     print("AVAILIBILITY STATUS")
     AVA=input(">>>")

     SQL = "INSERT INTO BOOKS (TITTLE,AUTHOR,ISBN,GENRE,PUBLISHER,AVAILIBILY) VALUES('{}','{}','{}','{}','{}','{}')".format(name,AUTHOR_name,ISBN,GEN,PUB,AVA)
     cursor.execute(SQL)
     myconn.commit()
     time.sleep(2)
     print("BOOKS ADDED TO LIBRARY INVENTORY !!!")


def deletebook():
     print()
     print("ENTER THE ISBN NUMBER OF THE BOOK")
     N=input(">>>")
     query = "SELECT ALL FROM BOOKS WHERE ISBN LIKE %s"
     cursor.execute(query,(N,))
     result = cursor.fetchall()
     if result:
          sql = "DELETE FROM BOOKS WHERE ISBN LIKE %s"
          cursor.execute(sql,(N,))
          myconn.commit()
          time.sleep(1)
          print("BOOK HAS BEEN DELETED !!!")
     else:
          print("BOOK NOT FOUND !!!")


def updatebook():
     print()
     print("WHAT DO YOU WANT TO UPDATE ?")
     print("""1. TITTLE.
     2. AUTHOUR.
     3. ISBN.
     4. PUBLISHER.
     5. GENRE.
     6. ALL DETAILS EXCEPT ISBN NUMBER.
     """)
     N=int(input(">>>"))
     if N == 1:
          print()
          print("ENTER THE ISBN NUMBER OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW NAME OF THE BOOK")
          K=input(">>>")
          cursor.execute(" UPDATE BOOKS SET TITTLE =%s WHERE ISBN =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 2:
          print()
          print("ENTER THE ISBN NUMBER OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW AUTHOR NAME OF THE BOOK")
          K=input(">>>")
          cursor.execute(" UPDATE BOOKS SET AUTHOR =%s WHERE ISBN =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 3:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW ISBN NUMBER OF THE BOOK")
          K=input(">>>")
          cursor.execute(" UPDATE BOOKS SET ISBN =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 4:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW PUBLISHER OF THE BOOK")
          K=input(">>>")
          cursor.execute(" UPDATE BOOKS SET PUBLISHER =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 5:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW GENRE OF THE BOOK")
          K=input(">>>")
          cursor.execute(" UPDATE BOOKS SET GENRE =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 6:
          print()
          print("ENTER THE ISBN NUMBER OF THE BOOK")
          O=input(">>>")
          print("ENTER THE NEW NAME OF THE BOOK")
          K=input(">>>")
          print("ENTER THE NEW AUTHOR OF THE BOOK")
          P=input(">>>")
          print("ENTER THE NEW PUBLISHER OF THE BOOK")
          Q=input(">>>")
          print("ENTER THE NEW GENRE OF THE BOOK")
          R=input(">>>")
          cursor.execute(" UPDATE BOOKS SET TITTLE =%s, AUTHOR=%s, PUBLISHER=%s, GENRE=%s WHERE ISBN =%s"),(K,P,Q,R,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     else:
          print("INVALID / UNKNOWN CHOICE")
          time.sleep(1.5)
          updatebook()


def changeavailable(BOOK_NAME):
     y="YES"
     n="NO"
     QUERY = f"SELECT AVAILIBILITY FROM BOOKS WHERE NAME='{BOOK_NAME}'"
     if QUERY=="YES":
          sql=f"UPDATE BOOKS SET AVAILIBILITY ='{n}' WHERE BOOK_NAME='{BOOK_NAME}' "
          cursor.execute(sql)
          myconn.commit()
          print()
          print("CHANGED !!!")
     else:
          sql=f"UPDATE BOOKS SET AVAILIBILITY ='{y}' WHERE BOOK_NAME='{BOOK_NAME}' "
          cursor.execute(sql)
          myconn.commit()
          print()
          print("CHANGED !!!")


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


def bookrelated():
     print()
     print("1. ADD NEW BOOK TO THE STOCK.")
     print("2. DELETE BOOK FROM THE STOCK.")
     print("3. UPDATE BOOK DETAILS.")
     print("4. CHANGE AVALIBILITY OF THE BOOK.")
     print("5. GO BACK TO PREVIOUS PAGE.")
     n=int(input(">>>"))

     if n==1:
          addbook()
     if n==2:
          deletebook()
     if n==3:
          updatebook()
     if n==4:
          changeavailable()
     if n==5:
          adminchoice()
     else:
          print()
          print("INVALID / UNKNOWN CHOICE !!!")


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