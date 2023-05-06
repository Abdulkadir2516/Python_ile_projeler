import sys
import PyQt5

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class myApp(QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.setWindowTitle("P115 PyQt5")
        self.setGeometry(0, 0, 300, 250)
        self.yukle()

    def yukle(self):

        self.lbl_1 = QtWidgets.QLabel(self)
        self.lbl_1.setText("Uygulamamıza Hoş Geldiniz: ")
        self.lbl_1.setGeometry(25, 1, 200, 50)

        self.lbl_2 = QtWidgets.QLabel(self)
        self.lbl_2.setText("Sayı1: ")
        self.lbl_2.move(10, 52)

        self.txt_1 = QtWidgets.QLineEdit(self)
        self.txt_1.move(60, 52)

        self.lbl_3 = QtWidgets.QLabel(self)
        self.lbl_3.setText("Sayı2: ")
        self.lbl_3.move(10, 90)

        self.lbl_4 = QtWidgets.QLabel(self)
        self.lbl_4.setText("Sonuç: ")
        self.lbl_4.move(10, 135)

        self.txt_2 = QtWidgets.QLineEdit(self)
        self.txt_2.move(60, 90)

        self.txt_3 = QtWidgets.QLineEdit(self)
        self.txt_3.move(60, 135)

        self.btn_1 = QtWidgets.QPushButton(self)
        self.btn_1.setText("Toplama")
        self.btn_1.setGeometry(200, 50, 100, 30)

        self.btn_2 = QtWidgets.QPushButton(self)
        self.btn_2.setText("Çıkartma")
        self.btn_2.setGeometry(200, 80, 100, 30)

        self.btn_3 = QtWidgets.QPushButton(self)
        self.btn_3.setText("Çarpma")
        self.btn_3.setGeometry(200, 110, 100, 30)

        self.btn_4 = QtWidgets.QPushButton(self)
        self.btn_4.setText("Bölme")
        self.btn_4.setGeometry(200, 140, 100, 30)

        self.btn_1.clicked.connect(self.hesapla)
        self.btn_2.clicked.connect(self.hesapla)
        self.btn_3.clicked.connect(self.hesapla)
        self.btn_4.clicked.connect(self.hesapla)

    def hesapla(self):
        isim = self.sender().text()

        if isim == "Toplama":
            sonuc = int(self.txt_1.text()) + int(self.txt_2.text())
        elif isim == "Çıkartma":
            sonuc = int(self.txt_1.text()) - int(self.txt_2.text())
        elif isim == "Çarpma":
            sonuc = int(self.txt_1.text()) * int(self.txt_2.text())
        elif isim == "Bölme":
            sonuc = int(self.txt_1.text()) / int(self.txt_2.text())

        print(sonuc)
        self.txt_3.setText(str(sonuc))


app = QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())
