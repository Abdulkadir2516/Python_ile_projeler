import sys # sistem ile ilgili kütüphane
from PyQt5 import QtWidgets
from makro import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.fonksiyon)

    def fonksiyon(self):
        self.rowPosition = self.ui.tablo.rowCount()
        self.ui.tablo.insertRow(self.rowPosition)
        self.ui.tablo.setItem(self.rowPosition, 0, QtWidgets.QTableWidgetItem("İşlem id"))
        self.ui.tablo.setItem(self.rowPosition, 1, QtWidgets.QTableWidgetItem("Eylem ismi"))
        self.ui.tablo.setItem(self.rowPosition, 2, QtWidgets.QTableWidgetItem("Değer"))
        self.ui.tablo.setItem(self.rowPosition, 3, QtWidgets.QTableWidgetItem("Açıklama"))



app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())