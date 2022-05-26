from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from GUI.NuovaPrenotazioneGUI import NuovaPrenotazioneGUI


class ModificaPrenotazioneGUI(QDialog):

    def __init__(self,listaPrenotazioniCliente, listaDateDisponibili):
        super(ModificaPrenotazioneGUI, self).__init__()
        loadUi("ModificaPrenotazione.ui",self)
        self.comboBox.addItems(listaPrenotazioniCliente)
        self.x = NuovaPrenotazioneGUI(listaDateDisponibili)

    def stampa(self):
        self.show()
        self.pushButton.clicked.connect(self.chiudiFinestra)

    def chiudiFinestra(self):
        self.close()
        self.x.setWindowTitle("Modifica Prenotazione")
        self.x.stampa()