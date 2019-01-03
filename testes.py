import mysql.connector as mysql

mydb = mysql.connect(
  host="127.0.0.1",
  user="root",passwd="123456",
  buffered=True,
  database="sakila"
)

mycursor = mydb.cursor()

mycursor.execute("select * from language")

columns = mycursor.description
print(columns)

# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)