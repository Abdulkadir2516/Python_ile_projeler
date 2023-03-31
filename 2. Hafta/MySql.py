import mysql.connector as conn


mydb = conn.connect(
  host="localhost",
  user="root",
  password="A1265913226y",
  database="classicmodels"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers limit 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)