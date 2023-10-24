"""
E' necessario scrivere una applicazione che simula il funzionamento di un frammento del sistema
informativo di un operatore di telefonia cellulare.

Si devono quindi rappresentare i dati relativi ad una carta SIM ed in particolare:
- il numero di telefono
- il credito disponibile in euro
- la lista delle telefonate effettuate da coservare in un file.txt nominato <numero_sim>.txt)

Per ciascuna telefonata deve essere rappresentata la durata in minuti

La classe SIM dovrà fornire le seguenti funzionalità:
- un costruttore parametrizzato che crea una SIM con numero di telefono, un credito e
la lista delle telefonate vuota

- un metodo per l'inserimento di una telefonata con i dati forniti dall'utente.

- una funzione per il calcolo dei minuti totali di conversazione.

- una funzione per il calcolo delle telefonate effettuate verso un certo numero SE RIUSCITE

- una procedura per la stampa dei dati della SIM e l'elenco delle telefonate.

"""
import time
from datetime import timedelta

class Sim:
    def __init__(self,numero,credito):
        self.__numero = numero
        self.__credito = credito #cast float
        self.listaTelefonate = []

    def __str__(self) -> str:
        return f"Numero: {self.numero}, credito: {self.credito}€"
    
    def chiamata(self, numeroChiamato,durataInSec): #durata si calcola in secondi
        self.listaTelefonate.append((numeroChiamato,int(durataInSec)))
    
    def getNumero(self):
        return self.__numero
    
    def setNumero(self,newNumero):
        if newNumero.isnumeric():
            self.__numero = newNumero
        else:
            print("Telefono: inserire solo numero telefonico")
            

    def getCredito(self):
        return self.__credito
    
    def setCredito(self,newCredito):
        if newCredito.isnumeric():
            self.__credito = newCredito
        else:
            print("Credito: inserire importo in numeri")

    def minutiTotali(self): #da convertire in minuti
        minutiTotali = 0
        for chiamata in self.listaTelefonate:
            minutiTotali += chiamata[1]
        return timedelta(seconds=minutiTotali)
    
    def stampaTelefonate(self):
        #file_name= "python/esercizi/file/3201465321.txt"
        file_txt= open("file_name","a+")
        for el in self.listaTelefonate:
           file_txt.write("\n")
           file_txt.write(str(el))
        file_txt.close()

#una funzione per il calcolo delle telefonate effettuate verso un certo numero SE RIUSCITE
    def numeroPiuChiamato(self):
        contatore = 0
        for chiamata in self.listaTelefonate:
            contatore += self.listaTelefonate.count(chiamata[0])
        return contatore



#file_name = "Python/esercizi/file/3201465321.txt" #crea file nella cartella fullStuckPython e n
sim1 = Sim("3201465321","15.50")

#print(sim1)
sim1.chiamata("0114542236","120")
sim1.chiamata("0114542236","60")
sim1.chiamata("0114542236","220")
sim1.chiamata("0771558965","30")
sim1.chiamata("3354478965","45")
sim1.stampaTelefonate()



print(sim1.numeroPiuChiamato())