from PyQt5.QtWidgets import QDialog,QMainWindow
from PyQt5.uic import loadUiType, loadUi

class prenotazione(QDialog):

    def __init__(self):
        super(prenotazione,self).__init__()
        loadUi("Prenotazione.ui",self)
        #self.buttonBox.clicked.connect(self.loginfunction)
        self.loginfunction

    def loginfunction(self):
         listaDate = self.comboBox
         tipoAppuntamento=self.comboBox_2
         note = self.textEdit.text()
         listaDate.addItem('ciao')
         listaDate.activated[str].connect(self.onChanged)
         return listaDate, tipoAppuntamento


    def onChanged(self,text):
        self.QLabel.setText(text)
        self.QLabel.adjustSize()
