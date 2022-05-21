import datetime

from Amministrazione.Ricetta import Ricetta


x=datetime.datetime(year=1980, month=2, day=5)
y=datetime.datetime.now()
Ricetta.compilaRicetta(Ricetta, 'cacca','pipi','pupu',y)

Ricetta.stampaRicetta(Ricetta)
Ricetta.prova(Ricetta)


