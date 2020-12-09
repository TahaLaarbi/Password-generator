# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Password generator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from os import path
import sys
import random

ui,_ = loadUiType(path.join(path.dirname(__file__), "Password generator.ui"))


class MainApp(QWidget, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()


    def Handle_UI(self):
        pass
    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.test)

    def test(self):
        sma = "abcdefghijklmnopqrstuvwxyz"
        cap = sma.upper()
        num = "0123456789"
        sym = "&#!?@<>{[|`\^]}/"
        pas = ''
        if self.checkBox.isChecked():
            pas += cap
        if self.checkBox_2.isChecked():
            pas += sma
        if self.checkBox_3.isChecked():
            pas += num
        if self.checkBox_4.isChecked():
            pas += sym
        password = ''.join(random.choices(pas, k=self.spinBox.value()))
        self.lineEdit.setText(password)
        print(password)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
