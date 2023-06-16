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




    def kayit(self):

        try:
            cursor = self.connection.cursor()

            k_adi = self.ui.userName.text()
            sifre = self.ui.password.text()

            sorgu = " INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');"

            cursor.execute(" INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');")
            self.connection.commit()

            QtWidgets.QMessageBox.information(self, "Bilgi", "Kayıt Başarılı")

        except Exception as err:
            print("Kayıt Başarısız => ", err)

    def giris(self):
        cursor = self.connection.cursor()

        k_adi = self.ui.userName.text()
        sifre = self.ui.password.text()

        #sorgu = "SELECT * FROM `kullanıcılar` WHERE `k_ıd`='{k_adi}' AND `password`='{sifre}'".format(k_adi,sifre)

        sql = ("SELECT * FROM `kullanıcılar` WHERE `k_ıd`=%s AND `password`=%s")
        cursor.execute(sql, (k_adi, sifre))

        myresult = cursor.fetchmany()

        if myresult:
            self.girisYap()
        else:
            print("Kullanıcı yok")

        self.connection.commit()


    def girisYap(self):
        self.dialog.setupUi(self)

        cursor = self.connection.cursor()

        sql = ("SELECT * FROM `kullanıcılar`")
        cursor.execute(sql)

        myresult = cursor.fetchall()

        for i in myresult:
            print(i[0])
            self.dialog.kisiler.addItem(i[0])

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




