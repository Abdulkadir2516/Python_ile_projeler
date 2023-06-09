import sys # sistem ile ilgili kütüphane

from PyQt5 import QtWidgets
from makro import Ui_MainWindow
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener
from pynput import keyboard, mouse
from pynput.mouse import Button, Controller
import pyautogui
import time

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.play.clicked.connect(self.fonksiyon)
        self.ui.record.clicked.connect(self.kaydet)
        self.ui.stop.clicked.connect(self.durdur)

    def durdur(self):
        self.key_listener.stop()
        self.mouse_listener.stop()


    def on_move(self, x, y):
        print("{},{}".format(x, y))

    def on_click(self, x, y, button, pressed):
        if pressed:
            print("{},{}".format(x, y))
            self.rowPosition = self.ui.tablo.rowCount()
            self.ui.tablo.insertRow(self.rowPosition)
            self.ui.tablo.setItem(self.rowPosition, 0, QtWidgets.QTableWidgetItem(str(button)))
            self.ui.tablo.setItem(self.rowPosition, 1, QtWidgets.QTableWidgetItem("{},{}".format(x, y)))
            self.ui.tablo.setItem(self.rowPosition, 2, QtWidgets.QTableWidgetItem(" "))
            self.ui.tablo.setItem(self.rowPosition, 3, QtWidgets.QTableWidgetItem(" "))

    def on_press(self, key):
        print("basılan tus => {}".format(key))


    def kaydet(self):

        self.key_listener = keyboard.Listener(on_press=self.on_press)
        self.key_listener.start()

        self.mouse_listener = mouse.Listener(on_click=self.on_click, on_move=self.on_move)
        self.mouse_listener.start()


    def fonksiyon(self):

        deneme = Controller()

        for i in range(self.ui.tablo.rowCount()):
            aksiyon = self.ui.tablo.item(i,0).text().split(".")[1]
            self.x = self.ui.tablo.item(i,1).text().split(",")[0]
            self.y = self.ui.tablo.item(i,1).text().split(",")[1]

            print(aksiyon,"   ", self.x ,"  ,  ", self.y)

            #deneme.move(0, 0)
            time.sleep(3)
            #deneme.press(Button(aksiyon))
            #deneme.release(Button(aksiyon))
            pyautogui.click(button=str(aksiyon), x = int(self.x), y=int(self.y))






app = QtWidgets.QApplication(sys.argv)
win = myApp()
win.show()
sys.exit(app.exec_())











