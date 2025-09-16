import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")