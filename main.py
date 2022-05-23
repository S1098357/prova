import datetime
import sys

import datetime as datetime
from PrenotazioneGUI import prenotazione
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import datetime

#from loginGUI import login

app=QApplication(sys.argv)
lista2=[]
lista=([datetime.datetime.now(),datetime.datetime.now()])
for giorno in lista:
    lista2.append(giorno.strftime("%m/%d/%Y, %H:%M"))
mainwindow=prenotazione(lista2)
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(400)
widget.setFixedWidth(500)
widget.show()
app.exec_()


