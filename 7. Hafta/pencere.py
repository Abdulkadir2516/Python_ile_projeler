# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(50000, 50000))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/yesil/Downloads/star.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(30, 30, 171, 41))
        self.input_text.setAcceptDrops(True)
        self.input_text.setObjectName("input_text")
        self.arti = QtWidgets.QPushButton(self.centralwidget)
        self.arti.setEnabled(True)
        self.arti.setGeometry(QtCore.QRect(210, 80, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.arti.sizePolicy().hasHeightForWidth())
        self.arti.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.arti.setFont(font)
        self.arti.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.arti.setMouseTracking(False)
        self.arti.setFocusPolicy(QtCore.Qt.TabFocus)
        self.arti.setObjectName("arti")
        self.eksi = QtWidgets.QPushButton(self.centralwidget)
        self.eksi.setEnabled(True)
        self.eksi.setGeometry(QtCore.QRect(210, 120, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eksi.sizePolicy().hasHeightForWidth())
        self.eksi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eksi.setFont(font)
        self.eksi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.eksi.setMouseTracking(False)
        self.eksi.setFocusPolicy(QtCore.Qt.TabFocus)
        self.eksi.setObjectName("eksi")
        self.bol = QtWidgets.QPushButton(self.centralwidget)
        self.bol.setEnabled(True)
        self.bol.setGeometry(QtCore.QRect(210, 160, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bol.sizePolicy().hasHeightForWidth())
        self.bol.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bol.setFont(font)
        self.bol.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bol.setMouseTracking(False)
        self.bol.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bol.setObjectName("bol")
        self.carpi = QtWidgets.QPushButton(self.centralwidget)
        self.carpi.setEnabled(True)
        self.carpi.setGeometry(QtCore.QRect(210, 200, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carpi.sizePolicy().hasHeightForWidth())
        self.carpi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.carpi.setFont(font)
        self.carpi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.carpi.setMouseTracking(False)
        self.carpi.setFocusPolicy(QtCore.Qt.TabFocus)
        self.carpi.setObjectName("carpi")
        self.esittir = QtWidgets.QPushButton(self.centralwidget)
        self.esittir.setEnabled(True)
        self.esittir.setGeometry(QtCore.QRect(150, 200, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.esittir.sizePolicy().hasHeightForWidth())
        self.esittir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.esittir.setFont(font)
        self.esittir.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.esittir.setMouseTracking(False)
        self.esittir.setFocusPolicy(QtCore.Qt.TabFocus)
        self.esittir.setObjectName("esittir")
        self.full_sil = QtWidgets.QPushButton(self.centralwidget)
        self.full_sil.setEnabled(True)
        self.full_sil.setGeometry(QtCore.QRect(90, 200, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_sil.sizePolicy().hasHeightForWidth())
        self.full_sil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.full_sil.setFont(font)
        self.full_sil.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.full_sil.setMouseTracking(False)
        self.full_sil.setFocusPolicy(QtCore.Qt.TabFocus)
        self.full_sil.setObjectName("full_sil")
        self.dokuz = QtWidgets.QPushButton(self.centralwidget)
        self.dokuz.setEnabled(True)
        self.dokuz.setGeometry(QtCore.QRect(150, 80, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dokuz.sizePolicy().hasHeightForWidth())
        self.dokuz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dokuz.setFont(font)
        self.dokuz.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dokuz.setMouseTracking(False)
        self.dokuz.setFocusPolicy(QtCore.Qt.TabFocus)
        self.dokuz.setObjectName("dokuz")
        self.sifir = QtWidgets.QPushButton(self.centralwidget)
        self.sifir.setEnabled(True)
        self.sifir.setGeometry(QtCore.QRect(30, 200, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sifir.sizePolicy().hasHeightForWidth())
        self.sifir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sifir.setFont(font)
        self.sifir.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sifir.setMouseTracking(False)
        self.sifir.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sifir.setObjectName("sifir")
        self.sekiz = QtWidgets.QPushButton(self.centralwidget)
        self.sekiz.setEnabled(True)
        self.sekiz.setGeometry(QtCore.QRect(90, 80, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sekiz.sizePolicy().hasHeightForWidth())
        self.sekiz.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sekiz.setFont(font)
        self.sekiz.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sekiz.setMouseTracking(False)
        self.sekiz.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sekiz.setObjectName("sekiz")
        self.yedi = QtWidgets.QPushButton(self.centralwidget)
        self.yedi.setEnabled(True)
        self.yedi.setGeometry(QtCore.QRect(30, 80, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yedi.sizePolicy().hasHeightForWidth())
        self.yedi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.yedi.setFont(font)
        self.yedi.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.yedi.setMouseTracking(False)
        self.yedi.setFocusPolicy(QtCore.Qt.TabFocus)
        self.yedi.setObjectName("yedi")
        self.dort = QtWidgets.QPushButton(self.centralwidget)
        self.dort.setEnabled(True)
        self.dort.setGeometry(QtCore.QRect(30, 120, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dort.sizePolicy().hasHeightForWidth())
        self.dort.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dort.setFont(font)
        self.dort.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.dort.setMouseTracking(False)
        self.dort.setFocusPolicy(QtCore.Qt.TabFocus)
        self.dort.setObjectName("dort")
        self.bes = QtWidgets.QPushButton(self.centralwidget)
        self.bes.setEnabled(True)
        self.bes.setGeometry(QtCore.QRect(90, 120, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bes.sizePolicy().hasHeightForWidth())
        self.bes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bes.setFont(font)
        self.bes.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bes.setMouseTracking(False)
        self.bes.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bes.setObjectName("bes")
        self.alti = QtWidgets.QPushButton(self.centralwidget)
        self.alti.setEnabled(True)
        self.alti.setGeometry(QtCore.QRect(150, 120, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alti.sizePolicy().hasHeightForWidth())
        self.alti.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.alti.setFont(font)
        self.alti.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.alti.setMouseTracking(False)
        self.alti.setFocusPolicy(QtCore.Qt.TabFocus)
        self.alti.setObjectName("alti")
        self.uc = QtWidgets.QPushButton(self.centralwidget)
        self.uc.setEnabled(True)
        self.uc.setGeometry(QtCore.QRect(150, 160, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uc.sizePolicy().hasHeightForWidth())
        self.uc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.uc.setFont(font)
        self.uc.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.uc.setMouseTracking(False)
        self.uc.setFocusPolicy(QtCore.Qt.TabFocus)
        self.uc.setObjectName("uc")
        self.bir = QtWidgets.QPushButton(self.centralwidget)
        self.bir.setEnabled(True)
        self.bir.setGeometry(QtCore.QRect(30, 160, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bir.sizePolicy().hasHeightForWidth())
        self.bir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bir.setFont(font)
        self.bir.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bir.setMouseTracking(False)
        self.bir.setFocusPolicy(QtCore.Qt.TabFocus)
        self.bir.setObjectName("bir")
        self.iki = QtWidgets.QPushButton(self.centralwidget)
        self.iki.setEnabled(True)
        self.iki.setGeometry(QtCore.QRect(90, 160, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iki.sizePolicy().hasHeightForWidth())
        self.iki.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.iki.setFont(font)
        self.iki.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.iki.setMouseTracking(False)
        self.iki.setFocusPolicy(QtCore.Qt.TabFocus)
        self.iki.setObjectName("iki")
        self.sil = QtWidgets.QPushButton(self.centralwidget)
        self.sil.setEnabled(True)
        self.sil.setGeometry(QtCore.QRect(210, 30, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sil.sizePolicy().hasHeightForWidth())
        self.sil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sil.setFont(font)
        self.sil.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.sil.setMouseTracking(False)
        self.sil.setFocusPolicy(QtCore.Qt.TabFocus)
        self.sil.setObjectName("sil")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hesap Makinesi"))
        self.arti.setText(_translate("MainWindow", "+"))
        self.eksi.setText(_translate("MainWindow", "-"))
        self.bol.setText(_translate("MainWindow", "/"))
        self.carpi.setText(_translate("MainWindow", "*"))
        self.esittir.setText(_translate("MainWindow", "="))
        self.full_sil.setText(_translate("MainWindow", "C"))
        self.dokuz.setText(_translate("MainWindow", "9"))
        self.sifir.setText(_translate("MainWindow", "0"))
        self.sekiz.setText(_translate("MainWindow", "8"))
        self.yedi.setText(_translate("MainWindow", "7"))
        self.dort.setText(_translate("MainWindow", "4"))
        self.bes.setText(_translate("MainWindow", "5"))
        self.alti.setText(_translate("MainWindow", "6"))
        self.uc.setText(_translate("MainWindow", "3"))
        self.bir.setText(_translate("MainWindow", "1"))
        self.iki.setText(_translate("MainWindow", "2"))
        self.sil.setText(_translate("MainWindow", "<--"))


