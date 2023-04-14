import mysql.connector as conn


mydb = conn.connect(
  host="127.0.0.1",
  user="root",
  password="A1265913226y",
  database="classicmodels"
)

mycursor = mydb.cursor()

mycursor.execute(""" select customerName from customers  where country = "France" """)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)