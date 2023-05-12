import sys # sistem ile ilgili kütüphane
from PyQt5 import QtWidgets #
from pencere import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):



    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.islem = []

        self.ui.sifir.clicked.connect(self.yaz)
        self.ui.bir.clicked.connect(self.yaz)
        self.ui.iki.clicked.connect(self.yaz)
        self.ui.uc.clicked.connect(self.yaz)
        self.ui.dort.clicked.connect(self.yaz)
        self.ui.bes.clicked.connect(self.yaz)
        self.ui.alti.clicked.connect(self.yaz)
        self.ui.yedi.clicked.connect(self.yaz)
        self.ui.sekiz.clicked.connect(self.yaz)
        self.ui.dokuz.clicked.connect(self.yaz)

        self.ui.full_sil.clicked.connect(self.silme)
        self.ui.sil.clicked.connect(self.silme)

        self.ui.arti.clicked.connect(self.islemler)
        self.ui.eksi.clicked.connect(self.islemler)
        self.ui.bol.clicked.connect(self.islemler)
        self.ui.carpi.clicked.connect(self.islemler)

        self.ui.esittir.clicked.connect(self.result)

    def result(self):
        self.islem.append(float(self.ui.input_text.text()))
        self.sonuc = self.islem[0]
        for i in range(1, len(self.islem)):
            if type(self.islem[i]) != "float":
                if self.islem[i] == "+":
                    self.sonuc += self.islem[i+1]
                elif self.islem[i] == "-":
                    self.sonuc -= self.islem[i+1]
                elif self.islem[i] == "*":
                    self.sonuc *= self.islem[i+1]
                elif self.islem[i] == "/":
                    self.sonuc /= self.islem[i+1]

        self.ui.input_text.setText(str(self.sonuc))
        self.islem = []

    def islemler(self):

        tagname = self.sender().text()

        if tagname == "+":
            self.islem.append(float(self.ui.input_text.text()))
            self.islem.append(tagname)
            self.silme()
            print(self.islem)
        elif tagname == "-":
            self.islem.append(float(self.ui.input_text.text()))
            self.islem.append(tagname)
            self.silme()
            print(self.islem)
        elif tagname == "/":
            self.islem.append(float(self.ui.input_text.text()))
            self.islem.append(tagname)
            self.silme()
            print(self.islem)
        elif tagname == "*":
            self.islem.append(float(self.ui.input_text.text()))
            self.islem.append(tagname)
            self.silme()
            print(self.islem)

    def silme(self):

        tagname = self.sender().text()
        if tagname == "<--":
            self.ui.input_text.setText(self.ui.input_text.text()[0:-1])
        else:
            self.ui.input_text.setText("")



    def yaz(self):

        tagname = self.sender().text()
        if tagname == "0":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "1":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "2":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "3":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "4":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "5":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "6":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "7":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "8":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)
        elif tagname == "9":
            self.ui.input_text.setText(self.ui.input_text.text() + tagname)




app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())