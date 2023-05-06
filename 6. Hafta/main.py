import sys # sistem ile ilgili kütüphane
from PyQt5 import QtWidgets #
from pencere import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.yedi.clicked.connect(self.fonksiyon)

    def fonksiyon(self):
        self.ui.input_text.setText("7")


app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())