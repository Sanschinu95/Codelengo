import mysql.connector

mydb= mysql.connector.connect (host="localhost", 
                               user="root",
                               password = "", 
                               database="school")

mycursor = mydb.cursor ()
mycursor.execute("CREATE TABLE student (Rollno int (3) Primary key, Name varchar (15), age integer, city char (8))")
