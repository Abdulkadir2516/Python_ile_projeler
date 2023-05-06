import sys
import PyQt5

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
win = QMainWindow()

win.setWindowTitle("P115 PyQt5")
win.setGeometry(0,0,200,200)

lbl_1 = QtWidgets.QLabel(win)
lbl_1.setText("Uygulamamıza Hoş Geldiniz: ")
lbl_1.setGeometry(25,1,200,50)

lbl_2 = QtWidgets.QLabel(win)
lbl_2.setText("Adınız: ")
lbl_2.move(10,52)

txt_1 = QtWidgets.QLineEdit(win)
txt_1.move(60,52)

lbl_3 = QtWidgets.QLabel(win)
lbl_3.setText("Soyadınız: ")
lbl_3.move(10,90)

txt_2 = QtWidgets.QLineEdit(win)
txt_2.move(60,90)

btn_1 = QtWidgets.QPushButton(win)
btn_1.setText("Bana Basma")
btn_1.setGeometry(25,120,100,30)

lbl_4 = QtWidgets.QLabel(win)
lbl_4.setGeometry(25,160,100,30)


def bas():
    sonuc = "İsim => " + txt_1.text() + "  " + txt_2.text()
    print(sonuc)
    lbl_4.setText(sonuc)
    # lbl_4.setMinimumWidth(len(sonuc)) #setMinimumSize(30,len(sonuc))
    # print(int(txt_1.text()) + int(txt_2.text()))


btn_1.clicked.connect(bas)


win.show()
sys.exit(app.exec_())
