import pymysql
import sys
from PyQt5 import QtWidgets, QtCore
from login import Ui_Login

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.signIn.clicked.connect(self.kayit)



    def kayit(self):
        cursor = connection.cursor()

        k_adi = self.ui.userName.text()
        sifre = self.ui.password.text()

        sorgu = " INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');"

        cursor.execute(" INSERT INTO `kullanıcılar` (`k_ıd`, `password`) VALUES ('"+k_adi+"', '"+sifre+"');")

        connection.commit()

        connection.close()





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




