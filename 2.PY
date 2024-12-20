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
               SUBSCRPTION VARCHAR(10) NOT NULL
               )""")
myconn.commit()
cursor.execute("""CREATE TABLE IF NOT EXISTS TOWNLIBRARY_BOOKS(
               BOOK_NAME VARCHAR(225) NOT NULL,
               BOOK_PRICE VARCHAR(5) NOT NULL,
               BOOKS_BARCODE VARCHAR(20) NOT NULL
               )""")
myconn.commit()

