import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "30Fariz05"
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE TA_db")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)