from datetime import datetime

from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SelezionaOrarioGUI(QDialog):

    def __init__(self):
        super(SelezionaOrarioGUI, self).__init__()
        loadUi("SelezionaOrarioGUI.ui", self)
        self.comboBox.addItems('10.00-16.00', '11.00-17.00', '12.00-18.00')
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        match self.comboBox.currentText():
            case '10.00-16.00':
                return datetime.time(hours=10.00)
            case '11.00-17.00':
                return datetime.time(hours=11.00)
            case '12.00-18.00':
                return datetime.time(hours=12.00)

    def indietro(self):
        self.close()
        return None