# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 390)
        MainWindow.setMinimumSize(QtCore.QSize(349, 390))
        MainWindow.setMaximumSize(QtCore.QSize(349, 390))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 291, 31))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"text-decoration: underline;")
        self.label.setObjectName("label")
        self.inputText = QtWidgets.QLineEdit(self.centralwidget)
        self.inputText.setGeometry(QtCore.QRect(20, 100, 311, 20))
        self.inputText.setObjectName("inputText")
        self.btntran = QtWidgets.QPushButton(self.centralwidget)
        self.btntran.setGeometry(QtCore.QRect(130, 140, 75, 23))
        self.btntran.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btntran.setObjectName("btntran")
        self.displayText = QtWidgets.QLabel(self.centralwidget)
        self.displayText.setGeometry(QtCore.QRect(20, 230, 301, 51))
        self.displayText.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.displayText.setText("")
        self.displayText.setObjectName("displayText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 291, 31))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 291, 31))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 349, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "โปรแกรมแปลภาษา ENG-TH"))
        self.label.setText(_translate("MainWindow", "โปรแกรมแปลภาษาอังกฤษ - ไทย"))
        self.btntran.setText(_translate("MainWindow", "แปลภาษา"))
        self.label_2.setText(_translate("MainWindow", "ความหมาย"))
        self.label_3.setText(_translate("MainWindow", "ป้อนคำศัพท์ภาษาอังกฤษ"))
        self.btntran.clicked.connect(self.googleTranslatorFunction)

    def googleTranslatorFunction(self):
        word=self.inputText.text()
        translator=Translator()
        result=translator.translate(word,dest='th')
        self.label_2.setText("ความหมาย คือ "+result.text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
