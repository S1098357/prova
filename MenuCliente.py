from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.PrenotazioneGUI import PrenotazioneGUI



class MenuCliente(QDialog):

    def __init__(self):
        super(MenuCliente, self).__init__()
        loadUi("MenuCliente.ui", self)
        #if (self.buttonBox.isClicked):
            #self.buttonBox.clicked.connect(lambda: self.NuovaPrenotazione)
        self.x=PrenotazioneGUI(['a','b'])

    def NuovaPrenotazione(self):
        self.pushButton.clicked.connect(lambda: self.x.stampa(self))
        self.show()
        #self.stampa()
        #Cliente.richiediPrenotazione()



