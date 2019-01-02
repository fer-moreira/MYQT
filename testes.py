import mysql.connector as mysql

mydb = mysql.connect(
  host="127.0.0.1",
  user="root",passwd="123456",
  buffered=True
)

mycursor = mydb.cursor()

mycursor.execute("show databases")
mycursor.execute("use sakila")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)