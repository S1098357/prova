from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton,QDialog, QWidget, QTextEdit
import sys
from PyQt5.uic import loadUiType, loadUi
class prenotazione(QDialog):

    def __init__(self, lista1):
        super(prenotazione,self).__init__()
        loadUi("Prenotazione.ui", self)
        self.comboBox_2.addItems(lista1)
        self.comboBox.addItems(['Certificato', 'Ricetta', 'Visita Medica Generica'])
        self.textEdit.toPlainText()
        self.buttonBox.clicked.connect(self.funzionePrenotazione)

    def funzionePrenotazione(self):
        print(self.comboBox_2.currentText())
        print(self.comboBox.currentText())
        print (self.textEdit.toPlainText())

