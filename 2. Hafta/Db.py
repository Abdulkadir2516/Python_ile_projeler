import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
# create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS users
                  (k_ad TEXT, şifre TEXT, ad TEXT, soyad TEXT,tel TEXT)
               """)
"""
cursor.execute("INSERT INTO users
                  VALUES ('greenrock','2516','Abdulkadir','Yeşilkaya','5459727734'),
                         ('deneme','1234','test','dene','5541524515')
                  "
               )
# save data
"""
conn.commit()

for i in cursor.execute("Select * From users"):
    print(i)