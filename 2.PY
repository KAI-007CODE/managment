import mysql.connector as mysql


myconn = mysql.connect(host="localhost", user="root", password= "arindam ak", database="townlibrary")
cursor=myconn.cursor()
