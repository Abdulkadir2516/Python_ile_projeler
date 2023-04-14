import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("P115 PyQt5")
    # win.setMinimumHeight(500)
    # win.setMaximumSize(250,250)

    win.setGeometry(0,0,280,390)
    win.setWindowIcon(QIcon("./icon.png"))
    win.setToolTip("My Tooltip")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("İsminiz:")
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soy İsminiz:")
    lbl_surname.move(50, 70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.setText("Abdulkadir")
    txt_name.move(120, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.setText("Yeşilkaya")
    txt_surname.move(120, 70)

    lbl_isim = QtWidgets.QLabel(win)
    lbl_isim.setText("")
    lbl_isim.move(60, 110)

    def click(self):
        print("Adınız =>" + txt_name.text() + "\nSoyadınız =>" + txt_surname.text())
        lbl_isim.setText(txt_name.text() + "  " + txt_surname.text())


    btn_goster = QtWidgets.QPushButton(win)
    btn_goster.setText("Kaydet")
    btn_goster.move(80,150)
    btn_goster.clicked.connect(click)


    win.show()
    sys.exit(app.exec_())

window()


