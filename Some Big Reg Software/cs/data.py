import mysql.connector as sqlcon

my_db = sqlcon.connect( 
    host = "localhost",
    user = "username",
    password = "password",
    database = "Ramakrishna_Mission"
)

mycursor = my_db.cursor()
sql = "INSERT INTO Student (Name,Roll_no) VALUES (%s, %s)"
val = ("Sanskar", "95")

mycursor.execute(sql,val)
my_db.commit()

print(mycursor.rowcount, "details inserted")

my_db.close()
