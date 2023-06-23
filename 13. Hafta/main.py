import exceptiongroup
import pymysql
import sys
from PyQt5 import QtWidgets, QtCore
from login import Ui_Login
from anasayfa import Ui_MainWindow
from pymysql import Connection
from PyQt5.QtCore import pyqtSignal #Bu veriyi sayfadan sayfaya aktarmak için lazım olacak.

import pymysql

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.signIn.clicked.connect(self.kayit)
        self.ui.logIn.clicked.connect(self.giris)


        self.ui.userName.setText("deneme")
        self.ui.password.setText("123456")

        self.connection = pymysql.connect(host="104.247.165.163", port=3306, user="greenro2_p115", passwd="A1265913226y+",
                                     database="greenro2_p115_chat")

        self.dialog = Ui_MainWindow()  # İkinci sayfamızın sınıfı, bunu çağırabilmek için kullanacağız.



    def arkadas_ekle(self):
        cursor = self.connection.cursor()

        k_id = self.dialog.kisiler.selectedItems()[0].text()

        sorgu0 = f"select ad, soyad from kullanıcılar where k_ıd = '{k_id}' "
        cursor.execute(sorgu0)

        arkadas = cursor.fetchall()

        f_adi = str(arkadas[0][0])
        f_soyadi = str(arkadas[0][1])

        varmı = False
        for i in range(self.dialog.myFriends.count()):
            if k_id == self.dialog.myFriends.item(i).text():
                varmı = True


        if varmı :
            QtWidgets.QMessageBox.information(self, "Bilgi", "Bu kişi ile zaten arkadaşsınız")

        else:
            sorgu = "INSERT INTO `friend` VALUES (%s, %s, %s, %s);"

            cursor.execute(sorgu, (self.k_adi, k_id, f_adi, f_soyadi))

            self.connection.commit()

        self.refresh()



    def kayit(self):

        try:
            cursor = self.connection.cursor()

            k_adi = self.ui.userName.text()
            sifre = self.ui.password.text()

            sql = ("SELECT * FROM `kullanıcılar` WHERE `k_ıd`=%s AND `password`=%s")
            cursor.execute(sql, (k_adi, sifre))

            myresult = cursor.fetchmany()

            if myresult:
                QtWidgets.QMessageBox.information(self, "Bilgi", "Bu kişi zaten kayıtlı")
            else:
                sorgu = " INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');"

                cursor.execute(" INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');")
                self.connection.commit()

                QtWidgets.QMessageBox.information(self, "Bilgi", "Kayıt Başarılı")


        except Exception as err:
            print("Kayıt Başarısız => ", err)

    def giris(self):
        cursor = self.connection.cursor()

        self.k_adi = self.ui.userName.text()
        self.sifre = self.ui.password.text()

        #sorgu = "SELECT * FROM `kullanıcılar` WHERE `k_ıd`='{k_adi}' AND `password`='{sifre}'".format(k_adi,sifre)

        sql = ("SELECT * FROM `kullanıcılar` WHERE `k_ıd`=%s AND `password`=%s")
        cursor.execute(sql, (self.k_adi, self.sifre))

        myresult = cursor.fetchmany()

        if myresult:
            self.girisYap()
        else:
            print("Kullanıcı yok")

        self.connection.commit()


    def girisYap(self):
        self.dialog.setupUi(self)
        self.dialog.addFriends.clicked.connect(self.arkadas_ekle)

        cursor = self.connection.cursor()

        sql = ("SELECT * FROM `kullanıcılar`")
        cursor.execute(sql)

        myresult = cursor.fetchall()

        for i in myresult:
            self.dialog.kisiler.addItem(i[0])

        sql = ("SELECT * FROM friend")

        cursor.execute(sql)

        myresult2 = cursor.fetchall()

        for i in myresult2:
            print(i[0])
            self.dialog.comboBox.addItem(i[1])
            self.dialog.myFriends.addItem(i[1])


        self.connection.commit()

    def refresh(self):

        self.dialog.kisiler.clear()
        self.dialog.comboBox.clear()
        self.dialog.myFriends.clear()

        cursor = self.connection.cursor()

        sql = ("SELECT * FROM `kullanıcılar`")
        cursor.execute(sql)

        myresult = cursor.fetchall()

        for i in myresult:
            self.dialog.kisiler.addItem(i[0])

        sql = ("SELECT * FROM friend")

        cursor.execute(sql)

        myresult2 = cursor.fetchall()

        for i in myresult2:
            print(i[0])
            self.dialog.comboBox.addItem(i[1])
            self.dialog.myFriends.addItem(i[1])


        self.connection.commit()




app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())




"""
cursor.execute(
    "    
    CREATE TABLE `p115chat`.`friend` (`kullanıcı_ıd` VARCHAR(50) NOT NULL , `friends_ıd` VARCHAR(50) NOT NULL ) ENGINE = InnoDB;
    "
)"""




