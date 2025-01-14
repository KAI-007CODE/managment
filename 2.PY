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
     name=input(">>>").upper()
     print("ENTER AUTOR NAME")
     AUTHOR_name=input(">>>").upper()
     print("ENTER THE ISBN")
     ISBN=input(">>>").upper()
     print("ENTER THE GENRE OF THE BOOK")
     GEN=input(">>>").upper()
     print("PUBLISHER")
     PUB=input(">>>").upper()
     print("AVAILIBILITY STATUS")
     AVA=input(">>>").upper()

     SQL = "INSERT INTO BOOKS (TITTLE,AUTHOR,ISBN,GENRE,PUBLISHER,AVAILIBILY) VALUES('{}','{}','{}','{}','{}','{}')".format(name,AUTHOR_name,ISBN,GEN,PUB,AVA)
     cursor.execute(SQL)
     myconn.commit()
     time.sleep(2)
     print("BOOKS ADDED TO LIBRARY INVENTORY !!!")
     bookrelated()


def deletebook():
     print()
     print("ENTER THE ISBN NUMBER OF THE BOOK")
     N=input(">>>").upper()
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
     bookrelated()


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
          O=input(">>>").upper()
          print("ENTER THE NEW NAME OF THE BOOK")
          K=input(">>>").upper()
          cursor.execute(" UPDATE BOOKS SET TITTLE =%s WHERE ISBN =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 2:
          print()
          print("ENTER THE ISBN NUMBER OF THE BOOK")
          O=input(">>>").upper()
          print("ENTER THE NEW AUTHOR NAME OF THE BOOK")
          K=input(">>>").upper()
          cursor.execute(" UPDATE BOOKS SET AUTHOR =%s WHERE ISBN =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 3:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>").upper()
          print("ENTER THE NEW ISBN NUMBER OF THE BOOK")
          K=input(">>>").upper()
          cursor.execute(" UPDATE BOOKS SET ISBN =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 4:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>").upper()
          print("ENTER THE NEW PUBLISHER OF THE BOOK")
          K=input(">>>").upper()
          cursor.execute(" UPDATE BOOKS SET PUBLISHER =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 5:
          print()
          print("ENTER THE NAME OF THE BOOK")
          O=input(">>>").upper()
          print("ENTER THE NEW GENRE OF THE BOOK")
          K=input(">>>").upper()
          cursor.execute(" UPDATE BOOKS SET GENRE =%s WHERE TITTLE =%s"),(K,O)
          myconn.commit()
          print("DETAILS CHANGED SUCCESFULLY !!!")
          time.sleep(2)
          bookrelated()
     if N == 6:
          print()
          print("ENTER THE ISBN NUMBER OF THE BOOK")
          O=input(">>>").upper()
          print("ENTER THE NEW NAME OF THE BOOK")
          K=input(">>>").upper()
          print("ENTER THE NEW AUTHOR OF THE BOOK")
          P=input(">>>").upper()
          print("ENTER THE NEW PUBLISHER OF THE BOOK")
          Q=input(">>>").upper()
          print("ENTER THE NEW GENRE OF THE BOOK")
          R=input(">>>").upper()
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
     QUERY = "SELECT AVAILIBILY FROM BOOKS WHERE TITTLE = %s"
     cursor.execute(QUERY, (BOOK_NAME,))

     result=cursor.fetchone()
     if result and result[0] == "YES":
          cursor.execute("UPDATE BOOKS SET AVAILIBILY ='NO' WHERE TITTLE=%s", (BOOK_NAME,))
          myconn.commit()
          print()
          print("CHANGED !!!")
     else:
          cursor.execute("UPDATE BOOKS SET AVAILIBILY ='YES' WHERE TITTLE=%s",(BOOK_NAME,))
          myconn.commit()
          print()
          print("CHANGED !!!")
     bookrelated()


def returnbook():
     print()
     name=input("WHAT BOOK DO YOU WANT TO RETURN: ").upper()
     QUERY = "SELECT AVAILIBILY FROM BOOKS WHERE TITTLE = %s"
     cursor.execute(QUERY, (name,))

     result=cursor.fetchone()
     if result and result[0] == "NO":
          isbn=input("ENTER THE ISBN OF THE BOOK RETURNED: ").upper()
          # NAME=input("ENTER THE NAME OF THE BOOK TO BE BORROWED: ").upper()
          RETURNNAME=input("ENTER THE NAME OF THE PERSON WHO RETURNED THE BOOK: ").upper()
          ISSUEDATE=input("ENTER THE DATE THE BOOK WAS RETURNED(DD/MM/YYYY): ").upper()
          SQL="INSERT INTO RETURNBOOK (ISBN,BOOKNAME,RETURNEDBY,DATE) VALUES ('{}','{}','{}','{}') ".format(isbn,name,RETURNNAME,ISSUEDATE)
          cursor.execute(SQL)
          cursor.execute("UPDATE BOOKS SET AVAILIBILY ='YES' WHERE TITTLE=%s", (name,))
          myconn.commit()
          print("THE BOOK HAS BEEN RETURNED !!!")
     else: 
          print()
          print(f"THE BOOK {name} IS NOT AVAILABLE")
     userchoice()

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
     username=input("ENTER THE NEW USERNAME: ").upper()
     passkey=input("ENTER THE NEW PASSKEY: ").upper()
     cursor.execute("UPDATE ACCOUNT SET USERNAME =%s, PASSKEY =%s WHERE ID =%s",(username,passkey,id))
     myconn.commit()
     print("DETAILS UPDATED SUCCESFULLY")


def userchoice():
     print()
     print("1. CREATE A ACCOUNT.")
     print("2. SEARCH FOR A BOOK.")
     print("3. RETURN A BOOK.")
     print("4. QUIT")
     n=int(input(">>>"))
     if n==1:
          ID = input("ENTER ID : ").upper()
          username= input('ENTER YOUR NAME: ').upper()
          passkey= input('ENTER PASSWORD: ').upper()
          createaccount(ID, username,passkey)
          time.sleep(1)
          userchoice()
     if n==2:
          print("ENTER THE NAME OF THE BOOK")
          bookname=input(">>>").upper()
          searchbook(bookname)
     if n==3:
          returnbook()
     if n==4:
          time.sleep(3)
          quit("THANKS FOR USING OUR SYSTEM !!!")
     else:
          print("INVALID/UNKNOWN CHOICE")
          

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
          username= input(">>>").upper()
          searchuser(username)
          time.sleep(1)
          userrelated()
     if N==2:
          print("ENTER THE USER NAME OF THE PERSON.")
          username= input(">>>").upper()
          deleteuser(username)
          time.sleep(1)
          userrelated()
     if N==3:
          print("ENTER THE ID OF THE PERSON")
          n=(input(">>>")).upper()
          updateuser(n)
     if N ==4:
          adminchoice()
     else:
          print("INVAID CHOICE !!!")
def viewbook():
     print()
     print("1. DO YOU WANT TO SEE ALL THE BOOKS PRESENT IN THE LIBRARY ? ")
     print("2. DO YOU WNAT TO VIEW ALL THE AVAILABLE BOOKS IN THE MOMENT ?")
     print("3. DO YOU WANT TO VIEW BOOKS FROM SPECIFIC GENRE ?")
     n= input(">>>").upper()
     if n == "1":
          cursor.execute("SELECT * FROM BOOKS ")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(tabulate(rows,headers=columns,tablefmt="grid"))
          time.sleep(2)  
          bookrelated()
     if n == "2":
          cursor.execute("SELECT * FROM BOOKS WHERE AVAILIBILY = 'YES'")
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(tabulate(rows,headers=columns,tablefmt="grid"))
          time.sleep(2)
          bookrelated()
     if n=="3":
          print()
          print("ENTER THE GENRE OF BOOKS YOU WNAT TO SEARCH")
          gen=input(">>>").upper()
          sql=f"SELECT * FROM BOOKS WHERE GENRE = '{gen}'"
          cursor.execute(sql)
          columns=[col[0] for col in cursor.description]
          rows=cursor.fetchall()
          print(tabulate(rows,headers=columns,tablefmt="grid"))
          time.sleep(2)
          bookrelated()
     else:
          print()
          print("INVALID/UNKOWN CHOICE !!!")


def viewissuedbook():
     cursor.execute("SELECT * FROM ISSUEBOOK ")
     columns=[col[0] for col in cursor.description]
     rows=cursor.fetchall()
     print(tabulate(rows,headers=columns,tablefmt="grid"))
     time.sleep(2)  
     adminchoice()


def viewreturnedbook():
     cursor.execute("SELECT * FROM RETURNBOOK ")
     columns=[col[0] for col in cursor.description]
     rows=cursor.fetchall()
     print(tabulate(rows,headers=columns,tablefmt="grid"))
     time.sleep(2)  
     bookrelated()


def bookrelated():
     print()
     print("1. ADD NEW BOOK TO THE STOCK.")
     print("2. DELETE BOOK FROM THE STOCK.")
     print("3. UPDATE BOOK DETAILS.")
     print("4. SHOW ALL THE BOOK")
     print("5. CHANGE AVALIBILITY OF THE BOOK.")
     print("6. GO BACK TO PREVIOUS PAGE.")
     n=int(input(">>>"))

     if n==1:
          addbook()
     if n==2:
          deletebook()
     if n==3:
          updatebook()
     if n==4:
          viewbook()
     if n==5:
          n=input("ENTER THE BOOKS NAME: ").upper()
          changeavailable(n)
     if n==6:
          adminchoice()
     else:
          print()
          print("INVALID / UNKNOWN CHOICE !!!")


def issuebook():
     print()
     name=input("WHAT BOOK DO YOU WANT TO BORROW: ").upper()
     QUERY = "SELECT AVAILIBILY FROM BOOKS WHERE TITTLE = %s"
     cursor.execute(QUERY, (name,))

     result=cursor.fetchone()
     if result and result[0] == "YES":
          isbn=input("ENTER THE ISBN OF THE BOOK BORROWED: ").upper()
          # NAME=input("ENTER THE NAME OF THE BOOK TO BE BORROWED: ").upper()
          ISSUENAME=input("ENTER THE NAME OF THE PERSON THE BOOK IS BORRROWED TO: ").upper()
          ISSUEDATE=input("ENTER THE DATE THE BOOK WAS ISSUED(DD/MM/YYYY): ").upper()
          SQL="INSERT INTO ISSUEBOOK (ISBN,BOOKNAME,ISSUEDTO,DATE) VALUES ('{}','{}','{}','{}') ".format(isbn,name,ISSUENAME,ISSUEDATE)
          cursor.execute(SQL)
          cursor.execute("UPDATE BOOKS SET AVAILIBILY ='NO' WHERE TITTLE=%s", (name,))
          myconn.commit()
     else: 
          print()
          print(f"THE BOOK {name} IS NOT AVAILABLE")
     adminchoice()

def adminchoice():
     print()
     print("1. CREATE A ACCOOUNT.")
     print("2. USER RELATED TASK.")
     print("3. BOOKS RELATED TASK.")
     print("4. ISSUE A BOOK.")
     print("5. VIEW ALL THE ISUED BOOKS.")
     print("6. VIEW ALL THE RETURNED BOOK.")
     print("7. EXIT THE PROGRAM.")
     print("8. GO BACK TO HOME PAGGE.")
     n= int(input(">>>"))
     if n==1:
          ID = input("ENTER ID : ").upper()
          username= input('ENTER YOUR NAME: ').upper()
          passkey= input('ENTER PASSWORD: ').upper()
          createaccount(ID, username,passkey)
          time.sleep(1)
          adminchoice()
     if n==2:
          userrelated()
     if n==3:
          bookrelated()
     if n==4:
          issuebook()
     if n==5:
          viewissuedbook()
     if n==6:
          viewreturnedbook()
     if n==7:
          exit("THANKS FOR USING THE PROGRAM.")
     if n==8:
          print()
          user()


def user():
     print("WELCOME TO THE TOWN NEW LIBRARY")
     print()
     print("WHO ARE YOU ? (USER / ADMIN)")
     ob=input(">>>").upper()
     if ob == "USER" or ob =="user" :
          print("WAHT DO YOU WANT TO DO ?")
          time.sleep(1)
          userchoice()

     elif ob == "ADMIN" or ob =="admin":
          print("ENTER USERNAME")
          um=input(">>>").upper()
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
          time.sleep(2)
          user()


user()