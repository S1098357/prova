import sys

import path as path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import PyQt5
from PyQt5.uic import loadUiType, loadUi

#FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))
from os import path


class login(QDialog):

    def __init__(self):
        super(login,self).__init__()
        loadUi("login.ui",self)
        self.buttonBox.clicked.connect(self.loginfunction)

    def loginfunction(self):
         username = self.lineEdit.text()
         password=self.lineEdit_2.text()
         return username, password





