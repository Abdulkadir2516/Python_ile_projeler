import pymysql
import sys

connection = pymysql.connect(host="104.247.165.163", port=3306, user="greenro2_p115", passwd="A1265913226y+", database="greenro2_p115_chat")
cursor = connection.cursor()

cursor.execute(
    """
    Create Table if not exists kullanicilar 
    (k_ad int, şifre int, ad int, soyad int ,tel int)

    """
)
"""
cursor.execute(
    "CREATE TABLE `p115chat`.`friend` (`kullanıcı_ıd` VARCHAR(50) NOT NULL , `friends_ıd` VARCHAR(50) NOT NULL ) ENGINE = InnoDB; "
)"""

connection.close()