from datetime import datetime


class Dottore:

    def __init__(self,nomeCognome,numTelefono):
        self.clienteAttuale=Cliente
        self.listaPrenotazioni=[]
        self.nomeCognome=nomeCognome
        self.numeroDiTelefono=numTelefono
        self.OrarioLavoro=[]
        self.listaCartelleCliniche=[]
        self.documento

    def ricercaCartellaClinica(self,id):
        for CC in self.listaCartelleCliniche:
            if CC.GetId==id
                return CC

    def aggiornaCartellaClinica(self):
        if self.ClienteAttuale.nomeCognome!='':
            CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
            CC.setPatologie(Grafica.contenuto)
            CC.stampaCartella
        else:
            Grafica.errore

    def chiamaClienteSuccessivo(self):
        for prenotazione in self.listaPrenotazioni:
            if prenotazione.nomeCliente==self.clienteAttuale.nomeCognome:
                appoggio=listaPrenotazioni.index(prenotazione)
                appoggio2=listaPrenotazioni.item(appoggio+1)
        self.ClienteAttuale=Segreteria.ricercaCliente(appoggio2.nomeCliente)

    def compilaCertificato(self):
        tipo=grafica.tipoCertificato()
        if tipo=='certificato di malattia':
            self.documento=CertificatoMalattia()
        else:
            if tipo=='certificato sana e robusta costituzione'
                self.documento=CertificatoSanaERobustaCostituzione()
            else:
                self.documento=CertificatoAgoistico()
        self.certificatoMedico.compilaCertificato(self.nomeCognome, self.clienteAttuale.nomeCognome, datetime.now())

    def prescriviFarmaco(self):
        self.documento.compilaRicetta(self.clienteAttuale.nomeCognome,self.nomeCognome,datetime.now(),grafica.compilaRicetta())

    def setDataOraLavoro(self):
        self.orarioLavoro.append(grafica.scegliOrario())

    def visualizzaCartellaClienteAttuale(self):
        if self.ClienteAttuale.nomeCognome!='':
            CC=self.ricercaCartellaClinica(self.ClienteAttuale.id)
            Grafica.visualizza(CC.leggiCartella())
        else:
            Grafica.errore

    def visualizzaPrenotazioni(self):
        grafica.Visualizza(self.listaPrenotazioni)