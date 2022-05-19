import os
import pickle

from Gestione.Documento import Documento


class Ricetta(Documento):

    def __init__(self):
        super().__init__(self)
        self.farmacoPrescritto=''

    def compilaRicetta(self,farmacoPrescritto,nomePaziente,nomeCognomeDottore,dataRilascio):
        self.CompilaDocumento(self=self,nomePaziente=nomePaziente, nomeCognomeDottore=nomeCognomeDottore, dataRilascio=dataRilascio)
        self.farmacoPrescritto=farmacoPrescritto

    def stampaRicetta(self):
        ricetta=self.StampaDocumento(self)
        ricetta['farmaco prescritto']=self.farmacoPrescritto
        if os.path.isfile('ricette/Ricetta.pickle'):
            with open ('ricette/Ricetta.pickle' , 'wb+') as f:
                pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)
        else:
            with open ("ricette/",'wb+') as f:
             pickle.dump(ricetta,f,pickle.HIGHEST_PROTOCOL)

   # def prova(self):
        #if os.path.isfile('ricette/Ricetta.pickle'):
           # with open('ricette/Ricetta.pickle', 'rb') as f:
          #     print(pickle.load(f))
