import mysql.connector
import random

# creating a database, tabale(townlibrary)
myconn= mysql.connector.connect(host="localhost",user="root",password="arindam ak")
cursor = myconn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS  TOWNLIBRARY")
cursor.execute("USE TOWNLIBRARY")
cursor.execute("""CREATE TABLE IF NOT EXISTS TOWNLIBRARY (
               USER_ID VARCHAR(10) PRIMARY KEY,
               USER_NAME VARCHAR(225) NOT NULL,
               DOC VARCHAR(10) NOT NULL,
               SUBSCRIPTION VARCHAR(10) NOT NULL
               )""")
myconn.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS TOWNLIBRARY_BOOKS(
               BOOK_NAME VARCHAR(225) NOT NULL,
               BOOK_PRICE VARCHAR(5) NOT NULL,
               BOOKS_BARCODE VARCHAR(20) NOT NULL FOREIGN KEY
               )""")
myconn.commit()

#funtion to add a new user
def newuser():
     name=input("ENTER THE NAME OF THE USER: ")
     doc=input("ENTER TODAYS DATE: ")
     sub=input("ENTER THE TYPE OF SUBSCRIPTION CHOOSEN BY THE USER(BASIC/PREMIUM/VIP): ")
     id =input("ENTER A ID TO ASSIGN TO THE USER: ")
     sql="INSERT INTO TOWNLIBRARY(USER_ID,USER_NAME,DOC,SUBSCRIPTION) VALUES ('{}','{}','{}','{}')".format(id,name, doc, sub)
     cursor.execute(sql)
     myconn.commit()

# funtion to books present in the library
def books():
     b_name=input("ENTER THE NAME OF THE BOOK: ")
     b_price=input("ENTER THE PRICE OF THE BOOK: ")
     b_barcode=input("ENTER THE BARCODE DETAILS OF THE BOOKS: ")
     sql="INPUT INTO TOWNLIBRARY_BOOKS(BOOK_NAME,BOOK_PRICE,BOOK_BARCODE) VALUES ('{}','{}','{}')".format(b_name,b_price,b_barcode)
     cursor.execute(sql)
     myconn.commit()
