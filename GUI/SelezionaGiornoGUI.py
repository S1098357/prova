from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class SelezionaGiornoGUI(QDialog):

    def __init__(self):
        super(SelezionaGiornoGUI, self).__init__()
        loadUi("SelezionaGiornoGUI.ui", self)
        self.comboBox.addItems('lunedì','martedì','mercoledì','giovedì','venerdì')
        self.stampa()

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.avanti)
        self.pushButton_2.clicked.connect(self.indietro)

    def avanti(self):
        self.close()
        match self.comboBox.currentText():
            case 'lunedì':
                return 0
            case 'martedì':
                return 1
            case 'mercoledì':
                return 2
            case 'giovedì':
                return 3
            case 'venerdì':
                return 4

    def indietro(self):
        self.close()
        return None